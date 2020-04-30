
def get_allTheData():
    import ibm_db
    import pandas as pd
    from pandas import DataFrame
    import ibm_db_dbi as db

    conn = db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=sfz85754;PWD=j0-9fgh89tfj30b8;", "", "")

    df = pd.read_sql("SELECT * from TELLER", conn)

    database = df.set_index('name').T.to_dict('dict')
    for key, value in database.items():
        value['language'] = [x.rstrip() for x in value['language'].split(',')]
        value['service'] = [x.rstrip() for x in value['service'].split(',')]

    return database

'''
input: user preference as txt file with features in order: 
language, 
service type, 
location
database: bank assistants as dict of dict of lists/int/string

'''



def sort_ranked_list(prefered_list):
    return(sorted(prefered_list, key = lambda x: x[1], reverse = True)[:3])

def select_bank_assistant(name):
    database[name]['availability'] = 0
    return

def finished_assistant(name):
    database[name]['availability'] = 1

def matching_algorithm(query,threshold, database):
    # set up a threshold for banking assistants to get into the list
    matched = []
    for name in database:
        if not database[name]['availability']:
            continue
        else:
            counterA = set(query['language'])
            counterB = set(database[name]['language'])
            cos_sim_lang = len(counterA.intersection(counterB))/len(counterA)
            counterA = set(query['service'])
            counterB = set(database[name]['service'])
            cos_sim_ser =len(counterA.intersection(counterB))/len(counterA)
            counterA = set(query['location'])
            counterB = set(database[name]['location'])
            cos_sim_loc =len(counterA.intersection(counterB))/len(counterA)
            score = 0.5 * cos_sim_lang + 0.4 * cos_sim_ser + 0.1 * cos_sim_loc
            if score > threshold:
                bank_assistant = name
                matched.append((bank_assistant,score))
    return matched


def run_algo(name, lang, serv, loc):
    import numpy as np
    import pandas as pd
    import sys
    import math
    from collections import Counter

    from pandas.io import sql
    
    the_data = get_allTheData()

    query = {name: {'language': [lang],
      'service': [serv],
      'location': loc}}

    query_map = {'Consumer Checking and Savings':'Consumer','Auto Loans':'Consumer',\
       'Credit Cards':'Consumer','Rewards':'Consumer',\
       'Retirement Planning':'Investment','IRAs and 401(k)s':'Investment',\
       'General Investing':'Investment','College Planning':'Investment',\
       'Mortgage Financing':'Home Loan','Refinancing Home':'Home Loan',\
       'Home Equity':'Home Loan',\
       'Business Checking and Savings':'Business','Lending':'Business',\
       'Payroll':'Business','Merchant':'Business','Financing':'Business'}       
    # map the services into categories
    for name,value in query.items():
        #print(value)
        result = value.pop("service") 
        res = []
        for ser in result:
            res.append(query_map[ser])
        value['service'] = res
    
    threshold = 0.5
    query_result = dict()
    for key,value in query.items(): 
        matched = matching_algorithm(value,threshold, the_data)
        ranked = sort_ranked_list(matched)
        teller_info = {key:[(x[0],the_data[x[0]]) for x in ranked]}
        query_result.update(teller_info)


    return query_result





