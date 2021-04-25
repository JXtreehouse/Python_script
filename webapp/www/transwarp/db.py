#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/michaelliao/awesome-python-webapp/blob/day-02/www/transwarp/db.py
__author__ = 'AlexZ33'

"""
Database operate module
"""

import time, uuid, functools, threading, logging


# Dict object
class Dict(dict):
    '''
        Simple dict but support access as x.y style.
        >>> d1 = Dict()
        >>> d1['x'] = 100
        >>> d1.x
        100
        >>> d1.y = 200
        >>> d1['y']
        200
        >>> d2 = Dict(a=1, b=2, c='3')
        >>> d2.c
        '3'
        >>> d2['empty']
        Traceback (most recent call last):
            ...
        KeyError: 'empty'
        >>> d2.empty
        Traceback (most recent call last):
            ...
        AttributeError: 'Dict' object has no attribute 'empty'
        >>> d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
        >>> d3.a
        1
        >>> d3.b
        2
        >>> d3.c
        3
        '''

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def next_id(t=None):
    '''
    Return next id as 50-char string.
    Args:
        t: unix timestamp, default to None and using time.time().
    '''
    if t is None:
        t = time.time()
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)


def _profiling(start, sql=''):
    t = time.time() - start
    if t > 0.1:
        logging.warning('[PROFILING] [DB] %s: %s' % (t, sql))
    else:
        logging.info('[PROFILING] [DB] %s: %s' % (t, sql))

class DBError(Exception):
    pass

class MutiColumnsError(DBError):
    pass

class _LasyConnection(object):

    def __init__(self):
        self.connection = None:

    def cursor(self):
        if self.connection is None:
            connection = engine.connect()
            logging.info('open conenction <%s>...' % hex(id(connection)))
            self.connection = connection
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.conection.rollback()

    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            logging.info('close connection <%s>...' % hex(id(connection)))
            connection.close()

class _DdCtx(threading.local):
    """
    Thread local object that holds connection info.
    """
    def __init__(self):
        self.conection = None
        self.transaction = 0

    def is_init(self):
        return not self.conection is None

