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

	def __init__(self):
		self.type = ''		# Describes the type of object: 'Car', 'Van',
							# 	'Truck', 'Pedestrian', 'Person_sitting',
							#	'Cyclist', 'Van', 'Misc', or 'DontCare'
		self.truncated = -1	# Float from 0 (non-truncated) to 1 (truncated)
							# where truncated refers to the object leaving
							# image boundaries
		self.occluded = -1	# Integer (0,1,2,3) indicating occlusion stat:
							# 0 = fully visible, 1 = partly occluded
							# 2 = largely occluded, 3 = unknown
		self.alpha = 0.0	# Observation angle of object, ranging [-pi..pi]
		self.x1 = 0.0
		self.y1 = 0.0
		self.x2 = 0.0
		self.y2 = 0.0
		self.bbox = (x1,y1,x2,y2)	# 2D bounding box of object in the
									# image (0-based index):
									# contains left, top, right, bottom
									# pixel coordinates
		self.dimensions = (0.0,0.0,0.0)	# 3D object dimensions: height, width,
										# length (in meters)
		self.location = (0.0,0.0,0.0)	# 3D object location x,y,z in camera
										# coordinates (in meters)
		self.rotation_y = 0.0	# Rotation ry around Y-axis in cameras
								# coordinates [-pi..pi]
		self.score - -1.0	# Only for results: Float, indicating confidence
							# in detection, needed for p/r curves, higher is
							# better

    def set(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])