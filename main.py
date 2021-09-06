import math
import pandas as pd
import numpy as np
import sklearn
import dronekit

"""
Start with the variables that we know or will find out
1. Target position (P0)
2. Target vector (P1)
3. Target speed (P3)
4. Drone origin (P4)
5. Drone speed (P5)
"""

"""
First equation:
The impact point is the same for both the target and the projectile. It is equal to the starting point of both objects + a certain length along the line of both their vectors. This length is denoted by their respective speeds, and the time of impact. 

P0 + (t * s0 * V0) = P1 + (t * s0 * V)

Second equation

The point of impact's distance from the origin of the projectile is equal to the speed of the projectile multiplied by the time passed

P0 + (t * s0 * V0) <-- point of impact

The point of origin is P1 The distance between these two must be equal to the speed of the projectile multiplied by the time passed (distance = speed * time)

The formula for distance is: (x0 - x1)^2 + (y0 - y1)^2 = distance^2

Third equation

((P0.x + s0 * t * V0.x) - P1.x)^2 + ((P0.y + s0 * t * V0.y) - P1.y)^2 = (s1 * t)^2 

Note:
Once t is discovered, place it into the second equation and find the vector V


"""
