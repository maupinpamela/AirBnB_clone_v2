#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    local("sudo mkdir -p versions")
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    prints = "versions/web_static_{}.tgz".format(dt)
    var = local("sudo tar -cvzf {} web_static".format(prints))
    if var.succeeded:
        return prints
    else:
        return "None"


if __name__ == "__main__":
    do_pack()
