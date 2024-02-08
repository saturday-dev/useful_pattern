#!/home/komodo/miniconda3/envs/py311/bin/python3

import sys
import os
import asyncio

pjtPath = os.path.dirname(__file__)
sys.path.append(pjtPath)

from utils import common_utils as cu


if __name__ == '__main__':
    # subprocess로 실행하는 것을 asyncio를 이용하여 결과 기다리는 것을 순차적이 아닌 끝난 순서대로 받을 수 있는 방식
    cmd_list = ['ll','conda env list', 'conda list']
    task_list = []
    for cmd in cmd_list:
        task_list.append(cu.async_do_task_and_report(cmd=cmd))
    loop = asyncio.get_event_loop()
    commands = asyncio.gather(*task_list)
    result = loop.run_until_complete(commands)
    print(result)
    loop.close()