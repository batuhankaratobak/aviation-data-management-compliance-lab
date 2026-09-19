from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
required = ["README.md", "01-company-profile.md", "02-isms-scope.md", "03-risk-methodology.md", "04-information-security-policy.md", "05-internal-audit-report.md", "06-access-control-procedure.md", "07-incident-response-procedure.md", "08-backup-and-recovery-procedure.md", "09-internal-audit-checklist.md", "PROJECT_STATUS.md", "CISO_ASSISTANT_LOCAL_SETUP.md", "CISO_ASSISTANT_DATA_ENTRY_GUIDE.md", "scripts/validate_project.py", ".gitignore", "evidence/README.md", "BK-ISO27001-ISMS-Simulation.xlsx"]
fails, warns = [], []
def result(ok, msg, warning=False):
    (warns if warning else fails).append(("WARNING" if warning else "FAIL", msg)) if not ok else print("PASS: " + msg)

for f in required: result((ROOT/f).exists(), f"required file: {f}")
xlsx = ROOT / "BK-ISO27001-ISMS-Simulation.xlsx"
if xlsx.exists():
    try:
        with zipfile.ZipFile(xlsx) as z:
            wb = ET.fromstring(z.read("xl/workbook.xml"))
            ns = {"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            sheets = [s.attrib.get("name") for s in wb.findall("m:sheets/m:sheet", ns)]
            xml_text = "\n".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist() if n.endswith(".xml"))
        expected_sheets = ["Asset Inventory", "Risk Register", "Risk Treatment", "SoA", "CAPA Register", "Aviation Data Inventory", "Data Quality Register", "Regulatory Requirements Matrix", "Regulatory Data Submission Log", "Aviation Audit & CAPA"]
        for s in expected_sheets: result(s in sheets, f"sheet exists: {s}")
        result(len(sheets) == 10, "exactly ten project sheets")
        for prefix, count in [("A-",10),("R-",10),("F-",4),("C-",4)]:
            found = set(re.findall(prefix + r"0[1-9]|" + prefix + r"10", xml_text)) if prefix in ("A-","R-") else set(re.findall(prefix + r"0[1-4]", xml_text))
            result(len(found) >= count, f"xlsx contains {count} {prefix} records")
        result(xml_text.count("F") > 0 and xml_text.count("G") > 0, "risk score formula cells present", warning=True)
        for token in ["AVI-01", "AVI-06", "DQ-01", "DQ-06", "REG-01", "REG-04", "SUB-01", "SUB-04", "AV-CAPA-01", "AV-CAPA-04", "Accuracy", "Completeness", "Consistency", "Timeliness", "Traceability", "CSV", "XML", "JSON", "API", "SFTP"]:
            result(token in xml_text, f"aviation reference: {token}")
        for token in ["R-01", "R-08", "R-10", "A.5.18", "A.5.24", "A.8.15", "A.8.16"]:
            result(token in xml_text, f"cross-reference: {token}")
    except Exception as e: fails.append(("FAIL", f"xlsx readable: {e}"))
# Record IDs are authoritative in the Excel workbook. Do not search only Markdown
# files here: the four previous warnings were false positives caused by that scope.
all_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*.md"))
result("Karatopak" not in all_text, "no misspelled Karatobak")
result(not re.search(r"ISO certified|fully compliant", all_text, re.I), "no prohibited certification/compliance claims")
result(not re.search(r"(I have|my|our) (professional )?(aviation|SHGM|EASA|IATA|ICAO) experience|professional experience (with|in) (aviation|SHGM|EASA|IATA|ICAO)|real (SHGM|EASA|IATA|ICAO) submission was made", all_text, re.I), "no real aviation experience or submission claims")
secret_files = [p for p in ROOT.rglob("*") if p.is_file() and (p.name.startswith(".env") or "secret" in p.name.lower() or "api_key" in p.name.lower())]
result(not secret_files, "no .env, secret, or API key files")
for status, msg in fails + warns: print(f"{status}: {msg}")
print(f"Summary: {len(fails)} FAIL, {len(warns)} WARNING")
raise SystemExit(1 if fails else 0)
