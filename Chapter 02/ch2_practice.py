from math import sqrt
from typing import List
from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5),
                (-3,4), (-4,4), (-5,3), (-5,2), (-2,2),
                (-5,1), (-4,0), (-2,1), (-1,0), (0, -3),
                (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1),
                (5,1)]

#draw(
#    Points(*dino_vectors),
#    Polygon(*dino_vectors)
#)

#def add(v1, v2):
#    return (v1[0]+v2[0], v1[1]+v2[1])

def add(*vectors):
    return (sum(v[0] for v in vectors), sum(v[1] for v in vectors))


def subtract(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

if __name__ == '__main__':
    #draw(Points((2, 2), (-1, 3)),
    #Segment((2, 2), (-1, 3), color=red)
    #)
    u = (-2, 0)
    v = (1.5, 1.5)
    w = (4, 1)
    print('adding u and v' , add(u, v))
    print('adding v and w', add(v, w))
    print('adding u and w', add(u, w))
    print('adding u, v, and w', add(u,v,w))
    test1=[u, v, w]
    translation1 = (0, 1)
    print(translate(translation1, test1))
    print(translate((1,1), [(0,0), (0,1), (3, -3)]))
    
