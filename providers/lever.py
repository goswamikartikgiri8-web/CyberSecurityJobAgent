import requests

from providers.base_provider import BaseProvider
from models.job import Job


LEVER_COMPANIES = [
    "crowdstrike",
    "digitalocean",
    "elastic",
    "canonical",
    "mixpanel",
    "postman",
    "zapier",
    "udemy"
]


KEYWORDS = [
    "cyber security",
    "cybersecurity",
    "soc analyst",
    "security analyst",
    "security engineer",
    "application security",
    "product security",
    "cloud security",
    "devsecops",
    "incident response",
    "threat intelligence",
    "penetration",
    "pentest",
    "vapt",
    "red team",
    "blue team",
    "dfir",
    "digital forensics",
    "forensics",
    "iam",
    "grc",
    "siem"
]


class LeverProvider(BaseProvider):

    name = "Lever"

    def fetch_jobs(self):

        jobs = []

        for company in LEVER_COMPANIES:

            try:

                url = f"https://api.lever.co/v0/postings/{company}?mode=json"

                response = requests.get(url, timeout=20)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data:

                    title = item.get("text", "")

                    if not any(word in title.lower() for word in KEYWORDS):
                        continue

                    jobs.append(

                        Job(

                            company=company.title(),

                            title=title,

                            location=item.get("categories", {}).get("location", ""),

                            experience="Not Specified",

                            salary="",

                            posted=item.get("createdAt", ""),

                            apply_link=item.get("hostedUrl", ""),

                            source="Lever"

                        )

                    )

            except Exception:
                pass

        return jobs