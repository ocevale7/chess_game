
def pat(game,echequier,couleur):
    tot = 0
    if couleur == 0:
        for i in game.all_blancs_alive:
            if i.get_id() in echequier:
                tot += len(i.recup_all_pos((i.rect.x//100,i.rect.y//100),echequier,True))
        return tot == 0
    else:
        for i in game.all_noirs_alive:
            if i.get_id() in echequier:
                tot += len(i.recup_all_pos((i.rect.x//100,i.rect.y//100),echequier,True))
        return tot == 0
def repeat(game):
    echequiers = game.list_all_move_in_game
    if len(echequiers) >= 8:
        return (str(echequiers[-1]) == str(echequiers[-5])) and (str(echequiers[-2]) == str(echequiers[-6])) and (str(echequiers[-3]) == str(echequiers[-7])) and (str(echequiers[-4]) == str(echequiers[-8]))

def materiel(game,echequier,couleur):
    have_cavalier = [False,False]
    have_fou = [False,False]
    have_tour = False
    have_dame = False
    have_pion = False
    for x in range(8):
        for y in range(8):
            piece = game.dico_piece_id[echequier[(x,y)]]
            if piece is not(None):
                if piece.name == "cavalier":
                    if piece.color == "blanc":
                        have_cavalier[0] = True
                    else:
                        have_cavalier[1] = True
                elif piece.name == "fou":
                    if piece.color == "blanc":
                        have_fou[0] = True
                    else:
                        have_fou[1] = True
                elif piece.name == "tour":
                    have_tour = True
                elif piece.name == "dame":
                    have_dame = True
                elif piece.name == "pion":
                    have_pion = True
    
    return not(have_pion or have_tour or have_dame or (have_cavalier[0] and have_fou[0]) or (have_cavalier[1] and have_fou[1]))
                
            