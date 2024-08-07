#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

from fabric.operations import run, put
from fabric.api import env
from os.path import exists
from fabric.operations import local
from datetime import datetime


env.hosts = ["100.24.238.120", "3.85.16.187"]
env.key_filename = '~/.ssh/id_rsa'
env.user = 'ubuntu'


def do_pack():
    """
    Function to create a .tgz archive of the web_static directory
    """
    try:
        local("mkdir -p versions")

        tmestmp_str = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_" + tmestmp_str + ".tgz"

        local(f"tar -cvzf versions/{file_name} web_static")

        return (f"versions/{file_name}")

    except Exception as e:
        return


def do_deploy(archive_path):
    """
    Task/function to upload an archive, extract and deploy new version
    of web_static
    """
    try:
        if not exists(archive_path):
            return False

        put(archive_path, "/tmp/")

        archive_name = archive_path.split("/")[-1]
        rm_extension = archive_name.split(".")[0]

        remote_archive_path = "/tmp/" + archive_name

        run(f"mkdir -p /data/web_static/releases/{rm_extension}")

        run(f"tar -xzf {remote_archive_path} -C \
            /data/web_static/releases/{rm_extension}")

        run(f"mv /data/web_static/releases/{rm_extension}/web_static/* \
                /data/web_static/releases/{rm_extension}/")

        run(f"rm -rf /data/web_static/releases/{rm_extension}/web_static")

        run(f"rm -rf {remote_archive_path}")

        run("rm -rf /data/web_static/current")

        run(f"ln -s /data/web_static/releases/{rm_extension} \
           /data/web_static/current")

        return True

    except Exception as e:
        return False
