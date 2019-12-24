ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="sisilet"

RUN bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"

ENV CC clang
ENV CXX clang++