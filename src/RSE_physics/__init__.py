import numpy as np
if not hasattr(np, 'cumproduct'):
    np.cumproduct = np.cumprod

from .core import calc_speed

__all__ = ["calc_speed"]
