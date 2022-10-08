from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()


setup(
    name="btcpay-python-sdk",
    version="0.1.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    description="BTCPay Python SDK using the Greenfield API",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/enfront/btcpa-python-sdk",
    author="Enfront LLC",
    author_email="support@enfront.io",
    keywords="btcpay, bitcoin, payments, crypto",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial"
    ],
    install_requires=[
        "requests",
        "ecdsa"
    ],
)
