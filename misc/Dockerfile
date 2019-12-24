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

RUN /entrypoint.d/conan_add_repositories.sh
RUN conan profile new default --detect
RUN conan profile update settings.compiler.libcxx=libstdc++11 default
RUN conan install gtest/1.8.1@bincrafters/stable --build missing
RUN conan install boost_atomic/1.69.0@bincrafters/stable --build missing
RUN conan install boost_format/1.69.0@bincrafters/stable --build missing
RUN conan install boost_asio/1.69.0@bincrafters/stable --build missing
RUN conan install boost_system/1.69.0@bincrafters/stable --build missing
RUN conan install boost_property_tree/1.69.0@bincrafters/stable --build missing
RUN conan install boost_program_options/1.69.0@bincrafters/stable --build missing
RUN conan install boost_beast/1.69.0@bincrafters/stable --build missing
RUN conan install boost_stacktrace/1.69.0@bincrafters/stable --build missing
RUN conan install boost_tokenizer/1.69.0@bincrafters/stable --build missing
RUN conan install pcapplusplus/19.04@bincrafters/stable --build missing
RUN conan install pistache/d5608a1@conan/stable --build missing
RUN conan install rapidjson/1.1.0@bincrafters/stable --build missing
RUN conan install spdlog/1.3.1@bincrafters/stable --build missing
RUN conan install libpcap/1.8.1@bincrafters/stable --build missing
RUN conan install mysql-connector-c/6.1.11@bincrafters/stable --build missing