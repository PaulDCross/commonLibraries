import os
import math
import random
import numpy as np
import time
import Vector
import matplotlib.cm as cm
import matplotlib as mpl

def bearingMeasurement(dx, dy):
    a = math.atan2(dx,dy)
    a = a*(a>=0) + (a+2*math.pi)*(a<0)
    return round(a*(180/math.pi),1)

def bearingMeasurementRad(dx, dy):
    a = math.atan2(dx,dy)
    a = a*(a>=0) + (a+2*math.pi)*(a<0)
    return a

def chunker(seq, size):
    return [seq[pos:pos + size] for pos in xrange(0, len(seq), size)]

def colourise(value, minimum, maximum):
    norm   = mpl.colors.Normalize(vmin=minimum, vmax=maximum)
    m      = cm.ScalarMappable(norm=norm, cmap=cm.gray)
    colour = np.array(m.to_rgba(value)[:-1])*255
    return colour[::-1]

def linspace(start, end, step=1, sigfigs=1, type="+"):
    array = []
    temp = start
    if type == "+":
        while round(temp,sigfigs) <= round(end,sigfigs):
            array.append(round(temp,sigfigs))
            temp += step
    if type == "-":
        while round(temp,sigfigs) >= round(end,sigfigs):
            array.append(round(temp,sigfigs))
            temp -= step
    return array

def makedir(DIR):
    if not os.path.exists(DIR):
        os.makedirs(DIR)

def size(x):
    return int(round((0.0333*x) + 3.3333, 0))

def readFile2List(textFile):
    with open(textFile, "r") as file:
        data = []
        for line in file.readlines():
            data.append([float(i) for i in line.split()])
    return data

def writeList2File(textFile, DATA):
    with open(textFile, "w") as file:
        DATA = '\n'.join('\t'.join(map(str,j)) for j in DATA)
        file.write(DATA)

def lowerLimit(value, minimum):
    return max(minimum, value)

def upperLimit(value, maximum):
    return min(maximum, value)

def limit(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def mapValue(OldValue, OldMin, OldMax, NewMin, NewMax):
    # Range = maximum - minimum
    # New value = (((Old value - Old minimum) * New Range) / Old Range + New minimum)
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

def lerpColour(scolour, fcolour, p):
    return tuple((np.array(scolour)*(1-p) + np.array(fcolour)*p).astype(int))

def polygon(sides, radius, offset=None):
    if offset == None:
        offset = Vector.Vector([0, 0])
    points = [[radius*math.sin(2*math.pi*float(i/sides))+offset.x, radius*math.cos(2*math.pi*float(i/sides))+offset.y] for i in linspace(1,sides)]
    points.append(points[0])
    points = np.array(points)
    return points

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def overlap(r1,r2):
    '''Overlapping rectangles overlap both horizontally & vertically
    '''
    r1_left   = r1[0]
    r1_right  = r1[0] + r1[2]
    r1_top    = r1[1]
    r1_bottom = r1[1] + r1[3]

    r2_left   = r2[0]
    r2_right  = r2[0] + r2[2]
    r2_top    = r2[1]
    r2_bottom = r2[1] + r2[3]

    hOverlaps = (r1_left <= r2_right)  and (r1_right  >= r2_left)
    vOverlaps = (r1_top  <= r2_bottom) and (r1_bottom >= r2_top)
    return hOverlaps and vOverlaps


def sigmoid(x, deriv=False):
    if(deriv==True):
        return (x*(1-x))
    return 1/(1+np.exp(-x))

def tanh(x, deriv=False):
    if(deriv == True):
        return (1-(x**2))
    return np.tanh(x)

