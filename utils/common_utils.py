#!/home/komodo/miniconda3/envs/py311/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
import asyncio
import importlib
from typing import Any, Union
import logging
from logging import Logger
from time import time

def getTimer(func):
    """_summary_
        Decorator로 사용하기 위한 시간 측정 함수
    Args:
        func (_type_): 함수정보
    """
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs) # 함수 실행
        end_time = time()
        elapsed_time = end_time - start_time
        if 'logger' in kwargs.keys():
            logger = checkLogger(logger=kwargs['logger'])
        else:
            logger = checkLogger()
        logger.info(f'함수 {func.__name__} 소요시간은 {elapsed_time:.2f} S 입니다.')
        return result
    return wrapper

async def async_subprocess(cmd: str):
    """_summary_
        Async 모드로 여러 프로세스를 실행할때 사용하는 함수
    Args:
        cmd (str): _description_

    Returns:
        _type_: _description_
    """
    proc = await asyncio.create_subprocess_shell(cmd=cmd, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip()

async def async_subprocess_limit_process(cmd: str, max_process: asyncio.Semaphore = asyncio.Semaphore(value=300)):
    """_summary_
        동시 수행 하는 프로세스 수를 제한고 싶을때 사용하는 함수
    Args:
        cmd (str): _description_
        max_process (asyncio.Semaphore, optional): _description_. Defaults to asyncio.Semaphore(value=300).

    Returns:
        _type_: _description_
    """
    print(f' report : {cmd}')
    async with max_process:
        stdout, stderr = await async_subprocess(cmd=cmd)
    
    return (stdout, stderr)
    

def load_module_func(modulePath: str):
    importPath = modulePath.replace('/','.')
    importPath = importPath.replace('.py','')
    module = importlib.import_module(name=importPath)
    return module

def load_class_func(modulePath, className: str):
    if type(modulePath) == str:
        module = load_module_func(modulePath=modulePath)
    loaded_class = getattr(module, className)
    return loaded_class

def getLogger(logPath: str =os.getcwd(), loggerName: str = 'main') -> Logger :
    """_summary_
        Logger 생성하여 반환하는 함수 설정
    Args:
        logPath (str): _description_
        loggerName (str): _description_

    Returns:
        Logger: _description_
    """
    # Logger 설정
    logger = logging.getLogger(loggerName)  # 로거 이름 지정
    logger.setLevel(logging.DEBUG)           # 로거 레벨 설정 (INFO, WARNING 포함)

    # 로그 포맷 설정
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s "
        "[File: %(pathname)s, Line: %(lineno)d]",  # 파일 경로와 라인 번호 포함
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 콘솔 핸들러 생성
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 파일 핸들러 생성
    if os.path.isfile(logPath):
        pass
    elif os.path.isdir(logPath):
        logPath = os.path.join(logPath, loggerName)
    file_handler = logging.FileHandler(logPath)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info(f'Logger Setting Complete - {logPath=}')
    return logger


def checkLogger(logger: Logger | None, loggerName: str = 'main'):
    """_summary_
        혹시나 Logger가 없으면 만들어서 반환해주는 함수.
    Args:
        logger (Logger | None): _description_

    Returns:
        _type_: _description_
    """
    if type(logger) is Logger:
        pass
    else:
        logger = getLogger()
    return logger

def read_file(filePath: str, logger: Logger | None = None):
    logger = checkLogger(logger=logger)   
      

@getTimer
def read_file_lazymode(filePath: str, logger: Logger | None = None):
    
    func_name = read_file_lazymode.__name__
    logger.info(f'{func_name} 실행 : {filePath=}')
    with open(file=filePath) as file_to_read:
        for line in file_to_read.readlines():
            yield line