from setuptools import find_packages, setup

setup(
    name = "AIMO",
    version = "0.1.0",
    author = "Mou YongLi, Stefan Decker",
    author_email = "mou@dbis.rwth-aachen.de",
    description = ("Kaggle AI Mathematical Olympiad (AIMO) Prize"),
    license = "MIT",
    url = "https://github.com/MouYongli/AIMO.git",
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Kaggle AI Mathematical Olympiad (AIMO) Prize",
        "License :: OSI Approved :: MIT License",
    ],
)