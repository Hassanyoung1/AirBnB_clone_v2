#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import env, put, run
from os import path
import re

env.hosts = ['35.175.132.72', '54.237.1.243']

def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    archive  = path.basename(archive_path)
    rm_ext = archive_filename.split(".")[0]
    uncompress_path = f"/data/web_static/releases/{rm_ext}"

    run(f"mkdir -p {uncompress_path}")
    run(f"tar -xzf /tmp/{archive} -C {uncompress_path}")
    run(f"rm /tmp/{archive}")
    run("rm -rf /data/web_static/current")
    run(f"ln -s {uncompress_path} /data/web_static/current")

    return True
