#!/bin/sh

printenv

BASEDIR=$PWD
echo BASEDIR: $BASEDIR

git clone --depth 1 https://github.com/Itseez/opencv.git
git clone --depth 1 https://github.com/Itseez/opencv_contrib.git

mkdiri -p opencv/build
cd opencv/build
cmake -D CMAKE_INSTALL_PREFIX=$BASEDIR/local -D CMAKE_BUILD_TYPE=RELEASE \
    -D OPENCV_EXTRA_MODULES_PATH=${BASEDIR}/opencv_contrib/modules \
    -D BUILD_opencv_python3=ON -D BUILD_opencv_python2=OFF \
    -D WITH_CUDA=ON -D BUILD_EXAMPLES=OFF .. || exit 1

make -j 4 || exit 1
make install || exit 1

cd ${BASEDIR}
find ${BASEDIR}

