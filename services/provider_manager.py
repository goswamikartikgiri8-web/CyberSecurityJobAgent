class ProviderManager:

    def __init__(self):
        self.providers = []

    def register(self, provider):
        self.providers.append(provider)

    def fetch_all(self):

        jobs = []

        print()

        for provider in self.providers:

            print(f"[+] {provider.name}")

            try:

                provider_jobs = provider.fetch_jobs()

                print(f"    {len(provider_jobs)} jobs")

                jobs.extend(provider_jobs)

            except Exception as e:

                print(f"    Failed ({e})")

        return jobs