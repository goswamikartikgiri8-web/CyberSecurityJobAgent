from database.sqlite import JobDatabase

from services.provider_manager import ProviderManager
from services.provider_registry import load_providers
from services.email_service import EmailService


def main():

    print("=" * 60)
    print("Cyber Security Job Agent")
    print("=" * 60)

    db = JobDatabase()

    manager = ProviderManager()

    for provider in load_providers():
        manager.register(provider)

    jobs = manager.fetch_all()

    print("\n" + "=" * 60)
    print(f"TOTAL JOBS COLLECTED : {len(jobs)}")
    print("=" * 60)

    new_jobs = []
    duplicates = 0

    for job in jobs:

        if db.save(job):

            new_jobs.append(job)

            print(f"Saved      : {job.company} | {job.title}")

        else:

            duplicates += 1

            print(f"Duplicate  : {job.company} | {job.title}")

    print()

    if len(new_jobs) > 0:

        print("Sending Email...")

        try:

            EmailService().send(new_jobs)

        except Exception as e:

            print(f"Email Error : {e}")

    else:

        print("No New Jobs. Email Skipped.")

    print("\n" + "=" * 60)
    print(f"New Jobs   : {len(new_jobs)}")
    print(f"Duplicates : {duplicates}")
    print("=" * 60)


if __name__ == "__main__":
    main()