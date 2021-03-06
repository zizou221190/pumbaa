#
# @file main.py
#
# @section License
# Copyright (C) 2016, Erik Moqvist
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# This file is part of the Pumbaa project.
#

import array
import binascii
import cmath
import collections
import hashlib
import io
import json
import math
import os
import random
import re
import struct
import sys
import time
import zlib

import gc
import micropython

import simba

import harness
import other
from harness import assert_raises


def test_smoke():
    """Various tests.

    """

    help()

    objs = [
        array,
        binascii,
        cmath,
        collections,
        hashlib,
        io,
        json,
        math,
        os,
        random,
        re,
        struct,
        sys,
        time,
        zlib,
        gc,
        micropython,
        simba,
        simba.Board,
        simba.Event,
        simba.Pin,
        simba.Timer,
        other
    ]

    for obj in objs:
        print()
        help(obj)

    try:
        import foo
    except:
        pass

    print("dir:", dir())

    print("sys.platform:", sys.platform)
    print("os.uname:", os.uname())
    print("time.time:", time.time())

    time.sleep(0.1)
    time.sleep_ms(1)
    time.sleep_us(1)

    try:
        print('CWD:', os.getcwd())
    except OSError as e:
        print(e)

    try:
        os.mkdir('foo')
    except Exception as e:
        print(e)

    with assert_raises(NotImplementedError):
        os.chdir('foo')

    with assert_raises(NotImplementedError):
        os.chdir('..')

    with assert_raises(NotImplementedError):
        os.rename('foo', 'bar')

    with assert_raises(NotImplementedError):
        os.remove('bar')

    with assert_raises(NotImplementedError):
        os.rmdir('bar')

    assert other.foo() == True

    with assert_raises(OSError):
        simba.fs_call("bad")

    print(simba.fs_call("kernel/thrd/list"))

    sio = io.StringIO("foo")
    sio.seek(0, 2)
    print("bar", file=sio)
    sio.seek(0)
    assert sio.read().strip() == "foobar"

    print(cmath.phase(complex(-1.0, 0.0)))
    z = complex(-1.0, 0.0)
    assert z == z.real + z.imag * 1j
    print(cmath.cos(math.pi))

    ordered_dict = collections.OrderedDict([(1,"a")])
    print(ordered_dict.popitem())

    m = hashlib.sha256()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    print(m.digest())

    simba.sys_lock()
    simba.sys_unlock()
      
def main():
    testcases = [
        (test_smoke, "test_smoke")
    ]
    harness.run(testcases)


if __name__ == '__main__':
    main()
