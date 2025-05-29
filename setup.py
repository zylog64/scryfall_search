from setuptools import find_packages, setup

setup(
    name="scryfall",
    version="0.1.0",
    url="",
    author="Micky Aarnoudse",
    description="Search scryfall for cardmarket whislists",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["scrython"],
    entry_points={"console_scripts": ["scryfall=scryfall.main:main"]},
    license='GPLv3+',
)
