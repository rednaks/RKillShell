import psutil, signal

def listAllPIDs():
    pid_list = psutil.get_pid_list()
    named_pid_list = []
    for pid in pid_list:
        process = psutil.Process(pid)
        named_pid_list.append('%d|%s' % (pid, process.name))

    return named_pid_list


def kill(pid):
    process = psutil.Process(pid)
    if process:
        process.kill()
        return process.is_running()
    else:
        return None
