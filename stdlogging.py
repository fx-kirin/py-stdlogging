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

    def __init__(self, logger, default_output, log_level=logging.INFO, only_on_error=True):
        self.logger = logger
        self.log_level = log_level
        self.default_output = default_output
        self.linebuf = ''
        self.only_on_error = only_on_error

    def write(self, buf):
        if buf != '':
            self.linebuf += buf

    def flush(self):
        if self.only_on_error and 'Traceback (most recent call last)' in self.linebuf:
            for buf in self.linebuf.split('\n'):
                if buf != '':
                    self.logger.log(self.log_level, buf.rstrip())
        else:
            self.default_output.write(self.linebuf)
            self.default_output.flush()
        self.linebuf = ''


def enable(stdout=False, stderror=True, stdout_loglevel=logging.INFO, stderr_loglevel=logging.ERROR):
    if stdout:
        stdout_logger = logging.getLogger('STDOUT')
        sl = StreamToLogger(stdout_logger, sys.stdout, stdout_loglevel)
        sys.stdout = sl

    if stderror:
        stderr_logger = logging.getLogger('STDERR')
        sl = StreamToLogger(stderr_logger, sys.stderr, stderr_loglevel)
        sys.stderr = sl
