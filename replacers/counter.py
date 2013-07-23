#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

from collections import Counter

# Taken from http://bugs.python.org/issue18352 in the file
# counter_copy_attrs_2.patch
class _Counter(Counter):
    def copy(self):
        "Return a shallow copy."
        copy = self.__class__(self)
        copy.__dict__.update(vars(self))
        return c

    def __reduce__(self):
        return self.__class__, (dict(self),), vars(self) or None
