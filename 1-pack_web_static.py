#!/usr/bin/python3

"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""

from fabric import run as local, task
import os
from datetime import datetime

@task
def do_pack():
    # Check if the 'versions' directory exists; create it if not
    if not os.path.exists("versions"):
        local("mkdir versions")

    # Generate a timestamp for the tarball filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    target_tgz_file = "versions/web_static_{}.tgz".format(timestamp)

    # Create a compressed tarball of the 'web_static' folder
    result = local("tar -cvzf {} web_static".format(target_tgz_file))

    # Check if the tarball creation was successful
    if result.ok:
        return target_tgz_file
    else:
        return None
