# BK-ISO27001-Lab

### ISO/IEC 27001 ISMS + Aviation Data Management Simulation

![Status](https://img.shields.io/badge/status-educational%20simulation-2563EB)
![ISO](https://img.shields.io/badge/ISO%2FIEC%2027001-ISMS%20lab-0F766E)
![Aviation](https://img.shields.io/badge/aviation-data%20management-basic%20awareness-7C3AED)
![Validation](https://img.shields.io/badge/validation-0%20fail%20%7C%200%20warning-16A34A)

> **Portfolio project · simulated environment · no real regulatory submission**

Karatobak Technology Lab için Batuhan Karatobak tarafından hazırlanmış eğitim ve portföy amaçlı bir ISO/IEC 27001 Information Security Management System simülasyonudur. Proje, genel ISMS risk çalışmasına ek olarak havacılık veri yönetimi ve temel düzenleyici farkındalık katmanı içerir.

## ⚠️ Scope & disclaimer

Bu proje:

- Gerçek ISO sertifikası veya resmi denetim değildir.
- Gerçek SHGM bildirimi, şirket sistemi veya otorite deneyimi değildir.
- Gerçek müşteri verisi, şifre, API key, gizli bilgi veya sahte denetim kanıtı içermez.
- Havacılık içeriğini yalnızca **simulated/basic awareness** seviyesinde ele alır.
- Bazı kontrolleri `Planned`, `Documentation Only`, `Partially Implemented` veya `Evidence Pending` durumundadır.

## 🎯 Project focus

| Layer | Focus |
|---|---|
| ISMS | Varlık envanteri, risk değerlendirmesi, treatment, SoA, CAPA ve iç denetim |
| Aviation data | Flight, passenger, aircraft, crew, maintenance ve operational delay data |
| Data quality | Accuracy, Completeness, Consistency, Timeliness, Traceability |
| Data exchange | CSV, XML, JSON, API ve SFTP örnek akışları |
| Regulatory awareness | SHGM, EASA, IATA ve ICAO’nun temel ve ayrı bağlamları |

## 📊 Workbook overview

`BK-ISO27001-ISMS-Simulation.xlsx` içindeki sekmeler:

| ISMS core | Aviation data layer |
|---|---|
| Asset Inventory | Aviation Data Inventory |
| Risk Register | Data Quality Register |
| Risk Treatment | Regulatory Requirements Matrix |
| SoA | Regulatory Data Submission Log |
| CAPA Register | Aviation Audit & CAPA |

## 🏛️ Regulatory awareness boundary

- **SHGM:** Türkiye sivil havacılık otoritesi bağlamı.
- **EASA:** Avrupa Birliği havacılık emniyeti düzenleyicisi bağlamı.
- **IATA:** Havayolu sektör kuruluşu ve sektör uygulamaları bağlamı; otorite değildir.
- **ICAO:** Uluslararası sivil havacılık standartları ve iş birliği bağlamı.

Bu isimler birbirinin yerine kullanılmaz; proje gerçek uygulanabilirlik veya hukuki yorum iddiasında bulunmaz.

## 🧪 Validation

```bash
python3 scripts/validate_project.py
```

Validation; dosya bütünlüğünü, Excel sekmelerini, asset/risk/CAPA referanslarını, havacılık veri bağlantılarını, kontrol ID’lerini, yasaklı iddiaları ve gizli dosyaları kontrol eder.

Beklenen çıktı:

```text
Summary: 0 FAIL, 0 WARNING
```

## 📁 Documentation map

- `01-company-profile.md` — Kurgusal şirket profili
- `02-isms-scope.md` — ISMS kapsamı
- `03-risk-methodology.md` — Risk puanlama yöntemi
- `04-information-security-policy.md` — Bilgi güvenliği politikası
- `05-internal-audit-report.md` — Örnek iç denetim raporu
- `06-08-*.md` — Erişim, olay ve yedekleme prosedürleri
- `09-internal-audit-checklist.md` — İç denetim kontrol listesi
- `PROJECT_STATUS.md` — Proje durumu ve sınırlar
- `evidence/README.md` — Örnek kanıt kapsamı

> CISO Assistant bu proje için zorunlu değildir; yalnızca opsiyonel bir eğitim aracı olarak değerlendirilebilir.
