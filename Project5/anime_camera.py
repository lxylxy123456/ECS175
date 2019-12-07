#!/usr/bin/python3
#  
#  ECS175 - Computer Graphics class homework demo
#  Copyright (C) 2019  lxylxy123456
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  

import os, sys, math, time, random, subprocess

assert(os.path.exists(sys.argv[1]))

DEG = 10

p = subprocess.Popen(['./Project5', sys.argv[1]], stdin=-1)
p.stdin.write(b'15 1\n')
p.stdin.flush()
for index in range(1000) :
	rad = index * DEG * math.pi / 180
	f = [5, .5 + 4.5 * math.cos(rad), .5 + 4.5 * math.sin(rad)]
	a = [-4.5, -4.5 * math.cos(rad), -4.5 * math.sin(rad)]
	p.stdin.write(b'''
	8
	%f %f %f
	%f %f %f
	0 1 0
	7
	100
	0.1
	''' % tuple(f + a))
	p.stdin.flush()
	time.sleep(0.05)
p.stdin.write(b'0\n0\n')
p.stdin.flush()
print(p.wait())

