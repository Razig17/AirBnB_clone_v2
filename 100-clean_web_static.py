#!/usr/bin/python3
"""Contains the function do_clean that deletes out-of-date archives"""
import os
from fabric.api import *
env.hosts = ['100.25.151.99', '52.3.247.32']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives and so on.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(ar)) for ar in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [ar for ar in archives if "web_static_" in ar]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(ar)) for ar in archives]
