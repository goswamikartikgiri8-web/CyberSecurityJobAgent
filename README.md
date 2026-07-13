# 🛡 Cyber Security Job Agent

An automated Python-based job aggregator that collects the latest Cyber Security jobs from multiple job portals and sends a beautifully formatted email report every day.

---

## 🚀 Features

- Collects jobs from multiple providers
- Removes duplicate jobs
- Filters only Cyber Security jobs
- Filters Fresher / Internship / 0–2 Years jobs
- Sorts jobs by priority
- Stores previous jobs using SQLite
- Sends HTML email reports
- Attaches CSV report
- Runs automatically every day using GitHub Actions

---

## 📌 Supported Job Providers

- ✅ Greenhouse
- ✅ Lever
- ✅ Adzuna
- ✅ Naukri
- ⚠️ Wellfound (disabled because of bot protection)

---

## 🛠 Tech Stack

- Python 3.13
- Playwright
- Requests
- SQLite
- BeautifulSoup
- GitHub Actions
- Gmail SMTP

---

## 📂 Project Structure

```
CyberSecurityJobAgent/

│
├── database/
│   └── sqlite.py
│
├── models/
│   └── job.py
│
├── providers/
│   ├── greenhouse.py
│   ├── lever.py
│   ├── adzuna.py
│   ├── naukri.py
│   └── wellfound.py
│
├── services/
│   ├── email_service.py
│   ├── job_filter.py
│   ├── job_sorter.py
│   ├── provider_manager.py
│   └── provider_registry.py
│
├── .github/
│   └── workflows/
│       └── daily_jobs.yml
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/goswamikartikgiri8-web/CyberSecurityJobAgent.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright

```bash
playwright install chromium
```

Create a `.env`

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=your_email@gmail.com

ADZUNA_APP_ID=xxxxxxxx
ADZUNA_APP_KEY=xxxxxxxx
```

Run

```bash
python main.py
```

---

## 📧 Email Preview

Each report contains:

- Company
- Job Title
- Location
- Experience
- Salary
- Source
- Apply Link

Along with a downloadable CSV attachment.

---

## 🤖 Automation

The project uses GitHub Actions to execute automatically every day.

---

## 📈 Future Improvements

- LinkedIn Integration
- Indeed Integration
- Glassdoor Integration
- Telegram Notifications
- Discord Notifications
- AI Job Ranking
- Resume Matching

---

## 👨‍💻 Author

**Kartikgiri Goswami**

MSc Cyber Security

Python • SOC • VAPT • Automation • Cyber Security