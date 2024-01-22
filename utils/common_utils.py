
import asyncio

async def async_subprocess(cmd: str):
    proc = await asyncio.create_subprocess_shell(cmd=cmd, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip()

async def async_do_task_and_report(cmd: str):
    stdout, stderr = await async_subprocess(cmd=cmd)
    print(f' report : {cmd}')
    return (stdout, stderr)
    



if __name__ == '__main__':
    cmd_list = ['ll','conda env list', 'conda list']
    task_list = []
    for cmd in cmd_list:
        task_list.append(async_do_task_and_report(cmd=cmd))
    loop = asyncio.get_event_loop()
    commands = asyncio.gather(*task_list)
    result = loop.run_until_complete(commands)
    print(result)
    loop.close()