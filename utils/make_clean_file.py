"""
Utility to create a new file.
Remove any file with the same name.
"""

import os.path as osp
import os.remove as osr

def make_clean_file(file_name):
    """
    Remove file (if exists) and open another (clean) file

    Parameters:
        file_name - file name to create
    Returns:
        fp - file points to newly created file
    """
    if osp.isfile(file_name):
        osr(file_name)

    fp = open(file_name, 'a+')
    return fp
