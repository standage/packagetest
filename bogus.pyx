# distutils: language = c++
# distutils: sources = src/bogus.cpp
# cython: c_string_type=str, c_string_encoding=ascii

cdef extern from 'bogus.hpp':
    cdef cppclass bogus:
        bogus() except +
        int get_double(int value)

cdef class Bogus:
    cdef bogus b
    def get_double(self, int value):
        return self.b.get_double(value)
