class JobFilter:

    # -----------------------------
    # Cyber Security Roles
    # -----------------------------
    INCLUDE = [

        "cyber",
        "security",
        "soc",
        "soc analyst",
        "security analyst",
        "security engineer",
        "security consultant",
        "security operations",
        "information security",
        "network security",
        "cloud security",
        "application security",
        "product security",
        "vapt",
        "penetration",
        "pentest",
        "ethical hacker",
        "red team",
        "blue team",
        "incident response",
        "threat",
        "threat intelligence",
        "grc",
        "iam",
        "pam",
        "siem",
        "splunk",
        "dfir",
        "digital forensics",
        "forensics",

    ]

    # -----------------------------
    # Ignore These Roles
    # -----------------------------
    EXCLUDE = [

        # Teaching
        "professor",
        "assistant professor",
        "associate professor",
        "faculty",
        "trainer",
        "teacher",

        # Non Technical
        "sales",
        "marketing",
        "customer success",
        "business development",
        "presales",
        "pre sales",

        # Senior Roles
        "senior",
        "lead",
        "staff",
        "principal",
        "manager",
        "director",
        "head",
        "vice president",
        "vp",
        "architect",
        "distinguished",

    ]

    # -----------------------------
    # Allowed Experience
    # -----------------------------
    EXPERIENCE_ALLOWED = [

        "intern",
        "internship",
        "graduate",
        "apprentice",

        "fresher",
        "freshers",
        "entry level",

        "0 year",
        "0 years",

        "0-1",
        "0 - 1",

        "0-2",
        "0 - 2",

        "1-2",
        "1 - 2",

        "1-3",
        "1 - 3",

        "2 year",
        "2 years",

        "not specified",
        "",

    ]

    # -----------------------------
    # Remove Duplicate Jobs
    # -----------------------------
    @staticmethod
    def remove_duplicates(jobs):

        unique = []
        seen = set()

        for job in jobs:

            company = (job.company or "").strip().lower()
            title = (job.title or "").strip().lower()

            key = (company, title)

            if key in seen:
                continue

            seen.add(key)
            unique.append(job)

        return unique

    # -----------------------------
    # Filter Jobs
    # -----------------------------
    @staticmethod
    def filter_jobs(jobs):

        filtered = []

        for job in jobs:

            title = (job.title or "").lower()
            experience = (job.experience or "").lower()

            # Ignore unwanted jobs
            if any(word in title for word in JobFilter.EXCLUDE):
                continue

            # Must be Cyber Security related
            if not any(word in title for word in JobFilter.INCLUDE):
                continue

            # Experience filter
            if not any(exp in experience for exp in JobFilter.EXPERIENCE_ALLOWED):
                continue

            filtered.append(job)

        return filtered