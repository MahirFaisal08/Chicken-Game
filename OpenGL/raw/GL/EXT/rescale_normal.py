'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_rescale_normal'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_rescale_normal',error_checker=_errors._error_checker)
GL_RESCALE_NORMAL_EXT=_C('GL_RESCALE_NORMAL_EXT',0x803A)
