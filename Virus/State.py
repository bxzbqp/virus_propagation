import numpy as np
from functools import reduce
from Virus.Human import Human

class State:
    currrent_population = np.array([Human(i,0,0,0) for i in range(10)])
    
    def __init__(self,size_population,n_infected,n_dead,avg_contact,std_contact):
        try :
            if n_dead <= n_infected and n_infected <= size_population:
                
                clean_humans = [Human(i,0,0,
                                      max(0,int(np.random.normal(avg_contact,
                                                                 std_contact))))
                                for i in range(size_population-n_infected)]
                
                infected_humans = [Human(i+n_infected,1,0,
                                         max(0,int(np.random.normal(avg_contact,
                                                                    std_contact)))) 
                                   for i in range(n_infected-n_dead)]
                
                dead_humans = [Human(i+n_dead,1,1,
                                     max(0,int(np.random.normal(avg_contact,
                                                                std_contact)))) 
                               for i in range(n_dead)]
                
                self.current_population = np.append(clean_humans,
                                                    np.append(infected_humans,
                                                              dead_humans))
                
            elif n_dead > n_infected:
                raise ValueError
            elif n_infected > size_population:
                raise ValueError
        except ValueError:
            print('too many dead or infected')
        return
        
    def __str__(self):
        out = "size of your population : " + str(self.size)
        for elem in self.current_population:
            out += '\n'
            out += elem.__str__()
        return out
        
    def kill(self,ids_to_kill):
        for id in ids_to_kill:
            self.current_population[id].kill()
            
    def heal(self,ids_to_heal):
        for id in ids_to_heal:
            self.current_population[id].heal()
    
    def infect(self, ids_to_infect):
        for id in ids_to_infect:
            self.current_population[id].infect()
    
    def survive(self, ids_to_survive):
        for id in ids_to_survive:
            self.current_population[id].survive()
    
    def size(self):
        return len(self.current_population)
    
    def get_n_infected(self):
        return len(self.get_humans_infected())
    
    def get_n_dead(self):
        return len(self.current_population)-len(self.get_humans_alive())
    
    def get_n_healed(self):
        return len(self.get_humans_healed())
    
    def get_humans_infected(self):
        return [human.id for human in self.current_population if human.infected > 0]
    
    def get_humans_healed(self):
        return [human.id for human in self.current_population if human.infected < 0]
    
    def get_humans_not_infected(self):
        return [human.id for human in self.current_population if human.infected ==0]
    
    def get_humans_alive(self):
        return [human.id for human in self.current_population if human.dead == 0]
    
    #def get_humans_contaminable(self):
    #    return [human.id for human in self.get_humans_alive() if human.infected == 0]
    
    def print_summary(self):
        print("_________")
        print("Infected : " + str(self.get_n_infected()))
        print("Deads : " + str(self.get_n_dead()))
        print("Healed : " + str(self.get_n_healed()))
        print("_________")
        return