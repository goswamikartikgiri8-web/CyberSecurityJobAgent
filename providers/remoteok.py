from providers.base_provider import BaseProvider
from models.job import Job


class RemoteOKProvider(BaseProvider):

    def fetch_jobs(self):

        return [

            Job(

                company="Cisco",

                title="SOC Analyst Intern",

                location="Bangalore",

                experience="Fresher",

                salary="₹6-8 LPA",

                posted="Today",

                apply_link="https://jobs.cisco.com",

                source="Demo"

            )

        ]