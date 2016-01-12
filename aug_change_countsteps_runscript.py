# domain_times = get_infected_times('sample-10000.txt','the')
import cPickle as pickle
# open the pickled dictionary of infected domains                                                             
with open('aug_pickle.pickle', 'rb') as handle:
    infectdomains = pickle.load(handle)    
len_time_unit = 86400
start_time = '2008-08-01'
import count_timesteps
S,  I, R = count_timesteps.count_timesteps(len_time_unit, start_time, infectdomains)
count_timesteps.graph_SIR(S,I,R)