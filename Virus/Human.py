import numpy as np
from functools import reduce
import random

class Human :
    id = 0
    infected = 0
    dead = 0
    contact = 0
    healed = 0
    position_x = 0
    position_y = 0
    
    def __init__(self,id,infected,dead,contact,position):
        self.id = id
        self.infected = infected
        self.dead = dead
        self.contact = contact
        self.position_x = position[0]
        self.position_y = position[1]
        return
        
    def __str__(self):
        out=""
        if self.infected == 0 :
            out+="Human " + str(self.id)+" not infected"
        elif self.infected != 0 and self.dead == 0:
            out+="Human " + str(self.id)+" infected, not dead"
        elif self.infected != 0 and self.dead == 1:
            out+="Human " + str(self.id)+" infected and dead"
            
        print("contact : " + str(self.contact))
        return out
    
    def survive(self):
        self.infected += 1
    
    def infect(self):
        if self.infected ==0:
            self.infected = 1
    
    def kill(self):
        self.dead = 1
        
    def heal(self):
        self.infected = -1