#!/usr/bin/env python3

"""
    Netstrings module for Python 3
    Copyright (C) 2015  Alfredo Mungo <alfredo.mungo@openmailbox.org>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -----------------------------------------------------------------------------------------

    Netstrings specification: http://cr.yp.to/proto/netstrings.txt
"""

__version__ = '1.0.0'

if __name__ == '__main__':
  import sys
  sys.exit('This is a Python module and not intended to be run as a standalone application')

def encode(data):
  """
    Encodes a bytes object into a netstring and returns the result as another bytes object.
  """
  return (str(len(data)).encode('ascii') + b':' + data + b',')

def decode(b):
  """
    Decodes the first netstring in the provided bytes object, returning the contained data as another bytes object.
    
    THROWS:
      ValueError if the provided bytes object does not begin with a valid netstring
  """
  slen, s = _decode(b)

  return s[:slen]

def _decode(b):
  """
    Internal decode function (see decode()).

    RETURN VALUE:
      A tuple (slen: int, s: bytes) where slen is the length of the data in bytes and s is the initial buffer with length and colon removed.

    THROWS:
      ValueError if the provided bytes object does not begin with a valid netstring
  """
  slen, s = b.split(b':', 1)
  slen = int(slen.decode('ascii'))

  if slen < 0 or s[slen] != b','[0]:
    raise ValueError

  return (slen, s)

def size(b):
  """
    Returns the size in bytes of the first netstring in the provided bytes object.
    WARNING: This function doesn't check for netstring validity.

    THROWS:
      ValueError if cannot determine size
  """
  try:
    slen = b[:b.find(b':')].decode('ascii')

    return 2 + len(slen) + int(slen)
  except:
    raise ValueError

def length(b):
  """
    Returns the length of the first netstring in the provided bytes object without decoding it.
    WARNING: This function doesn't check for netstring validity.
  """
  try:
    return int(b[:b.find(b':')].decode('ascii'))
  except:
    raise ValueError

def is_valid(b):
  """
    Checks the validity of the nestring at the beginning of the given bytes object.

    RETURNS:
      True if the given buffer objects starts with a valid nestring, False if not.
  """
  try:
    slen, s = _decode(b)
  except:
    return False

  return True
