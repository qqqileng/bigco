import numpy as np
import pandas as pd
import sys
import math
from collections import Counter


'''
input: user preference as txt file with features in order: 
language, 
service type, 
location
database: bank assistants as dict of dict of lists/int/string

'''
if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        line = fp.readlines()
    language = [x.rstrip() for x in line[0].split(',')]
    #service = [x.rstrip() for x in line[1].split(',')]
    #location = [x.rstrip() for x in line[2].split(',')]
    language = line[0].rstrip()
    service = line[1].rstrip()
    location = line[2].rstrip()
    #joined = language + service + location
    database = {'Rebecca White':{'language':['English','German','Spanish'], 'service':'card,transfer,check', 'location':'US', 'availability':1},\
                'Aysha Mathis':{'language':['French','Italian','Spanish'], 'service':'savings,loan,mortgage', 'location':'UK', 'availability':0}, \
                'Kimberley Petty':{'language':['Chinese','Japanese','Korean'], 'service':'loan,report,transfer', 'location':'Australia', 'availability':1}}
    best = 0
    bank_assistant = ''
    def counter_cosine_similarity(c1, c2):
        terms = set(c1).union(c2)
        dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
        magA = math.sqrt(sum(c1.get(k, 0) ** 2 for k in terms))
        magB = math.sqrt(sum(c2.get(k, 0) ** 2 for k in terms))
        return dotprod / (magA * magB)

    for name in database:
        if not database[name]['availability']:
            continue
        else:
            counterA = Counter(language)
            counterB = Counter(database[name]['language'])
            cos_sim_lang = counter_cosine_similarity(counterA, counterB)
            counterA = Counter(service)
            counterB = Counter(database[name]['service'])
            cos_sim_ser = counter_cosine_similarity(counterA, counterB)
            counterA = Counter(location)
            counterB = Counter(database[name]['location'])
            cos_sim_loc = counter_cosine_similarity(counterA, counterB)
            score = 0.5 * cos_sim_lang + 0.4 * cos_sim_ser + 0.1 * cos_sim_loc
            if score > best:
                best = score
                bank_assistant = name
                database[name]['availability'] = 0
    print(bank_assistant)




