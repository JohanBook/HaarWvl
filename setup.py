import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="haarwvl",
    version="0.0.1",
    author="Björn Annby, Johan Book, Frank Johansson and David Linehan",
    description="Package for compressing images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johanbook/haarwvl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
