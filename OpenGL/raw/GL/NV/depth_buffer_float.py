'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_depth_buffer_float'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_depth_buffer_float',error_checker=_errors._error_checker)
GL_DEPTH32F_STENCIL8_NV=_C('GL_DEPTH32F_STENCIL8_NV',0x8DAC)
GL_DEPTH_BUFFER_FLOAT_MODE_NV=_C('GL_DEPTH_BUFFER_FLOAT_MODE_NV',0x8DAF)
GL_DEPTH_COMPONENT32F_NV=_C('GL_DEPTH_COMPONENT32F_NV',0x8DAB)
GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV=_C('GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV',0x8DAD)
@_f
@_p.types(None,_cs.GLdouble)
def glClearDepthdNV(depth):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glDepthBoundsdNV(zmin,zmax):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glDepthRangedNV(zNear,zFar):pass