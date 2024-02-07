#!/usr/bin/python3
"""  
	return list of available attrs and methods
	
"""

def lookup(obj):
    """return list of available attrs"""
    return dir(obj)
