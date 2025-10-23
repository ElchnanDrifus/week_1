
def create_card(rank,suite):
     dic={}
     if rank=='j':
         value=11
     elif rank=='q':
         value=12
     elif rank=='k':
         value=13
     elif rank=='a':
         value=14
     else:
         value=rank
     dic['rank']=rank
     dic['suite']=suite
     dic['value']=value
     return dic





def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card['value']>p2_card['value']:
        return 'p1'
    elif p1_card['value']<p2_card['value']:
        return 'p2'
    else:
        return 'WAR'


def create_deck():
    arr_card=[]
    for i in range(2,15):
        a=i
        if a==11:
            a='j'
        elif a==12:
            a='q'
        elif a==13:
            a='k'
        elif a==14:
            a='a'
        for j in ['c', 's', 'd', 'h']:
            dic={}
            dic['rank']=a
            dic['suite']=j
            dic['value']=i
            arr_card.append(dic)
    return arr_card





def shuffle(deck:list[dict]):
    return({},{})


