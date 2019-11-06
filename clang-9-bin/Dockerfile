ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="sisilet"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-9 main" >> /etc/apt/sources.list \
 && echo "deb-src http://apt.llvm.org/bionic/ llvm-toolchain-bionic-9 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        xz-utils \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -SL http://releases.llvm.org/9.0.0/clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz \
        | tar -xJC . \
    && cp -R clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04/* /usr \
    && ls /usr/bin/clang \
    && rm -rf clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04 \
#    && echo 'export PATH=/clang_9.0.0/bin:$PATH' >> /etc/bash.bashrc \
#    && echo 'export LD_LIBRARY_PATH=/clang_9.0.0/lib:$LD_LIBRARY_PATH' >> /etc/bash.bashrc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV CC clang
ENV CXX clang++