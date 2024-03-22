from setuptools import setup

setup(
    name="public_invest_api",
    version="1.0.1",
    description="Unofficial Public.com Invest API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NelsonDane/public-invest-api",
    author="Nelson Dane",
    packages=["public_invest_api"],
    install_requires=["requests", "python-dotenv"],
)
