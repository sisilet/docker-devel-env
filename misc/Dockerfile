ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="sisilet"

RUN echo "deb http://ubuntu.mirror.digitalpacific.com.au/archive/ bionic main universe" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y graphviz libcanberra-gtk-module sudo \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -I mysql-connector
#RUN pip3 install -I pandas numpy matplotlib
