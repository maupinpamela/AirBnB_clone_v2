#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    local("sudo mkdir /versions/")
    dt = datetime.now().strftime("%y%m%d%h%m%s")
    prints = "versions.web_static{}.tgz".format(dt)
    var = local("sudo tar -cvzf {} web_static".format(prints))
    if var.success:
        return dt
    else:
        return None


if __name__ == "__main__":
    do_pack()
