from providers.greenhouse import GreenhouseProvider
from providers.lever import LeverProvider
from providers.adzuna import AdzunaProvider


def load_providers():
    return [

        GreenhouseProvider(),

        LeverProvider(),

        AdzunaProvider(),

    ]