from setuptools import setup, find_packages

setup(
    name="cloud-infrastructure-auditor",
    version="1.0.0",
    description="A Python CLI tool for auditing cloud infrastructure and identifying cost optimization opportunities.",
    author="Karthika R",
    py_modules=["main"],
    install_requires=[
        "typer>=0.27.0",
        "boto3>=1.43.0",
        "rich>=15.0.0",
    ],
)