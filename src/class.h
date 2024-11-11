
#ifndef _CLASS_H_
#define _CLASS_H_

#include <iostream>


class _DummyClass {

    public:

        void sayHelloFromHeader(int b){
            int a = 1;
            std::cout << "Hello from class.h" << std::endl;
            std::cout << "a = " << a << ", b = " << b << std::endl;
        };

        void sayHelloFromCode(int b);

};


extern "C" {
    _DummyClass* DummyClass(){ return new _DummyClass(); }
    void sayHelloFromCode(_DummyClass* foo, int b){ foo->sayHelloFromCode(b); }
    void sayHelloFromHeader(_DummyClass* foo, int b){ foo->sayHelloFromHeader(b); }
}

#endif