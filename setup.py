"""The setup."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()    # pylint: disable=C0103

setuptools.setup(
    name="string_calculator",
    version="0.0.1",
    author="Suradet Jitprapaikulsarn",
    author_email="suradet.j@gmail.com",
    description="A string calculator kata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suradet/string-calculator-kata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licnse :: OSI Approved :: BSD License",
        "Operating Sytem :: OS Independent",
    ],
)
