"""Top-level package for titorium EGDA."""

__author__ = """Roberto Arce Aguirre"""
__email__ = 'roberto_arce_@hotmail.com'


# Modules
from . import time_series  # noqa : F401
from . import flow  # noqa : F401
from . import proportion  # noqa : F401
from . import distribution  # noqa : F401
from . import correlation  # noqa : F401
from . import ranking  # noqa : F401

# Functions
from .utils import create_fake_dataset  # noqa : F401


class showcase:
    def __init__(self, df1):
        self.df = df1
