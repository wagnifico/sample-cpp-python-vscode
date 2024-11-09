
cd ./src

## build without cmake
# g++ -c -fPIC class.cpp -o build/class.o
# g++ -shared -Wl,-soname,libclass.so -o build/libclass.so build/class.o

## build with cmake
rm -rf build
mkdir build

cd build
cmake ..
make VERBOSE=1