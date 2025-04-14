# Setup.py is a script for packaging Python projects.
# It contains information about the project, such as its name, version, author, and dependencies.

from setuptools import setup, find_packages
from typing import List

# Ignore -e from the requirements.txt file
HYPEN_LINK = "-e ."

# This is a function to get the list of requirements from the requirements.txt file
# It will read the requirements.txt file and return a list of requirements
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = [] # it will read  requirements.txt
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if "-e ." in requirements: # Ignore -e from the requirements.txt file
            requirements.remove("-e .")
    return requirements




# Basic Information about the author, project name, version, and packages
setup(
    name="Students_Score_Project",
    version="0.0.1",
    author="Pratap",
    author_email= "pratap.jadhav0@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")       #["numpy","pandas"]
)