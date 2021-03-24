FROM ubuntu:20.04

# Setup timezone data
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Refresh package list
RUN apt-get update -y  --fix-missing
RUN apt-get upgrade -y

RUN apt-get install -y zip git
RUN apt-get install -y build-essential cmake python3-dev python3-sip-dev protobuf-compiler libprotoc-dev libprotobuf-dev python3-pip autoconf libtool libtool-bin

# push App and Pip stuff
COPY ./app /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install --upgrade pip
RUN pip install -r ./requirement.txt

# Download all the zip and unzip
RUN mkdir -p '/curaengine/4.8.0'
COPY ./download.py /download.py
RUN python3 /download.py

# install protobuf
WORKDIR "/curaengine/4.8.0/protobuf-3.15.6"
RUN ./autogen.sh && ./configure && make && make install

# install libArcus
RUN ldconfig
RUN mkdir "/curaengine/4.8.0/libArcus-4.8.0/build"
WORKDIR "/curaengine/4.8.0/libArcus-4.8.0/build"
RUN cmake .. && make && make install

# install curaengine
RUN mkdir "/curaengine/4.8.0/CuraEngine-4.8.0/build"
WORKDIR "/curaengine/4.8.0/CuraEngine-4.8.0/build"
RUN cmake .. && make

# App
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
