from playwright.sync_api import sync_playwright

from models.job import Job
from providers.base_provider import BaseProvider


KEYWORDS = [
    "cyber security",
    "cybersecurity",
    "soc analyst",
    "security analyst",
    "security engineer",
    "product security",
    "application security",
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


class NaukriProvider(BaseProvider):

    name = "Naukri"

    URL = "https://www.naukri.com/cyber-security-jobs"

    def fetch_jobs(self):

        jobs = []

        try:

            with sync_playwright() as p:

                browser = p.chromium.launch(headless=True)

                page = browser.new_page()

                page.goto(
                    self.URL,
                    wait_until="networkidle",
                    timeout=60000
                )

                cards = page.locator("article")

                for i in range(cards.count()):

                    card = cards.nth(i)

                    try:
                        title = card.locator("a.title").inner_text().strip()
                    except:
                        continue

                    if not any(
                        keyword.lower() in title.lower()
                        for keyword in KEYWORDS
                    ):
                        continue

                    try:
                        company = card.locator(".comp-name").inner_text().strip()
                    except:
                        company = "Not Specified"

                    try:
                        location = card.locator(".locWdth").inner_text().strip()
                    except:
                        location = "Not Specified"

                    try:
                        experience = card.locator(".expwdth").inner_text().strip()
                    except:
                        experience = "Not Specified"

                    try:
                        salary = card.locator(".sal-wrap").inner_text().strip()
                    except:
                        salary = "Not Specified"

                    try:
                        apply_link = card.locator("a.title").get_attribute("href")
                    except:
                        apply_link = ""

                    jobs.append(

                        Job(

                            company=company,

                            title=title,

                            location=location,

                            experience=experience,

                            salary=salary,

                            posted="",

                            apply_link=apply_link,

                            source="Naukri"

                        )

                    )

                browser.close()

            return jobs

        except Exception:

            return []