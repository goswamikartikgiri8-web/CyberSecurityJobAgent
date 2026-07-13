class JobSorter:

    PRIORITY = [

        "intern",
        "internship",
        "apprentice",
        "graduate",
        "trainee",
        "associate",

        "soc analyst",
        "security analyst",
        "cyber security analyst",

        "security engineer",
        "cyber security engineer",

        "security consultant",

        "vapt",
        "penetration tester",
        "ethical hacker",

    ]

    @staticmethod
    def priority(job):

        title = (job.title or "").lower()

        for i, keyword in enumerate(JobSorter.PRIORITY):

            if keyword in title:
                return i

        return 999

    @staticmethod
    def sort(jobs):

        return sorted(

            jobs,

            key=lambda job: (

                JobSorter.priority(job),

                (job.company or "").lower(),

                (job.title or "").lower()

            )

        )