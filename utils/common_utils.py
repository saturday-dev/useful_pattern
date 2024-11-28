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
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs) # 함수 실행
        end_time = time()
        elapsed_time = end_time - start_time
        if 'logger' in kwargs.keys() and type(kwargs['logger']) == Logger:
            logger = kwargs['logger']
            logger.info(f'함수 {func.__name__} 소요시간은 {elapsed_time:.2f} S 입니다.')
        else:
            print(f'함수 {func.__name__} 소요시간은 {elapsed_time:.2f} S 입니다.')                
        return result
    return wrapper

async def async_subprocess(cmd: str):
    proc = await asyncio.create_subprocess_shell(cmd=cmd, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip()

async def async_do_task_and_report(cmd: str, max_process: asyncio.Semaphore = asyncio.Semaphore(value=300)):
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

def getLogger(logPath: str ='./', loggerName: str = 'MyLogger') -> Logger :
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



def read_file(filePath: str, logger: Logger, lazy_load: bool =False):
    with open(file=filePath) as file_to_read:
        for line in file_to_read.readlines():
            yield line