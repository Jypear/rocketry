
from atlas.core.task import Task

import os, sys, subprocess

class Restart(Task):
    "Restart the scheduler"

    def execute_action(self, hard=False, new_window=False, **kwargs):
        python = sys.executable
        if hard:
            os.execl(python, python, *sys.argv)
            # From now on, there is no code to execute
        else:
            if new_window:
                creationflags = subprocess.CREATE_NEW_CONSOLE
            else:
                creationflags = None
            cmd = [python, *sys.argv]
            subprocess.Popen(cmd, shell=False, creationflags=creationflags)
            sys.exit()