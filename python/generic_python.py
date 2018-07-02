#!/usr/bin/env python3
"""
generic_python.py

Purpose
"""

class GenericPython:
    
    def __init__(self):
        pass

def _main(args):
    from sys import argv
    if(len(argv) < 2):
        print("Not enough arguments.")
        return
    return
    
    
if(__name__ == '__main__'):
	import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    _main(args)

