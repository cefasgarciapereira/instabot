import numpy as np
friends = ['@plmacch', '@gregoryassis', '@tulio3m', '@ana.carolina.poscidonio', '@machatelie', '@marcela_danza', '@lucas.rte', '@maceli_berloques', '@arquiteta.danza', '@swatboss93', '@gabrielradec']

def generate_tags(lst, number_of_friends):
    sub = np.random.choice(friends,2, replace=False)
    response = ''
    for s in sub:
        response += s+' '
    return response

print(generate_tags(friends, 2))