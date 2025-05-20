from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
    
#     return requirements

# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = [req.strip() for req in file_obj.readlines()]
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return [req for req in requirements if req]  # Remove empty strings


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements,
    excluding any editable install lines like '-e .'
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and not req.startswith('-e'):
                requirements.append(req)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='kusumm',
    author_email='kusumm.mhz@gmail.com',
    description='A simple ML project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)