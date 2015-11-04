# coding: utf-8

import os, sys

sys.path.insert(0, os.getcwd() + "/mapengine")

import mapengine
from mapengine import Scene, Actor, simpleloop



def main():
    scene = Scene("fase_1")
    simpleloop(scene, (800,600), True)

 
 
main()
