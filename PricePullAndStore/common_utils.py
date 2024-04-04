import pandas as pd
import numpy as np


def enforce_list(input):
    if isinstance(input, list) or isinstance(input, np.ndarray) or isinstance(input, tuple):
        return input
    elif isinstance(input, str):
        return [input]
