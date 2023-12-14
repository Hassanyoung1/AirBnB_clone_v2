#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy """

from fabric.api import *
from os import path

env.user = "ubuntu"
env.hosts = ["54.237.1.243", "35.175.132.72"]
env.key_filename = "/root/.ssh/school"


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
"""
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    target_tgz_file = f"versions/web_static_{timestamp}.tgz"

    result = local(f"tar -cvzf {target_tgz_file} web_static")

    if result.ok:
        return target_tgz_file
    else:
        return None


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split("/")[-1]
        archive_folder = "/data/web_static/releases/" + file.split(".")[0]
        run(f"mkdir -p {archive_folder}")
        run(f"tar -xzf /tmp/{archive} -C {archive_folder}")
        run(f"rm /tmp/{archive}")
        run(f"mv {archive_folder}/web_static/* {archive_folder}")
        run(f"rm -rf {archive_folder}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {archive_folder} /data/web_static/current")
        return True
    except BaseException:
        return False
