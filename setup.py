import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="log-analyzer",
    version="2.0.0",
    author="Supporterino",
    author_email="lars@roth-kl.de",
    description="A log analyzer for IIS logs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Supporterino/IISLogAnalyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib','sqlalchemy', 'sys', 'os', 'chardet',
      ],
)