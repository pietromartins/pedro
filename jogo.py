# coding: utf-8

import os, sys

sys.path.insert(0, os.getcwd() + "/mapengine")

import mapengine
from mapengine import Scene, simpleloop
from mapengine.base import Actor, Hero, GameObject, Event

class ator(Hero):
    weight = (0,1)
    def update(self):
        if (self.pos[1] < self.controller.scene.height - 1):
            object = self.controller[self.pos[0], self.pos[1] + 1]
            hardness = getattr(object, "hardness", 0)
            if hardness < self.strength:
                self.move(self.weight)
        return super(ator, self).update()
    

class chao(GameObject):
    hardness = 5

class Escada_diagonal(GameObject):
    hardness = 5
    def on_touch(self, other):
        if isinstance(other, Hero):
            if other.pos[1] > 0:
                other.pos = other.pos[0], other.pos[1] - 1
                other.weight = (0,0)
                other.events.add(Event(other.base_move_rate * 2, "weight", (0,1)))
        super(Escada_diagonal, self).on_touch(other)

def main():
    scene = Scene("fase_1")
    simpleloop(scene, (800,600),)

 
 
main()
