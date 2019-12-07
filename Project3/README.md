This work is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License.
(http://creativecommons.org/licenses/by-nc-nd/4.0/)

ECS 175 Fall 2019 - Assignment 3 Manual
Author: lxylxy123456 (https://github.com/lxylxy123456/)

# Run
* make sure `test_scene` is in same directory (I provided a file which is a
  small updated version on `cube_and_icosahedron.txt`)
* Run the following line
`./Project3`
* Or specify a file: e.g. `test_scene2`
`./Project3 test_scene2`

# Screen layout
The layout of the screen follows the one given by test file:
* upper left is project to XY plane
    * horizontal: x
    * vertical: y
    * From point is equivalent to (0.5, 0.5, inf)
* upper right is project to XZ plane
    * horizontal: x
    * vertical: z
    * From point is equivalent to (0.5, inf, 0.5)
* lower left is project to YZ plane
    * horizontal: y
    * vertical: z
    * From point is equivalent to (inf, 0.5, 0.5)

# Interactions
* All interactions can be done by simply looking at the stdout output.
  Each time input an integer to specify which menu option, then follow what
  prints on the screen. 
* For example, enter `1`, then enter ID of a polyhedral can hide / show it. 
* Each time when anything (even hidden object) goes outside the unit box,
  the program will ask whether a bounding box should be used. Type 0 or 1 for
  not using or using the bounding box. 
* To quit, type `0` and enter. 

## From Project 2
I included some functionality from project 2 for convenience. 
* Menu entry `2` translates a polyhedral. specify polyhedral ID and translation
  vector.
* Menu entry `3` rotates a polyhedral. specify polyhedral ID, two points
  on rotation axis, and rotation angle. 
* Menu entry `4` scales a polyhedral. specify polyhedral ID, and scaling factor.
* Note that changes will NOT be written to the input file (unlike in project 2).

## Phong's lighting model
Note: to turn off Phong model, use menu entry `13`. 

Menu entry `5` leads to a sub-menu for setting Phong's lighting model's
 parameters. The default values are displayed clearly in the sub-menu. 
* Sub-entry 2, 3, 4, 5, 6, 7 are specifying 3D vector or color. Use three
  floating point values as xyz or rgb. 
* Sub-entry 1, 8, 13 are values of a single floating point value. 
* Sub-entry 9, 10, 11, 12 can turn on / off ambient, diffuse, or specular
  lightning, and color normalizing (no argument).
* Sub-entry 1 and 2 are exclusive. Selecting one will disable the other. 
    * Sub-entry 1 is calculating from points w.r.t. each projection. For
      example, if the distance is set to 10, then the from points will be
      (0.5, 0.5, 10), (0.5, 10, 0.5), (10, 0.5, 0.5) for XY, XZ, YZ plane.
      (this is the default value)
    * Sub-entry 2 is making both three projections use the same from point. 
* Sub-entry 12 and 13 are exclusive, which defines how to map color after this
  calculation to r, g, b in [0, 1]
    * Sub-entry 12 is normalizing all color such that the brightest is 1.
      Sometimes this may make the color unstable when the light changes. 
    * Sub-entry 13 is multiplying all color by a constant, and force colors
      larger than 1 to be 1. In this method, some thing may be too bright or too
      dark, then you can look at output of Sub-entry 12 and decide a reference
      constant. The defult behavior has the constant value of 100. 

## Half-toning
Select menu entry `6` turns on / off half-toning model (no arguments). 

## Extra features
The following features are implemented during development, and are provided
just for convenience. 

* I implemented two versions to calculate a vertex's color. 
    * The default one is calculating a normal of average from each face. 
    * By selecting menu entry `10`, each vertex will have different color for
      different faces. This makes it easier to debug. 
* To enable backface culling, use menu entry `11` (color normalization may
  change)
* To use painter's algorithm instead of Z-buffer, use menu entry `12`. 

# Extra credit

## Camera viewing model
* Menu entry `7`: a simple model. Input 10 will make the each plane be viewing
  from point (0.5, 0.5, 10), (0.5, 10, 0.5), (10, 0.5, 0.5).
    * Example: distance about 0.5 on `cube_and_icosahedron.txt`
* Menu entry `8` is the complete model, (clipping NOT implemented)
  specify f, a, u, alpha, ze max, ze min manually. Only upper left screen used.
  These parameters do not change values in Phong's lighting model.
    * Example: run with `cube_and_icosahedron.txt` or `bunny.txt`, then enter:
        `    8    5 5 5    -1 -1 -1    0 1 0    3    100    0.1    `

## Animation
* Make sure files `cube_and_icosahedron.txt` and `bunny.txt` exist
* A rotation sample with the simple camera view: `python3 anime_rotate.py`.
	* Pre-rendered version: `anime_rotate.gif`
* A demo of the real camera viewing model: `python3 anime_camera.py`.
	* Pre-rendered version: `anime_camera.gif`
* A rotating rabbit: `bash anime_bunny.sh 3`
    * Decreasing the `3` will make image smaller and animation more fluent.
	* Pre-rendered version: `anime_bunny.gif`
	* You need to wait for less than 30 seconds to see it moving. 
* After testing animation, please run `make clean; make Project3`

## Colored half-toning
Select menu entry `14` turns on / off half-toning model (no arguments). 

