#!/bin/bash
base_account='braintwister'
base='ubuntu-18.04-cuda-10.1-cmake-3.15'

modules=(
    clang-9-bin
    conan-1.19
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

base_name=${base_account}/${base}
docker pull $base_name

curr_image=$base
curr_account=$base_account

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

