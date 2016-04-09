#!/bin/sh

printenv

BASEDIR=$PWD
echo BASEDIR: $BASEDIR

git clone --depth 1 https://github.com/Itseez/opencv.git
# git clone --depth 1 https://github.com/Itseez/opencv_contrib.git

mkdir -p opencv/build
cd opencv/build

git checkout 3.1.0
cmake -D CMAKE_INSTALL_PREFIX=$BASEDIR/local -D CMAKE_BUILD_TYPE=RELEASE \
    -D BUILD_opencv_python3=ON -D BUILD_opencv_python2=OFF \
    -D WITH_CUDA=ON -D BUILD_EXAMPLES=OFF .. || exit 1
#    -D OPENCV_EXTRA_MODULES_PATH=${BASEDIR}/opencv_contrib/modules \

make -j 4 || exit 1
make install || exit 1

cd ${BASEDIR}
find ${BASEDIR}

