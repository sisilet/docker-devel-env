FROM ubuntu:18.04

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG TIMEZONE='Europe/Berlin'
ARG DEBIAN_FRONTEND=noninteractive

RUN echo $TIMEZONE > /etc/timezone && \
  apt-get update && apt-get install -y tzdata && \
  rm /etc/localtime && \
  ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
  dpkg-reconfigure -f noninteractive tzdata && \
  apt-get clean

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    git \
    git-svn \
    gpg-agent \
    make \
    ninja-build \
    software-properties-common \
    vim \
    wget \
    ssh \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set aliases
COPY aliases /tmp/
RUN cat /tmp/aliases >> /etc/bash.bashrc && rm -f /tmp/aliases

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
