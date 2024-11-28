#!/home/komodo/miniconda3/envs/py311/bin/python3
#-*- coding: utf-8 -*-
import asyncio
import importlib
from typing import Any, Union
import logging
from logging import Logger
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

def getLogger(logPath: str, logerName: str) -> Logger :
    # Logger 설정
    logger = logging.getLogger(logerName)  # 로거 이름 지정
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

def read_file(filePath: str, logger: Logger, lazy_load: bool =False):
    with open(file=filePath) as file_to_read:
        for line in file_to_read.readlines():
            yield line