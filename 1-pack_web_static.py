#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.operations import local
from datetime import datetime


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
