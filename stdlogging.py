#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""

import logging
import sys

class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.splitlines():
            line = line.rstrip()
            if line != '':
                self.logger.log(self.log_level, line)

def enable(stdout_loglevel=logging.INFO, stderr_loglevel=logging.ERROR):
    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, stdout_loglevel)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, stderr_loglevel)
    sys.stderr = sl
