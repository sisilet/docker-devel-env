#!/bin/bash

docker run --rm -it \
	-e DISPLAY \
	-e USER_ID=1000 \
	-e GROUP_ID=1000 \
	-e USER_NAME=eric \
	-e GROUP_NAME=eric \
	-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
	-v ~/projects:/opt/projects \
	-v home:/home/eric \
	--privileged \
        eric3322/ubuntu-18.04-cuda-10.1-tensorflow-gpu-1.14-jupyter-1.0-cmake-3.15-clang-9-bin-conan-1.20-misc \
	bash
