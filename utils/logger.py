import sys

BUFFER_SIZE = 4096
log_buffer = []

def flush_buffer():
    global log_buffer
    log_file = "/var/log/cybertester/cybertest.log"
    with open(log_file, "a") as f:
        f.write(''.join(log_buffer))
    log_buffer = []

def append_to_logs(arg, error=False, console=False):
    global log_buffer
    if console:
        if error:
            print(arg, file=sys.stderr)
        else:
            print(arg)

    log_buffer.append(arg + '\n')
    if sum(len(x) for x in log_buffer) >= BUFFER_SIZE:
        flush_buffer()

import atexit
atexit.register(flush_buffer)
