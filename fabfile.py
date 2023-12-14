#!/usr/bin/python3

from invoke import task, run as local
from fabric import Connection
from os import path
from datetime import datetime

@task
def do_pack(c):
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    target_tgz_file = "versions/web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf {} web_static".format(target_tgz_file))

    if result.ok:
        return target_tgz_file
    else:
        return None

def get_connections():
    hosts = ["54.237.1.243", "35.175.132.72"]
    user = "ubuntu"
    passphrase = "betty"

    connections = [Connection(host=host, user=user, connect_kwargs={"passphrase": passphrase}) for host in hosts]
    return connections

@task
def do_deploy(c, archive_path):
    connections = get_connections()

    if not path.exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return False

    for connection in connections:
        try:
            connection.put(archive_path, "/tmp/")
            archive = archive_path.split("/")[-1]
            archive_folder = "/data/web_static/releases/" + archive.split(".")[0]
            connection.run(f"mkdir -p {archive_folder}")
            connection.run(f"tar -xzf /tmp/{archive} -C {archive_folder}")
            connection.run(f"rm /tmp/{archive}")
            connection.run(f"mv {archive_folder}/web_static/* {archive_folder}")
            connection.run(f"rm -rf {archive_folder}/web_static")
            connection.run("rm -rf /data/web_static/current")
            connection.run(f"ln -s {archive_folder} /data/web_static/current")
            print(f"Deployment successful on {connection.host}.")
        except Exception as e:
            print(f"Deployment failed on {connection.host}: {e}")

        return True  # You can modify this based on your needs
