from providers.greenhouse import GreenhouseProvider
from providers.lever import LeverProvider
from providers.adzuna import AdzunaProvider
from providers.naukri import NaukriProvider

def load_providers():
    return [

        GreenhouseProvider(),

        LeverProvider(),

        AdzunaProvider(),

        NaukriProvider(),


    ]