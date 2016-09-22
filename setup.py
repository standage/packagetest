from setuptools import setup, Extension
import glob

headers = list(glob.glob('inc/*.hpp'))

bogus = Extension(
    'bogus',
    sources=['bogus.pyx', 'src/bogus.cpp'],
    include_dirs=['inc/'],
    language='c++',
    extra_compile_args=['--std=c++11', '-Wno-unused-function'],
    extra_link_args=['--std=c++11'],
)

setup(
    name='bogus',
    description='Troubleshooting Python packaging and distribution',
    author='Daniel Standage',
    ext_modules=[bogus],
    install_requires=['cython'],
    version='0.1.0'
)
