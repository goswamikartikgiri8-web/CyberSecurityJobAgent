from database.sqlite import JobDatabase

from services.provider_manager import ProviderManager
from services.provider_registry import load_providers
from services.email_service import EmailService
from services.job_filter import JobFilter
from services.job_sorter import JobSorter


def main():

    print("=" * 60)
    print("Cyber Security Job Agent")
    print("=" * 60)

    db = JobDatabase()

    manager = ProviderManager()

    # Register Providers
    for provider in load_providers():
        manager.register(provider)

    # Fetch Jobs
    jobs = manager.fetch_all()

    print("\n" + "=" * 60)
    print(f"TOTAL JOBS COLLECTED : {len(jobs)}")
    print("=" * 60)

    # Remove Duplicate Jobs
    jobs = JobFilter.remove_duplicates(jobs)

    # Keep only relevant jobs
    jobs = JobFilter.filter_jobs(jobs)

    # Sort Jobs
    jobs = JobSorter.sort(jobs)

    print(f"After Filters : {len(jobs)} Jobs\n")

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

    # Sort again before email
    new_jobs = JobSorter.sort(new_jobs)

    if new_jobs:

        print("Sending Email...")

        try:

            EmailService().send(new_jobs)

        except Exception as e:

            print(f"Email Error : {e}")

    else:

        print("No New Jobs. Email Skipped.")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Collected Jobs : {len(jobs)}")
    print(f"New Jobs       : {len(new_jobs)}")
    print(f"Duplicates     : {duplicates}")
    print("=" * 60)


if __name__ == "__main__":
    main()