from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the specified file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip whitespace and newlines from each requirement
        requirements = [req.strip() for req in requirements]

        # Remove the editable install if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Setup function to define package metadata and dependencies
setup(
    name="Movie_Recommender_System_Content_Based_Filtering",  # Updated project name
    version="1.0.0",
    packages=find_packages(),
    # Package metadata
    author="Suresh Beekhani",
    author_email="sureshbeekhani26@gmail.com",
    description="A tool for recommending movies based on content-based filtering techniques.",
    long_description="This package provides a comprehensive model for recommending movies using content-based filtering and data analysis techniques.",
    long_description_content_type="text/markdown",
    url="https://github.com/SURESHBEEKHANI/Movie-Recommender-System-Content-Based-Filtering.git",  # Updated URL to match your project
    # Read dependencies from requirements.txt
    install_requires=get_requirements('requirements.txt'),
    # License and classification
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
