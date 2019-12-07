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

import os, math, time, random, subprocess

os.system("cp bunny_scene /tmp")
# os.system("cp test_scene /tmp/bunny_scene")
os.system('chmod u+w /tmp/bunny_scene')

os.system("echo 4 0 3  0 | ./Project2 /tmp/bunny_scene")
DEG = 15
REP = 24
Z_RATE = 1/7
Z_FUNC = math.cos
if not 'no Z' :
	Z_RATE = 0
	Z_FUNC = math.sin

p = subprocess.Popen(['./Project2', '/tmp/bunny_scene'], stdin=-1)
axis = [1, 0.5, 0.5]
for index in range(10000) :
	p.stdin.write(b'3 0  %f %f %f  %f %f %f  %f\n' %
					(tuple(axis) + tuple(map(lambda x: 1 - x, axis)) + (DEG,)))
	p.stdin.flush()
	theta = index / 30
	axis = [math.sin(theta) / 2 + 0.5, math.cos(theta) / 2 + 0.5,
			Z_FUNC(theta * Z_RATE) / 2 + 0.5]
p.stdin.write(b'0\n')
p.stdin.flush()
print(p.wait())

