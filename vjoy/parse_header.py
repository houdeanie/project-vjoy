import re
import os
from ctypes import *
from pprint import pprint

decl_p = re.compile(r"\s*VJOYINTERFACE_API\s+(\w+)\s+__cdecl\s+(\w+)\((.*)\).+")
enum_p = re.compile(r"\s*enum\s+(\w+).*")

type_lookup = {
    '': "[]",
    'void': "None",
    'pvoid': "c_void_p",
    'uint': "c_uint",
    'int': "c_int",
    'short': "c_short",
    'bool': "c_bool",
    'dword': "c_uint32",
    'word': "c_uint16",
    'long': "c_long",
    'uchar': "c_uint8",
    'byte': "c_uint8",
}

ptr_p = re.compile(r"[const\s+]?(\w+)\s*\*\s*(\w+)")
norm_p = re.compile(r"[const\s+]?(\w+)\s+(\w+)")

def parse_param(p):
    p = p.strip()

    m = ptr_p.findall(p)
    if len(m) > 0:
        return (m[0][0], True, m[0][1])

    m = norm_p.findall(p)
    if len(m) > 0:
        return (m[0][0], False, m[0][1])

    return (p, False, '')
    

def parse_param_list(plist):
    params = plist.split(',')
    for p in params:
        yield parse_param(p)

lines = []
funcs = []

with open("vjoyinterface.h", "r") as fp:
    for line in fp.readlines():
        line = line.strip()

        m = decl_p.findall(line)
        if len(m) > 0:
            l = m[0]
            ret_type = l[0]
            func = l[1]
            plist = list(parse_param_list(l[2]))
            funcs.append((ret_type, func, plist))
            lines.append(f"{ret_type} {func}({l[2]})")
            continue
        
        m = enum_p.findall(line)
        if len(m) > 0:
            type_lookup[m[0]] = c_int
            continue

def get_type(name):
    lname = name.lower()
    if lname in type_lookup:
        return type_lookup[lname]
    
    return name
    # raise ValueError(f"Unknown type: {name}")

def cvt_param_list(plist):
    for ptype, is_ptr, pname in plist:
        ptype = get_type(ptype)
        if ptype in ('None', '[]'):
            ptype = ''
        yield (ptype, is_ptr, pname)

hooks_header =\
"""from ctypes import *
import os

from .constants import *
from .enums import *
from .structs import *

DLL_FILENAME = "vJoyInterface.dll"

DLL_FILEPATH = os.path.join(os.path.dirname(__file__), DLL_FILENAME)

vj = cdll.LoadLibrary(DLL_FILEPATH)
"""

func_names = []
param_names = []

with open("hooks.py", "w") as fp:
    fp.write(hooks_header)

    for line, func in zip(lines, funcs):
        ret_type, fname, plist = func
        func_names.append(fname)
        param_names.append([pname for _,_,pname in plist if len(pname) > 0])

        plist = list(cvt_param_list(plist))
        ret_type = get_type(ret_type)

        fp.write(f"# {line}\n")
        fp.write(f"{fname} = vj.{fname}\n")
        fp.write(f"{fname}.restype = {ret_type}\n")

        params = []
        for ptype, is_ptr, _ in plist:
            if is_ptr:
                params.append(f"POINTER({ptype})")
            else:
                params.append(ptype)
        
        pstr = ','.join(params)

        fp.write(f"{fname}.argtypes = [{pstr}]\n")
        fp.write("\n")

with open("vjoy.py", "w") as fp:
    fp.write("from .hooks import *\n")
    fp.write("class VJoy:\n")
    for line, fname, pnames in zip(lines, func_names, param_names):
        pstr = ', '.join(pnames)
        pstr = pstr.lower()
        fp.write(f"    # {line}\n")
        fp.write(f"    @staticmethod\n")
        fp.write(f"    def {fname}({pstr}):\n")
        fp.write(f"        return {fname}({pstr})\n")
        fp.write("\n")




    
