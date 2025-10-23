def create_player(name:str):
    if name=='':
        user='AI'
    else:
        user=name
    dic={"name":user,"hand":[],"won_pile":[]}
    return dic


def init_game():
    return {}
def play_round(p1:dict,p2:dict):
    return ({},{})
