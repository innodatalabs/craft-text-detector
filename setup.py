import io
import os
import re
from datetime import datetime

import setuptools


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "craft_text_detector", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        version = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)
        build_date = datetime.now().strftime("%Y%m%d")
        return f"{version}+criteo.{build_date}"


setuptools.setup(
    name="craft-text-detector",
    version=get_version(),
    author="Fatih Cagatay Akyon",
    license="MIT",
    description="Fast and accurate text detection library built on CRAFT implementation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/fcakyon/craft_text_detector",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=get_requirements(),
    python_requires=">=3.9,<3.10",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    keywords="machine-learning, deep-learning, ml, pytorch, text, text-detection, craft",
)
