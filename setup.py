import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iis-loganalyer",
    version="0.0.1",
    author="Supporterino",
    author_email="lars@roth-kl.de",
    description="A small package to analyze iis log files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Supporterino/IISLogAnalyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'storm'
    ],
)