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


def _validate_param(d, param_name):
    if d is None:
        raise ValueError(f"Expected '{param_name} param not found")

class StreamToLogger:
    """
    This is adapter class from any stream-like object to logging.Logger.
    """

    def __init__(self, **kwargs):
        """
        It is recommended to use package-level initStream() function and not this method directly.

        :param logger: Required. Standard Python's Logger or any Logger-like object.
        :param stream: Required. sys.stderr, sys.stdout or any other stream-like object.
        :param log_level: Optional. If not supplied, logging.DEBUG will be used.
        """

        _validate_param(kwargs, 'logger')
        _validate_param(kwargs, 'log_level')
        _validate_param(kwargs, 'stream')

        self.logger = kwargs.pop('logger')
        self.log_level = kwargs.pop('log_level', logging.DEBUG)
        self.stream = kwargs.pop('stream')

    def write(self, lines):
        if lines:
            lines = lines+'\n'
            for line in lines.split('\n'):
                if line:
                    self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        self.stream.flush()



def initStream(logger=None, logger_level=logging.ERROR, stream_getter=None, stream_setter=None):
    """
    Preffered API.
    stream_getter() is supplier/factory method that returns stream-like object (i.e. sys.stderr) that we're adapting upon.
                   It's intended usage is to supply stream-like object that we want to apapt upon.
    stream_setter() is consumer method that receives wrapped object as parameter.
                   It's intended usage is to overwrite source stream-like, i.e. sys.stderr = s.

    :param logger: Optional. If not supplied logging.getLogger('stderr') will be used.
    :param logger_level: Optional. If not supplied logging.ERROR will be used.
    :param stream_getter: Optional. if not supplied method that returns sys.stderr will be used.
    :param stream_setter: Optional. if not supplied method that get's strema-like object and set's sys.stderr will be used.
    :return:
    """
    if logger is None:
        logger = logging.getLogger('stderr')

    if stream_getter is None:
        def stream_getter():
            return sys.stderr

    if stream_setter is None:
        def stream_setter(s):
            sys.stderr = s

    stream = stream_getter()
    sl = StreamToLogger(logger=logger, stream=stream, logger_level=logger_level)
    stream_setter(sl)
