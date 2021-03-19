#!/bin/bash

# Dependency for libarcus
apt install build-essentials cmake python3-dev python3-sip-dev protobuf-compiler libprotoc-dev libprotobuf-dev

# Download libraries and curaengine
python3 download.py

# Install protobuf
cd protobuf-3.15.6 && \
	./autogen.sh && \
	./configure && \
	make && \
	make install && \
	cd ..

# Install libArcus
cd libArcus-4.8.0 && \
	mkdir build && cd build && \
    cmake .. && \
	make && \
	make install && \
	cd ../..

# Install curaengine
cd  CuraEngine-4.8.0 && mkdir build && cd build && \
	cmake .. && \
	make && cd ../..

# Test curaengine
# TODO

# Remove zip files
rm -rf curaengine-4.8.0.zip
rm -rf libArcus-4.8.0.zip
rm -rf protobuf-all-3.15.6.zip
