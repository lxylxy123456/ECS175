#!/bin/bash
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

cp bunny_scene /tmp
# cp test_scene /tmp/bunny_scene
chmod u+w /tmp/bunny_scene

echo 4 0 3  0 | ./Project2 /tmp/bunny_scene
DEG=15
REP=$(echo {1..24})
yes $(
for _ in $REP; do echo 3 0  0 .5 .5  1 .5 .5  $DEG; done	# x
for _ in $REP; do echo 3 0  0 .51 .5  1 .5 .5  $DEG; done
for _ in $REP; do echo 3 0  0 .5 .51  1 .5 .5  $DEG; done
for _ in $REP; do echo 3 0  .5 0 .5  .5 1 .5  $DEG; done	# y
for _ in $REP; do echo 3 0  .5 0 .51  .5 1 .5  $DEG; done
for _ in $REP; do echo 3 0  .51 0 .5  .5 1 .5  $DEG; done
for _ in $REP; do echo 3 0  .5 .5 0  .5 .5 1  $DEG; done	# z
for _ in $REP; do echo 3 0  .5 .51 0  .5 .5 1  $DEG; done
for _ in $REP; do echo 3 0  .51 .5 0  .5 .5 1  $DEG; done
for _ in $REP; do echo 3 0  0 0 .5  1 1 .5  $DEG; done	# xy
for _ in $REP; do echo 3 0  0 0 .5  1 1 .51  $DEG; done
for _ in $REP; do echo 3 0  0 .5 0  1 .5 1  $DEG; done	# xz
for _ in $REP; do echo 3 0  0 .5 0  1 .51 1  $DEG; done
for _ in $REP; do echo 3 0  .5 0 0  .5 1 1  $DEG; done	# yz
for _ in $REP; do echo 3 0  .5 0 0  .51 1 1  $DEG; done
for _ in $REP; do echo 3 0  0 0 0  1 1 1  $DEG; done	# xyz
for _ in $REP; do echo 3 0  1 0 0  0 1 1  $DEG; done	# xyz
for _ in $REP; do echo 3 0  0 1 0  1 0 1  $DEG; done	# xyz
for _ in $REP; do echo 3 0  0 0 1  1 1 0  $DEG; done	# xyz
) | ./Project2 /tmp/bunny_scene

# ./Project2 /tmp/bunny_scene

