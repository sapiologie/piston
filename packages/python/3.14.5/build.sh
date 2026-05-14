#!/bin/bash

PREFIX=$(realpath $(dirname $0))

mkdir -p build

cd build

curl "https://www.python.org/ftp/python/3.14.5/Python-3.14.5.tgz" -o python.tar.gz
tar xzf python.tar.gz --strip-components=1
rm python.tar.gz

./configure --prefix "$PREFIX" --with-ensurepip=install
make -j$(nproc)
make install -j$(nproc)

cd ..

rm -rf build

bin/pip3 install --no-cache-dir \
    numpy==2.4.4 \
    scipy==1.17.1 \
    pandas==3.0.3 \
    matplotlib==3.10.9 \
    openpyxl==3.1.5 \
    Pillow==12.2.0
