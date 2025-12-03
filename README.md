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

- 📡 تست اتصال اینترنت (Ping خودکار به چند DNS)
- 🧭 بررسی کامل وضعیت شبکه: Gateway / DNS / IP
- 🖥 نمایش IP محلی و عمومی (بدون افشای اطلاعات واقعی)
- 🌍 تست همزمان چند وب‌سایت — کاملاً قابل‌شخصی‌سازی
- 🔐 تست TCP به پورت 443 برای بررسی HTTPS
- 🌐 تست HTTP GET بدون نیاز به کتابخانه جانبی
- 🧪 رفتار دقیق سایت‌ها در بلاک‌کردن ICMP/TCP
- 📦 قابلیت ساخت نسخه Portable (EXE)
- 📝 خروجی حرفه‌ای، قابل انتشار و قابل خواندن

---

## 🚀 نصب و اجرا

### ▶ اجرای نسخه Python

```bash
# ساخت محیط مجازی (اختیاری)
python -m venv .venv
.venv\Scripts\activate

# نصب نیازمندی‌ها
pip install -r requirements.txt

# اجرا
python network_checker_pro.py
