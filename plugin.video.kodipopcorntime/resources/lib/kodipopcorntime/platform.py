﻿#!/usr/bin/python
import sys, os

class Platform(object):
    class __metaclass__(type):
        def __getattr__(cls, name):
            getattr(cls, "_%s" % name)()
            return getattr(cls, name)

        def _arch(cls):
            if sys.platform.lower().startswith('linux') and (os.uname()[4].lower().startswith('arm') or os.uname()[4].lower().startswith('aarch')):
                if os.uname()[4].lower().startswith('armv6'):
                    cls.arch = 'armv6'
                cls.arch = 'arm'
            elif sys.maxsize > 2**32:
                cls.arch = 'x64'
            else:
                cls.arch = 'x86'

        def _system(cls):
            if sys.platform.lower().startswith('linux'):
                cls.system = 'linux'
                if 'ANDROID_DATA' in os.environ:
                    cls.system = 'android'
            elif sys.platform.lower().startswith('win'):
                cls.system = 'windows'
            elif sys.platform.lower().startswith('darwin'):
                cls.system = 'darwin'
            else:
                cls.system = None
