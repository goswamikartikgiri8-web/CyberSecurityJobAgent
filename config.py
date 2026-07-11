import os
from dotenv import load_dotenv

load_dotenv()

# Email Settings
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Database
DATABASE_PATH = "database/jobs.db"

# Search Settings
KEYWORDS = [
    "Cyber Security Intern",
    "SOC Analyst",
    "SOC Intern",
    "VAPT",
    "Penetration Tester",
    "Ethical Hacker",
    "Information Security",
    "Digital Forensics"
]

LOCATIONS = [
    "Ahmedabad",
    "Gandhinagar",
    "Gujarat",
    "Bengaluru",
    "Pune",
    "Hyderabad",
    "Mumbai",
    "Delhi NCR",
    "Remote"
]