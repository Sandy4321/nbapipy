from distutils.core import setup

setup(
    name="nbapipy",
    version="0.1.0",
    author="Raul Gil",
    author_email="gilraul90@gmail.com",
    packages=["src", "helpers"],
    include_package_data=True,
    # license="LICENSE.txt",
    description="API wrapper around the erikberg mlb/nba web service",
    install_requires=["requests", ]

)