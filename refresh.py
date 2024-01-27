# Feel free to use

from os import path, remove

if path.exists('logs.txt'):
    with open('logs.txt', 'r+') as logfile:
        logfile.truncate(0)
