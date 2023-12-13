#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
import os
from fabric.api import env, put, run

""" Define the list of web servers """
env.hosts = ['35.175.132.72', '54.237.1.243']

""" Fabric function to deploy an archive to the web servers """


def do_deploy(archive_path):
    """
    Deploy the specified archive to the web servers.

    :param archive_path: The path to the archive file.
    :return: True if deployment succeeds, False otherwise.
    """

    """ Check if the specified archive file exists """
    if not os.path.exists(archive_path):
        return False

    """ Upload the archive to the /tmp/ directory on the web servers """
    put(archive_path, "/tmp/")
    archive = os.path.basename(archive_path)

    """ Extract the base filename without extension """
    rm_ext = archive.split(".")[0]

    """ Define the path to the target directory for extraction """
    uncompress_path = f"/data/web_static/releases/{rm_ext}"

    """ Create the target directory """
    run(f"mkdir -p {uncompress_path}")

    """ Extract the archive to the target directory """
    run(f"tar -xzf /tmp/{archive} -C {uncompress_path}")

    """ Remove the uploaded archive from the /tmp/ directory """
    run(f"rm /tmp/{archive}")

    """ Remove the existing symbolic link to the current release """
    run("rm -rf /data/web_static/current")

    """ Create a new symbolic link to the deployed release """
    run(f"ln -s {uncompress_path} /data/web_static/current")

    """ Deployment successful """
    return True
