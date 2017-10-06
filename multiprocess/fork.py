#!/usr/bin/python
#coding=utf8
"""
# Author: sagata
# Created Time : 2017-10-06 09:33:55

# File Name: fork.py
# Description:

"""
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
