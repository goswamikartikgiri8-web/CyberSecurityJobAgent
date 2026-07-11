from typing import List
from providers.base_provider import BaseProvider
from models.job import Job


class ProviderManager:

    def __init__(self):
        self.providers: List[BaseProvider] = []

    def register(self, provider: BaseProvider):
        self.providers.append(provider)

    def fetch_all(self) -> List[Job]:

        jobs = []

        for provider in self.providers:

            print(f"[+] {provider.name}")

            try:
                results = provider.fetch_jobs()
                print(f"    {len(results)} jobs")

                jobs.extend(results)

            except Exception as e:
                print(f"    ERROR : {e}")

        return jobs