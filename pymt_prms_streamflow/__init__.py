#! /usr/bin/env python

from .bmi import (PRMSStreamflow,
)

__all__ = ["PRMSStreamflow",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
