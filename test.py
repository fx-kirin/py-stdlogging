#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 fx-kirin
#

import unittest
import stdlogging
import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s|%(threadName)s|%(filename)s:%(lineno)d|%(levelname)s : %(message)s', level=logging.DEBUG)
    stdlogging.enable()
    raise RuntimeError("TestError")
