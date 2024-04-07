#!/home/komodo/miniconda3/envs/py311/bin/python3
#-*- coding: utf-8 -*-
import asyncio
import importlib
from typing import Any
async def async_subprocess(cmd: str):
    proc = await asyncio.create_subprocess_shell(cmd=cmd, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip()

async def async_do_task_and_report(cmd: str):
    stdout, stderr = await async_subprocess(cmd=cmd)
    print(f' report : {cmd}')
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