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
from tegda.graphs.utils import create_fake_dataset, classify_cols   # noqa : F401

from .Target import *


class showcase:

    def __init__(self, df1, target):
        self.df = df1
        self.target = target

        classify = classify_cols(df1)
