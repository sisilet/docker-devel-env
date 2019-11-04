#!/usr/bin/env python3

import subprocess
import sys
import os

base_image = 'ubuntu-18.04-cuda-10.1-cmake-3.15'

images_yml = f"""
---
images:
 - ['{base_image}', 'clang-9-bin']
 - ['{base_image}', 'clang-9-bin', 'conan-1.19']
 - ['{base_image}', 'clang-9-bin', 'conan-1.19', 'ninja']
 - ['{base_image}', 'clang-9-bin', 'conan-1.19', 'ninja', 'misc']
 - ['{base_image}', 'clang-9-bin', 'conan-1.19', 'ninja', 'misc', 'nsight']
 """

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

p = subprocess.Popen(f'docker pull braintwister/{base_image}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while p.poll() is None:
    line = p.stdout.readline().decode('ascii', 'backslashreplace')
    print(line, end='')

with open('images.yml', 'w') as f:
    f.write(images_yml)

