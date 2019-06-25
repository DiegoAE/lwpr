from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib, parse_config_h
import os

requirements = ['numpy']

lwprsources = ['lwprmodule.c', 
               'src/lwpr.c', 
               'src/lwpr_xml.c', 
               'src/lwpr_math.c', 
               'src/lwpr_binio.c', 
               'src/lwpr_mem.c', 
               'src/lwpr_aux.c']

configs = parse_config_h(open('include/lwpr_config.h'))

if 'HAVE_LIBEXPAT'in configs and configs['HAVE_LIBEXPAT']:
   module = Extension('lwpr', 
      include_dirs = ['include', os.path.join(get_python_lib(),'numpy','core','include')],
      libraries = ['expat'],   
      sources = lwprsources)
else:
   module = Extension('lwpr',
      include_dirs = ['include', os.path.join(get_python_lib(),'numpy','core','include')],
      sources = lwprsources)

setup (name = 'LWPR Module',
       version = '1.1',
       description = 'Python wrapper around LWPR library',
       ext_modules = [module],
       install_requires = requirements)
