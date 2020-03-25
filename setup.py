from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="preciphysics",
    version="0.0.1",
    author="Berkay DONMEZ",
    author_email="donmezberkay@outlook.com",
    description="Numerical calculations in Meteorology",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/donmezberkay/preciphysics",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT License",
    ],
)
