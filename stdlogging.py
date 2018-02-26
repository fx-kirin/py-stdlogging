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
        if buf != '':
            if "\n" in buf:
                self.linebuf += buf
                self.logger.log(self.log_level, self.linebuf.rstrip())
                self.linebuf = ''
            else:
                self.linebuf += buf

def enable(stdout=False, stderror=True, stdout_loglevel=logging.INFO, stderr_loglevel=logging.ERROR):
    if stdout:
        stdout_logger = logging.getLogger('STDOUT')
        sl = StreamToLogger(stdout_logger, stdout_loglevel)
        sys.stdout = sl

    if stderror:
        stderr_logger = logging.getLogger('STDERR')
        sl = StreamToLogger(stderr_logger, stderr_loglevel)
        sys.stderr = sl
