#!/usr/bin/python3

import signal
import sys


def sigusr1_handler(signum,frame):
    sys.stderr.write ("In sigusr1\n")
    sys.exit(0)

signal.signal(signal.SIGUSR1,sigusr1_handler)
while (True):
    pass
