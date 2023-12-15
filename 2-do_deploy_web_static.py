#!/usr/bin/python3

"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import *
from os import path

""" Define the user, hosts, and key file for Fabric environment """
env.hosts = ["54.237.1.243", "35.175.132.72"]


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers
    """
    """Check if the specified archive_path exists """
    if not path.exists(archive_path):
        return False

    try:
        """ Upload the archive to the /tmp/ directory on the server """
        put(archive_path, "/tmp/")

        """ Extract information about the archive """
        archive = archive_path.split("/")[-1]
        archive_folder = "/data/web_static/releases/" + archive.split(".")[0]

        """ Create the necessary directories on the server """
        run(f"mkdir -p {archive_folder}")

        """ Extract the contents of the archive to the specified folder """
        run(f"tar -xzf /tmp/{archive} -C {archive_folder}")

        """ Remove the uploaded archive from the /tmp/ directory """
        run(f"rm /tmp/{archive}")

        """ Move the contents of the web_static folder to the parent folder """
        run(f"mv {archive_folder}/web_static/* {archive_folder}")

        """ Remove the now empty web_static folder """
        run(f"rm -rf {archive_folder}/web_static")

        """ Remove the current symbolic link to the web_static folder """
        run("rm -rf /data/web_static/current")

        """ Create symbolic link to the new vers of the web_static folder """
        run(f"ln -s {archive_folder} /data/web_static/current")
        run("sudo service nginx restart")
        return True
    except BaseException:
        """ Return False if an except occurs during the deployment process """
        return False

