<div align="center">

# 🔍 Network Checker PRO  
### ⚡ Modern · Fast · Clean · Portable Network Diagnostics Tool

A lightweight, portable network analyzer for Windows — no installation required.

Developed by **Milad Hadad**

<br>

<img src="https://img.shields.io/badge/version-v1.0.0-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/status-stable-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/language-python-yellow?style=for-the-badge"/>

</div>

---

## ✨ ویژگی‌ها

- 📡 تست اتصال اینترنت (Ping خودکار به چند DNS معتبر)
- 🧭 بررسی کامل شبکه: Gateway / DNS / IP
- 🖥 نمایش IP محلی و عمومی (بدون افشای اطلاعات واقعی کاربر)
- 🌍 تست همزمان چند وب‌سایت — قابل شخصی‌سازی
- 🔐 تست TCP پورت 443 (HTTPS Connectivity)
- 🌐 تست HTTP GET بدون کتابخانه جانبی
- 🧪 تشخیص صحیح رفتار سایت‌ها در بلاک‌کردن ICMP و TCP
- 📦 امکان ساخت نسخه Portable (EXE)
- 📝 خروجی حرفه‌ای، تمیز، قابل خواندن و قابل انتشار

---

## 🚀 نصب و اجرا

### ▶ اجرای نسخه Python

```bash
# ساخت محیط مجازی (اختیاری)
python -m venv .venv
.venv\Scripts\activate

# نصب نیازمندی‌ها (در صورت نیاز)
pip install -r requirements.txt

# اجرا
python network_checker_pro.py

---

## 🌐 Sample Output (Demo)

> ✔️ این خروجی یک نمونه است — اطلاعات واقعی شبکه نمایش داده نمی‌شود.

```text
🌐 UNIVERSAL NETWORK CHECKER PRO
────────────────────────────────────

📌 Local IP: 192.168.1.10
📌 Network Class: Class C

🔍 Checking Global Internet...

➡️  Pinging DNS 8.8.8.8 ...
   ✅ DNS reachable

🌍 Testing Websites...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 google.com
   📡 Ping:        ✅ OK
   🔐 TCP 443:     ✅ OK
   🌍 HTTP GET:    ✅ OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 youtube.com
   📡 Ping:        ❌ Fail
   🔐 TCP 443:     ❌ Fail
   🌍 HTTP GET:    ❌ Fail

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 cloudflare.com
   📡 Ping:        ✅ OK
   🔐 TCP 443:     ✅ OK
   🌍 HTTP GET:    ✅ OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 microsoft.com
   📡 Ping:        ❌ Blocked
   🔐 TCP 443:     ✅ OK
   🌍 HTTP GET:    ✅ OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 hamrah.academy
   📡 Ping:        ❌ Blocked
   🔐 TCP 443:     ✅ OK
   🌍 HTTP GET:    ❌ Fail

────────────────────────────────────
✔ TEST FINISHED — Developed by Milad Hadad
────────────────────────────────────
