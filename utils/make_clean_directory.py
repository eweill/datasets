"""
Utility to create a new directory.
Remove any directory with the same name.
"""

import os.path as osp
import os.makedirs as osm
import shutil.rmtree as shr

def make_clean_directory(dir_name):
    """
    Remove directory (if exists) and create another (clean) directory

    Parameters:
        dir_name - directory name to create
    Returns:
        None
    """
    if osp.exists(dir_name):
        shr(dir_name, ignore_errors=True)
    osm(dir_name)
