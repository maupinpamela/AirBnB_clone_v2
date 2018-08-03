#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy """

from fabric.api import run, put, env
import os


env.user = 'ubuntu'
env.hosts = ['35.196.197.251', '35.227.29.140']


def do_deploy(archive_path):
    if archive_path is None:
        return False
    new_file = archive_path[9:]
    new_path = "/data/web_static/releases/{}".\
               format(new_file)[0:-4]
    put(archive_path, "/tmp/")
    run("mkdir -p {}/".format(new_path))
    run("tar -xzf /tmp/{} -C {}/".format(new_file, new_path))
    run("rm /tmp/{}".format(new_file))
    run("mv {}/web_static/* {}/".format(new_path, new_path))
    run("rm -rf {}/web_static".format(new_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(new_path))
    print ("New version deployed!")
    return True
