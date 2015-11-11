# coding: utf-8

import os, sys

sys.path.insert(0, os.getcwd() + "/mapengine")

import mapengine
from mapengine import Scene, simpleloop
from mapengine.base import Actor, MainActor, GameObject, Event, Directions, Event

class ator(MainActor):
    weight = Directions.DOWN
    
    # Não deixa o ator voar
    falling_counter = 0
    def move(self, direction):
        abaixo = self.pos[0], self.pos[1] + 1
        if direction == Directions.UP and not getattr(self.controller[abaixo], "hardness", 0) > 0:
            return
        return super(ator, self).move(direction)
    
    # Faz o actor cair até o chão para começar a fase
    def update(self):
        if (self.pos[1] < self.controller.scene.height - 2):
            object = self.controller[self.pos[0], self.pos[1] + self.weight[1]]
            hardness = getattr(object, "hardness", 0)
            if hardness < self.strength and self.weight[1]:
                self.falling_counter += 1
                if self.falling_counter >= self.base_move_rate:
                    saved_value = self.move_counter
                    self.move_counter = self.falling_counter
                    self.move(self.weight)
                    self.move_counter = saved_value
        return super(ator, self).update()
    
    # Método on_fire é acionado quando aperta espaço
    # Implementa o pulo
    def on_fire(self):
        if not self.weight == Directions.DOWN:
            return
        self.weight = Directions.UP
        self.move((0, -2))
        self.events.add(Event(13, "weight", Directions.DOWN))


# Black corresponde à cor azul na fase
class black(GameObject):
    hardness = 5
    
class chao(GameObject):
    hardness = 5

class castelo(GameObject):
    hardness = 5

class Escada_diagonal(GameObject):
    hardness = 5
    def on_touch(self, other):
        if isinstance(other, ator):
            if other.pos[1] > 0:
                other.pos = other.pos[0], other.pos[1] - 1
                other.weight = (0,0)
                other.events.add(Event(other.base_move_rate * 2, "weight", (0,1)))
        super(Escada_diagonal, self).on_touch(other)


class Escada(GameObject):
    hardness = 2
    def on_over(self, other):
        if isinstance(other, ator):
            other.weight = 0, 0
            other.events.add(Event(5, "weight", (0, 1)))
        super(Escada, self).on_touch(other)
        
        
class Portal(GameObject):
    hardness = 10
    def on_touch(self, other):
        cena = Scene("fase_3")
        self.controller.load_scene(cena)
        self.controller.force_redraw = True
           
    
def main():
    scene = Scene("fase_2")
    simpleloop(scene, (800,600),)

 
 
main()
