from octrees import Octree, octree_from_list
from geometry import *

o = Octree(((0.0, 1.0), (0.0, 1.0), (0.0, 1.0)))
o.insert((0.33, 0.66, 0.99), 1)
o.insert((0.12, 0.34, 0.56), 2)
o.insert((0.98, 0.76, 0.54), 3)
for p in o:
    print(p)
o2 = o.deform(lambda p: (p[0]+0.1,p[1],p[2]))
for p in o2:
    print(p)