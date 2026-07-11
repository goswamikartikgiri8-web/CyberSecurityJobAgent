import requests

from providers.base_provider import BaseProvider
from models.job import Job


GREENHOUSE_BOARDS = [
    "cloudflare",
    "gitlab",
    "snyk",
    "fivetran",
    "chainguard",
    "sourcegraph",
    "cockroachlabs",
    "hashicorp"
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


class GreenhouseProvider(BaseProvider):

    name = "Greenhouse"

    def fetch_jobs(self):

        jobs = []

        for board in GREENHOUSE_BOARDS:

            try:

                url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

                response = requests.get(url, timeout=20)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("jobs", []):

                    title = item.get("title", "")

                    if not any(k.lower() in title.lower() for k in KEYWORDS):
                        continue

                    jobs.append(

                        Job(

                            company=board.title(),

                            title=title,

                            location=item.get("location", {}).get("name", ""),

                            experience="Not Specified",

                            salary="",

                            posted="",

                            apply_link=item.get("absolute_url", ""),

                            source="Greenhouse"

                        )

                    )

            except Exception:
                pass

        return jobs