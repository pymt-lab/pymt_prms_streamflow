#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_prms_streamflow").version


from .bmi import PRMSStreamflow

__all__ = [
    "PRMSStreamflow",
]
