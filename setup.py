##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

import os
import re

from setuptools import find_packages, setup

def _read_properties():
    init_path = os.path.abspath(os.path.join("googlecalendar", "__init__.py"))
    regex = re.compile("^\\s*__(?P<key>.*)__\\s*=\\s*\"(?P<value>.*)\"\\s*$")
    with open(init_path, "rt") as f:
        props = {}
        for line in f.readlines():
            m = regex.match(line)
            if m is not None:
                props[m.group("key")] = m.group("value")

    return props

props = _read_properties()
version = props["version"]
description = props["description"]

setup(
    name="google-calendar",
    version=version,
    description=description,
    setup_requires=["setuptools-markdown"],
    long_description_markdown_filename="README.md",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    url="https://github.com/rcook/google-calendar",
    author="Richard Cook",
    author_email="rcook@rcook.org",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "google-api-python-client",
        "httplib2",
        "pyprelude"
    ],
    entry_points={
        "console_scripts": [
            "google-calendar = googlecalendar.__main__:_main"
        ]
    },
    include_package_data=True,
    test_suite="googlecalendar.tests.suite",
    zip_safe=False)
