from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this fuction will return list of requirements 
    '''
    requiremetns=[]
    with open(file_path) as file_obj:
        requiremetns= file_obj.readlines()
        requiremetns = [req.replace("\n","") for req in requiremetns]
        if '-e .' in requiremetns:
            requiremetns.remove('-e .')


setup(
name = 'ML Project',
version = '0.0.1',
author = 'Umesh Shelar',
author_email = 'shelarumesh1006@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirement.txt')
)