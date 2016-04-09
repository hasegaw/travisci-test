#!/bin/sh

BASEDIR=`pwd`
echo BASEDIR: $BASEDIR

git clone --depth 1 https://github.com/Itseez/opencv.git
git clone --depth 1 https://github.com/Itseez/opencv_contrib.git

cd build
cmake -D CMAKE_INSTALL_PREFIX=$BASEDIR/local -D CMAKE_BUILD_TYPE=RELEASE \
    -D OPENCV_EXTRA_MODULES_PATH=${BASEDIR}/opencv_contrib/modules \
    -D BUILD_opencv_python3=ON -D BUILD_opencv_python2=OFF \
    -D WITH_CUDA=ON -D BUILD_EXAMPLES=OFF ..

make -j 4
make install
