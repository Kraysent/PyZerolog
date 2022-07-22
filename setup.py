from setuptools import setup

setup(
    name="pyzerolog",
    version="0.0.2",
    author="Kraysent",
    description="Package that makes typed logging convinient.",
    license="MIT License",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=["zlog"],
)
