from dataclasses import dataclass


@dataclass(slots=True)
class Job:
    company: str
    title: str
    location: str
    experience: str
    salary: str
    posted: str
    apply_link: str
    source: str