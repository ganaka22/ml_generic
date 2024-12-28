from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        list[str]: _description_

    this function will return list of requirements
    """
    HYPEN_CONST = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

        if HYPEN_CONST in requirements:
            requirements.remove(HYPEN_CONST)

    return requirements


setup(
    name="ml_generic",
    version="0.0.1",
    author="DB22",
    author_email="abc@email.com",
    packages=find_packages(),
    # install_requires = ['numpy','pandas', 'seaborn', 'matplotlib', 'scikit-learn']   OR
    install_requires=get_requirements("requirements.txt"),
)
