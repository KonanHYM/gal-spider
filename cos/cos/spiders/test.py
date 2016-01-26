#!/usr/bin/env python
# encoding: utf-8

if __name__ == "__main__":
    a = 1
    print id(a)
    print a
    b = a
    print id(b)
    b = b + 1
    print id(a)
    print id(b)
