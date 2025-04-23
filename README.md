# Akira-Outfit 👗🛒
*A minimalist fashion-store demo built with Django 4.2 and Razorpay.*

[![Build](https://img.shields.io/github/actions/workflow/status/IftikharZulfiqar/akira-outfit/ci.yml?label=build)](../../actions)
[![License](https://img.shields.io/github/license/IftikharZulfiqar/akira-outfit)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/IftikharZulfiqar/akira-outfit)](../../commits)

---

## ✨ Features
- Responsive product catalogue with image zoom
- Shopping cart and Razorpay-powered checkout
- Admin dashboard for inventory & orders
- Container-first deployment (Gunicorn + Docker Compose)
- CI ready for GitHub Actions

## 🏗️ Tech stack

| Layer       | Technology |
|-------------|------------|
| Backend     | **Django 4.2** :contentReference[oaicite:0]{index=0} |
| Runtime     | Gunicorn, Python 3.10 (slim) :contentReference[oaicite:1]{index=1} |
| Payments    | Razorpay SDK |
| Database    | SQLite in dev / PostgreSQL in prod |
| Container   | Docker, docker-compose :contentReference[oaicite:2]{index=2} |

---

## 🚀 Quick start

### 1. Clone & configure
```bash
git clone https://github.com/IftikharZulfiqar/akira-outfit.git
cd akira-outfit
cp .env.example .env        # add your Razorpay keys
