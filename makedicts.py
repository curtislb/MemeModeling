'''
makdicts.py
-does the preliminary loading in of giant files, stripes them line by line to create entries
-then uses curtis's code to create dictionaries of infected domain names and pickles those dictionaries for further use
'''

from Entry import Entry, base_url
from infected_time import get_infected_times

import read
import time

import cPickle as pickle

fn = '/home/curtis/Downloads/quotes_2008-08.txt'
ents = read.open_and_test(fn)
print 'number of entries: ', len(ents)

infectdomains = get_infected_times(fn, 'i can see russia')
print 'number of infected domains: ', len(infectdomains)

with open('russia_aug.pickle', 'wb') as handle:
   pickle.dump(infectdomains, handle)
