import os
import requests
from dotenv import load_dotenv

from providers.base_provider import BaseProvider
from models.job import Job

load_dotenv()


class AdzunaProvider(BaseProvider):

    name = "Adzuna"

    URL = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    def fetch_jobs(self):

        params = {
            "app_id": os.getenv("ADZUNA_APP_ID"),
            "app_key": os.getenv("ADZUNA_APP_KEY"),
            "what": "cyber security",
            "results_per_page": 20
        }

        response = requests.get(self.URL, params=params, timeout=30)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get("results", []):

            jobs.append(
                Job(
                    company=item.get("company", {}).get("display_name", "Unknown"),
                    title=item.get("title", ""),
                    location=item.get("location", {}).get("display_name", ""),
                    experience="Not Specified",
                    salary="",
                    posted=item.get("created", ""),
                    apply_link=item.get("redirect_url", ""),
                    source="Adzuna"
                )
            )

        return jobs