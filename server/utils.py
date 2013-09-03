import psutil, signal, time

def listAllPIDs():
    pid_list = psutil.get_pid_list()
    named_pid_list = []
    for pid in pid_list:
        process = psutil.Process(pid)
        named_pid_list.append('%d|%s' % (pid, process.name))

    return ','.join(named_pid_list)


def kill(pid):
    process = psutil.Process(pid)
    if process:
        process.kill()
        time.sleep(0.50)
        if(not process.is_running()) : return 'Process %d killed' %pid
        else: return 'Process %d still alive' % pid
    else:
        return None
