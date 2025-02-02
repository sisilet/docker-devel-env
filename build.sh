#!/bin/bash
base_account='braintwister'
base='ubuntu-18.04-cuda-10.1-tensorflow-gpu-1.14-jupyter-1.0'

modules=(
    cmake-3.15
    clang-9-bin
    conan-1.20
    misc
#    vscode-1.39
)

interactive=

while [ "$1" != "" ]; do
    case $1 in
        -u | --user )       shift
                            user=$1
                            ;;
        -p | --password )   shift
                            password=$1
                            ;;
        -a | --account )    shift
                            image_account=$1
                            

    esac
    shift
done

if [ "$base" == "" ]; then
    docker pull ubuntu:18.04
    cd ubuntu-18.04-extra
    curr_image=ubuntu-18.04-extra
    docker build -t ${image_account}/ubuntu-18.04-extra --build-arg BASE_IMAGE=ubuntu:18.04 .
    if [[ ! -z "$user" && ! -z "$password" ]]; then
        docker push ${image_account}/ubuntu-18.04-extra
    fi
    curr_account=${image_account}
    cd ..
else
    base_name=${base_account}/${base}
    docker pull $base_name
    curr_image=$base
    curr_account=$base_account
fi


if [[ ! -z "$user" && ! -z "$password" ]]; then
    echo $password | docker login -u $user --password-stdin
fi

for m in ${modules[@]}; do
    cd ${m}
    base_image=${curr_image}
    curr_image=${curr_image}-${m}
    echo build image: ${image_account}/${curr_image} with base: ${curr_account}/${base_image}
    docker build -t ${image_account}/${curr_image} --build-arg BASE_IMAGE=${curr_account}/${base_image} .
    if [[ ! -z "$user" && ! -z "$password" ]]; then
        docker push ${image_account}/${curr_image}
    fi
    curr_account=${image_account}
    cd ..
done

