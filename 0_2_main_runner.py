#!/home/komodo/miniconda3/envs/py311/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
import argparse

pjtPath = os.path.dirname(__file__)
sys.path.append(pjtPath)
from utils import common_utils as cu

class _9999_firstChecker:
    def __init__(self) -> None:
        self.__name__ = '_9999_firstChecker'
    
    def run_checker(self):
        modulePath = '_9999_firstChecker/_9999_firstChecker.py'
        className = modulePath.split('/')[0]
        cur_module = cu.load_module_func(modulePath=modulePath)
        cur_class = cu.load_class_func(modulePath=modulePath, className=className)
        print()

if __name__ == '__main__':
    module = _9999_firstChecker()
    
    print(f'{module.__name__}')
    module.run_checker()