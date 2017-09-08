"""
Class defining KITTI format
"""

import os, cv2, sys, shutil, glob, argparse, random
import numpy as np
import os.path as osp

class KITTIDetection:
	"""
	Enumerate the classes available for KITTI Object Detection
	"""
	Dontcare, Car, Van, Truck, Bus, Pickup, VehicleWithTrailer,\
	SpecialVehicle, Person, Person_fa, Person_unsure, People, Cyclist,\
	Tram, Person_Sitting, Misc = range(16)

	def __init__(self):
		pass

class Bbox:
	"""
	Methods dealing with bounding boxes
	"""
	def __init__(self, x_left=0, y_top=0, x_right=0, y_bottom = 0):
		self.xl = x_left
		self.yt = y_top
		self.xr = x_right
		self.yb = y_bottom

	def area(self):
		return (self.xr - self.xl) * (self.yb - self.yt)

	def width(self):
		return self.xr - self.xl

	def height(self):
		return self.yb - self.yt

	def get_array(self):
		return[self.xl, self.yt, self.xr, self.yb]

class KittLabelFormat(object):
	"""
	KITTI Object Detection Label Format

    #Values    Name      Description
    ----------------------------------------------------------------------------
    1    type         Class ID
    1    truncated    Float from 0 (non-truncated) to 1 (truncated), where
                      truncated refers to the object leaving image boundaries.
                      -1 corresponds to a don't care region.
    1    occluded     Integer (-1,0,1,2) indicating occlusion state:
                      -1 = unknown, 0 = fully visible,
                      1 = partly occluded, 2 = largely occluded
    1    alpha        Observation angle of object, ranging [-pi..pi]
    4    bbox         2D bounding box of object in the image (0-based index):
                      contains left, top, right, bottom pixel coordinates
    3    dimensions   3D object dimensions: height, width, length (in meters)
    3    location     3D object location x,y,z in camera coordinates (in meters)
    1    rotation_y   Rotation ry around Y-axis in camera coordinates [-pi..pi]
    1    score        Only for results: Float, indicating confidence in
                      detection, needed for p/r curves, higher is better.
    Here, 'DontCare' labels denote regions in which objects have not been labeled,
    for example because they have been too far away from the laser scanner.
    """

    OBJECT_TYPES = {
    	'bus': KITTIDetection.Bus,
    	'car': KITTIDetection.Car,
    	'cyclist': KITTIDetection.Cyclist,
    	'pedestrian': KITTIDetection.Person,
    	'people': KITTIDetection.People,
    	'person': KITTIDetection.Person,
    	'person_sitting': KITTIDetection.Person_Sitting,
    	'person_fa': KITTIDetection.Person_fa,
    	'person?': KITTIDetection.Person_unsure,
    	'pickup': KITTIDetection.Pickup,
    	'misc': KITTIDetection.Misc,
    	'special-vehicle': KITTIDetection.SpecialVehicle,
    	'tram': KITTIDetection.Tram,
    	'truck': KITTIDetection.Truck,
    	'van': KITTIDetection.Van,
    	'vehicle-with-trailer': KITTIDetection.VehicleWithTrailer
    }

	def __init__(self):
		self.type = ''
		self.truncated = -1
		self.occlusion = -1
		self.alpha = 0.0
		self.height = 0.0
		self.width = 0.0
		self.length = 0.0
		self.locx = 0.0
		self.locy = 0.0
		self.locz = 0.0
		self.roty = 0.0
		self.bbox = BBox()
		self.object = KITTIDetection.Dontcare
		self.score = -1

    def set(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])