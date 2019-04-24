#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 fx-kirin
#

import logging
import unittest
import sys

from add_parent_path import add_parent_path

with add_parent_path(0):
    import stdlogging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s|%(threadName)s|%(filename)s:%(lineno)d|%(levelname)s : %(message)s', level=logging.DEBUG)
    stdlogging.enable()

    sys.stderr.write('test')
    __import__('ipdb').set_trace()

    raise RuntimeError("TestError")
