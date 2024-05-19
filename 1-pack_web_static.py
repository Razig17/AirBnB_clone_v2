#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder using the function do_pack
"""


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
