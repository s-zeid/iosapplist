#!/usr/bin/env python2

# This file is public domain via CC0:
# <https://creativecommons.org/publicdomain/zero/1.0/>

from setuptools import setup, find_packages

setup(
 name="iosapplist",
 version="3.0.dev30",
 description="Lists installed iOS App Store apps.",
 url="https://code.s.zeid.me/iosapplist",
 author="Scott Zeid",
 author_email="support+appbackup@s.zeid.me",
 license="X11 License:  https://tldrlegal.com/license/x11-license",
 classifiers=[
  "Development Status :: 3 - Alpha",
  "Environment :: Console",
  "Intended Audience :: Developers",
  "Intended Audience :: System Administrators",
  "Natural Language :: English",
  "Operating System :: iOS",
  "Operating System :: MacOS :: MacOS X",
  "Operating System :: POSIX",
  "Operating System :: POSIX :: Linux",
  "Programming Language :: Python :: 2",
  "Programming Language :: Python :: 2.5",
  "Programming Language :: Python :: 2 :: Only",
  "Topic :: Software Development :: Libraries",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Topic :: System :: Systems Administration",
  "Topic :: Utilities",
 ],
 packages=find_packages(),
 install_requires=["argparse", "CFPropertyList", "simplejson"],
 entry_points={
  "console_scripts": [
    "iosapplist=iosapplist:main"
  ]
 },
)
