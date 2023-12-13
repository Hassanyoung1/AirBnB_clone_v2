#!/usr/bin/python3

from fabric import run as local, task
import os
from datetime import datetime


@task
def do_pack():
    if not os.path.exists("versions"):
        local("mkdir versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    target_tgz_file = "versions/web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf {} web_static".format(target_tgz_file))

    if result.ok:
        return target_tgz_file
    else:
        return None
