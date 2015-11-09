"""
Colors.py, module definition of Colors class.
This is a class aimed at coloring prints.
"""
# Copyright (C) 2015  Stefano Zaghi
#
# This file is part of FoBiS.py.
#
# FoBiS.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FoBiS.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FoBiS.py. If not, see <http://www.gnu.org/licenses/>.


class Colors(object):
  """
  Colors is an object that handles colors of shell prints, its attributes and methods.
  """
  def __init__(self,
               red='\033[1;31m',
               bld='\033[1m'):
    self.red = red
    self.bld = bld
    self.end = '\033[0m'

  def enable(self):
    """Method for enabling colors."""
    self.red = '\033[1;31m'
    self.bld = '\033[1m'
    self.end = '\033[0m'

  def disable(self):
    """Method for disabling colors."""
    self.red = ''
    self.bld = ''
    self.end = ''

  def print_b(self, string):
    """
    Method for printing string with bold color.

    Parameters
    ----------
    string : str
      string to be printed
    """
    print(self.bld + string + self.end)
    return

  def print_r(self, string):
    """
    Method for printing string with red color.

    Parameters
    ----------
    string : str
      string to be printed
    """
    print(self.red + string + self.end)
    return