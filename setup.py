#!/usr/bin/env python3

import subprocess
import sys
import os

base_image = 'ubuntu-18.04-cuda-10.1-cmake-3.15'
extra_packages = ['clang-9-bin', 'conan-1.19', 'misc', 'vscode-1.39']

images_block = ""
image = f"'{base_image}'"
for ep in extra_packages:
    image += f", '{ep}'"
    images_block += f" - [{image}]\n"

images_yml = f"""
---
images:
{images_block}
"""

full_image = '-'.join([f"{i}" for i in ([base_image] + extra_packages)])

docker_compose_yml = f"""
version: '3'
 
services:
    bash:
        image: eric3322/{full_image}
        volumes:
            - ~/projects:/opt/projects
            - home:/home/ubuntu
            - /tmp/.X11-unix:/tmp/.X11-unix:ro
        environment:
            - USER_ID=1000
            - GROUP_ID=1000
            - USER_NAME=ubuntu
            - GROUP_NAME=ubuntu
            - DISPLAY
        privileged: true
        stdin_open: true
        tty: true
 
volumes:
    home:
"""

with open('docker-compose.yml', 'w') as f:
    f.write(docker_compose_yml)

submodule_folder = 'docker-devel-env'
for i in [o for o in os.listdir(submodule_folder) if os.path.isdir(os.path.join(submodule_folder,o))]:
    
    p = subprocess.Popen(f'ln -s {submodule_folder}/{i} {i}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().decode('ascii', 'backslashreplace')
        print(line, end='')

    p = subprocess.Popen(f'echo {i} >> .gitignore', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().decode('ascii', 'backslashreplace')
        print(line, end='')

with open('images.yml', 'w') as f:
    f.write(images_yml)

