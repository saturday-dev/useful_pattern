#!/home/komodo/miniconda3/envs/py311/bin/python3
import os
import sys
import argparse

pjtPath = os.path.dirname(os.path.dirname(__file__))
if pjtPath not in sys.path:
    sys.path.append(pjtPath)

from utils import common_utils as cu

class _9999_firstChecker:
    def __init__(self) -> None:
        self.__name__ = '_9999_firstChecker'
    
    



if __name__ == '__main__':
    module = _9999_firstChecker()
    
    print(f'{module.__name__}')
    

