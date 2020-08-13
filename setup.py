import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mvdplots-mvondomaros",
    version="0.1",
    author="Michael von Domaros",
    author_email="mvondomaros@gmail.com",
    description="A package for setting up my plot style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mvondomaros/mvdplots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
