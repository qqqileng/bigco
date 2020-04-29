from matching_algorithm import *

tellers = {}
d = {}
d['language'] = 'Japanese'
d['service'] = 'Card'

tellers = run_algo('John Smith', d['language'], d['service'], 'US')

the_list = ['language', 'service', 'location', 'availability']
for key1 in tellers:

    teller1 = tellers[key1][0]
    teller2 = tellers[key1][1]
    teller3 = tellers[key1][2]

    print(teller1[1])

    
    teller_1 = teller1[1]
    teller_2 = teller2[1]
    teller_3 = teller3[1]


    teller_1_name = teller1[0]
    teller_1_lang = teller_1[the_list[0]]
    teller_1_serv = teller_1[the_list[1]]
    teller_1_loc = teller_1[the_list[2]]
    teller_1_avail = teller_1[the_list[3]]

    teller_2_name = teller2[0]
    teller_2_lang = teller_2[the_list[0]]
    teller_2_serv = teller_2[the_list[1]]
    teller_2_loc = teller_2[the_list[2]]
    teller_2_avail = teller_2[the_list[3]]

    teller_3_name = teller3[0]
    teller_3_lang = teller_3[the_list[0]]
    teller_3_serv = teller_3[the_list[1]]
    teller_3_loc = teller_3[the_list[2]]
    teller_3_avail = teller_3[the_list[3]]

    
##    for key2 in teller1[1]:
##
##        teller1_lang = teller1[1][0]
####        teller1_serv =
####        teller1_loc =
####        teller1_avail = 
    
    
