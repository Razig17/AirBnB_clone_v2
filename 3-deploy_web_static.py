#!/usr/bin/python3
"""
This module contains a fabrib file that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    versions = local("tar -cvzf versions/web_static_{}.tgz web_static"
                     .format(datetime.strftime(datetime.now(),
                             "%Y%m%d%H%M%S")))
    if versions.failed:
        return None
    return versions


env.hosts = ['100.25.151.99', '52.3.247.32']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
