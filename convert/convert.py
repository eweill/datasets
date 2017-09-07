"""
Convert one annotation format to another.

Supported Conversions:
    KITTI -> YOLO
    KITTI -> VOC
    VOC   -> KITTI
    VOC   -> YOLO
    YOLO  -> KITTI
    YOLO  -> VOC

Usage:
    python convert.py
"""

from __future__ import print_function
import os, sys, shutil, glob, argparse
import cv2, random
import numpy as np
import os.path as osp
from PIL import Image, ImageOps
