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

def gen_data(file=sys.stdout) :
	a = [	# x1, y1, x2, y2
		(49.0,-46.0,64.0,-50.5),
		(44.5,-35.5,49.0,-50.5),
		(44.5,-31.0,64.0,-35.5),
		(27.5,-46.0,42.5,-50.5),
		(22.5,-35.5,27.5,-50.5),
		(22.5,-31.0,42.0,-35.5),
		(16.0,-35.5,20.5,-51.0),
		( 4.5,-31.0,20.5,-35.5),
		( 0.0,-24.0, 4.5,-53.5),
	]
	z1 = 0.3
	z2 = 0.7

	vertices = []
	edges = []

	for i in a :
		x1, y1, x2, y2 = i[0] / 64, 1 + i[1] / 64, i[2] / 64, 1 + i[3] / 64
		x1, y1, x2, y2 = map(lambda x: x * 0.9 + 0.05, (x1, y1, x2, y2))
		l = len(vertices)
		edges.append((l + 1, l + 2))
		edges.append((l + 2, l + 3))
		edges.append((l + 3, l + 4))
		edges.append((l + 4, l + 1))
		edges.append((l + 5, l + 6))
		edges.append((l + 6, l + 7))
		edges.append((l + 7, l + 8))
		edges.append((l + 8, l + 5))
		edges.append((l + 1, l + 5))
		edges.append((l + 2, l + 6))
		edges.append((l + 3, l + 7))
		edges.append((l + 4, l + 8))
		vertices.append((x1, y1, z1))
		vertices.append((x2, y1, z1))
		vertices.append((x2, y2, z1))
		vertices.append((x1, y2, z1))
		vertices.append((x1, y1, z2))
		vertices.append((x2, y1, z2))
		vertices.append((x2, y2, z2))
		vertices.append((x1, y2, z2))
	print(1, file=file)
	print(len(vertices), file=file)
	for i in vertices :
		print(*i, file=file)
	print(len(edges), file=file)
	for i in edges :
		print(*i, file=file)

gen_data(open('/tmp/hcc_scene', 'w'))
os.system('chmod u+w /tmp/hcc_scene')

DEG = 5

p = subprocess.Popen(['./Project2', '/tmp/hcc_scene'], stdin=-1)
p.stdin.write(b'6\n1\n')
p.stdin.flush()
for index in range(1000) :
	rad = index * DEG * math.pi / 180
	p.stdin.write(b'3 0  .5 0 .5  .5 1 .5 %d\n' % DEG)
	p.stdin.flush()
	time.sleep(0.05)
p.stdin.write(b'0\n0\n')
p.stdin.flush()
print(p.wait())

