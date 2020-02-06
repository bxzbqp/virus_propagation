import numpy as np
from Virus.Human import Human
from Virus.State import State

def init_simulation(params):
    pop = State(params['size_population'],params['n_infected_start'],params['n_dead_start'],params['avg_contact'],params['std_contact'])
    return pop

def contaminate(state, params):
    infected = state.get_humans_infected()
    all_contacted=[]
    for human_infected in [state.current_population[id] for id in infected]:
        contacts = np.random.choice(state.get_humans_alive(),human_infected.contact)
        all_contacted = all_contacted + list(contacts)
    for id_human_contacted in set(all_contacted) :
        if np.random.binomial(1,params['contamination_rate']):
            state.current_population[id_human_contacted].infect()
    return

def kill_survive(state,params):
    infected = state.get_humans_infected()
    for id_human_infected in infected :
        if np.random.binomial(1,params['avg_death_rate']):
            state.current_population[id_human_infected].kill()
        else:
            state.current_population[id_human_infected].survive()
    return

def heal(state, params):
    infected = state.get_humans_infected()
    ids_to_heal = [state.current_population[human_id].id 
                   for human_id in infected if state.current_population[human_id].dead == 0 
                   and state.current_population[human_id].infected >=params['days_to_heal']]
    state.heal(ids_to_heal)
    return

def next_step(state,params,do_print):
    kill_survive(state,params)
    heal(state,params)
    contaminate(state,params)
    if do_print:
        state.print_summary()
    return state