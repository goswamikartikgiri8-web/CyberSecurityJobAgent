from typing import List
from models.job import Job


class SearchManager:

    def __init__(self):
        self.providers = []

    def register(self, provider):
        self.providers.append(provider)

    def run(self) -> List[Job]:

        jobs = []

        print("\nStarting Job Search...\n")

        for provider in self.providers:

            try:

                print(f"Searching {provider.__class__.__name__}")

                results = provider.fetch_jobs()

                print(f"Found {len(results)} Jobs")

                jobs.extend(results)

            except Exception as e:

                print(f"{provider.__class__.__name__} Failed")

                print(e)

        return jobs