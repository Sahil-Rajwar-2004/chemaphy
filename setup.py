from setuptools import setup,find_packages

setup(
    name = "chemaphy",
    version = "2.12.0",
    description = "Package for Scientific calculation",
    long_description = "For more info, check the github repository",
    author = "Sahil Rajwar",
    maintainer = "its_Sahil",
    author_email = "justsahilrajwar2004@gmail.com",
    packages = ["chemaphy"],
    license = "MIT",
    install_requires = ["numpy","trigo","pandas","statistics","matplotlib","sympy"],
    url = "https://github.com/Sahil-Rajwar-2004/chemaphy",
    keywords = ["calculator","scipy","calc","chemaphy"],
    classifiers = [
    "Programming Language :: Python :: 3",
    "Intended Audience :: Education",
    "Operating System :: OS Independent",
    ]
)
