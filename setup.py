#! /usr/bin/env python
import os
import sys
import subprocess
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points

from setuptools.command.build_ext import build_ext as _build_ext
from numpy.distutils.fcompiler import new_fcompiler
from scripting.contexts import cd


common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [
    ],
    "define_macros": [
    ],
    "undef_macros": [
    ],
    "extra_compile_args": [
    ],
    "language": "c",
}

libraries = [
]

# Locate directories under Windows %LIBRARY_PREFIX%.
if sys.platform.startswith("win"):
    common_flags["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
    common_flags["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))

ext_modules = [
    Extension(
        "pymt_prms_streamflow.lib.prmsstreamflow",
        ["pymt_prms_streamflow/lib/prmsstreamflow.pyx"],
        libraries=libraries + ["bmiprmsstreamflow"],
        extra_objects=['pymt_prms_streamflow/lib/bmi_interoperability.o'],
        **common_flags
    ),
]

packages = find_packages()
pymt_components = [(
        "PRMSStreamflow=pymt_prms_streamflow.bmi:PRMSStreamflow",
        "meta/PRMSStreamflow",
    ),
]


def build_interoperability():
    compiler = new_fcompiler()
    compiler.customize()

    cmd = []
    cmd.append(compiler.compiler_f90[0])
    cmd.append(compiler.compile_switch)
    if sys.platform.startswith("win") is False:
        cmd.append("-fPIC")
    for include_dir in common_flags['include_dirs']:
        if os.path.isabs(include_dir) is False:
            include_dir = os.path.join(sys.prefix, "include", include_dir)
        cmd.append('-I{}'.format(include_dir))
    cmd.append('bmi_interoperability.f90')

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        raise


class build_ext(_build_ext):

    def run(self):
        with cd('pymt_prms_streamflow/lib'):
            build_interoperability()
        _build_ext.run(self)


cmdclass = get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass())
cmdclass["build_ext"] = build_ext

setup(
    name="pymt_prms_streamflow",
    author="Community Surface Dynamics Modeling System",
    description="PyMT plugin for prms_streamflow",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=get_entry_points(pymt_components),
)
