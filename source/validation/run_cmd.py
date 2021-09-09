import os
import subprocess
import threading


class RunCmd(threading.Thread):
    # https://stackoverflow.com/questions/4158502/kill-or-terminate-subprocess-when-timeout?noredirect=1
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout
        self.out = b"TIMEOUT"
        self.err = b"TIMEOUT"

    def run(self):
        self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.out, self.err = self.p.communicate()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            os.kill(self.p.pid, 0)
            self.p.kill()  # use self.p.kill() if process needs a kill -9
            self.join()

        return self.out, self.err
