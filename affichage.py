import pygame
import time
from game import Game
from fleches import *
from class_gagnant import *
from modif_res_images import *

def rock_noir(game,echequier,piece_hand,new_pos_x,new_pos_y):
    """Gère le rock noir"""
    #Si le sens de l'échequier est noir en bas/blanc en haut
    if echequier.sens == 0:
        #Petit rock
        if (new_pos_x,new_pos_y) == (1,7):
            #Change la position de la tour
            echequier[(2,7)] = echequier[(0,7)]
            del echequier[(0,7)]
        #Grand rock
        elif (new_pos_x,new_pos_y) == (5,7):
            #Change la position de la tour
            echequier[(4,7)] = echequier[(7,7)]
            del echequier[(7,7)]
        #Bloque un nouveau rock de ce roi
        piece_hand.can_rock_noir = False
    #Si le sens de l'échequier est noir en haut/blanc en bas
    else:
        #Petit rock
        if (new_pos_x,new_pos_y) == (6,0):
            echequier[(5,0)] = echequier[(7,0)]
            del echequier[(7,0)]
            piece_hand.can_rock_blanc = False
        #Grand rock
        elif (new_pos_x,new_pos_y) == (2,0):
            echequier[(3,0)] = echequier[(0,0)]
            del echequier[(0,0)]
        #Bloque un nouveau rock de ce roi
        piece_hand.can_rock_blanc = False  

def rock_blanc(game,echequier,piece_hand,new_pos_x,new_pos_y):

    if echequier.sens == 1:
        if (new_pos_x,new_pos_y) == (6,7):
            echequier[(5,7)] = echequier[(7,7)]
            del echequier[(7,7)]
        elif (new_pos_x,new_pos_y) == (2,7):
            echequier[(3,7)] = echequier[(0,7)]
            del echequier[(0,7)]
            piece_hand.can_rock_noir = False
    else:
        if (new_pos_x,new_pos_y) == (1,0):
            echequier[(2,0)] = echequier[(0,0)]
            del echequier[(0,0)]
            piece_hand.can_rock_blanc = False
        elif (new_pos_x,new_pos_y) == (5,0):
            echequier[(4,0)] = echequier[(7,0)]
            del echequier[(7,0)]
            piece_hand.can_rock_blanc = False      
        

def quand_a_jouer(game,piece_hand,pos_x,pos_y,new_pos_x,new_pos_y):

    echequier = game.get_echequier()
    new = piece_hand.veref_pos((pos_x,pos_y),(new_pos_x,new_pos_y),echequier)

    if new[0]:
        #Vérifie si la pièce joué ne nous met pas en échec
        faux_echequier = echequier.copy()
        del faux_echequier[(new_pos_x,new_pos_y)]
        del faux_echequier[(pos_x,pos_y)]
        faux_echequier[(new_pos_x,new_pos_y)] = piece_hand.get_id()
        est_echec = game.is_echec(game.tour%2,faux_echequier)
        if not(est_echec):

            game.tour += 1
            game.pos_in_list = game.tour
            a_jouer = 0
            #Gère les pièces mangés
            if new[1] != 0:
                #Prise en passant
                if new[1] == "prise_passant_g_b":
                    mort = game.dico_piece_id[echequier[(pos_x-1,pos_y)]]
                    game.dico_mort["pn"] +=1
                    del echequier[(pos_x-1,pos_y)]
                elif new[1] == "prise_passant_d_b":
                    mort = game.dico_piece_id[echequier[(pos_x+1,pos_y)]]
                    game.dico_mort["pn"] +=1
                    del echequier[(pos_x+1,pos_y)]
                elif new[1] == "prise_passant_g_n":
                    mort = game.dico_piece_id[echequier[(pos_x-1,pos_y)]]
                    game.dico_mort["pb"] +=1
                    del echequier[(pos_x-1,pos_y)]
                elif new[1] == "prise_passant_d_n":
                    mort = game.dico_piece_id[echequier[(pos_x+1,pos_y)]]
                    game.dico_mort["pb"] +=1
                    del echequier[(pos_x+1,pos_y)]
                #Prise normal
                else:
                    mort = game.dico_piece_id[new[1]]
                    if mort in game.all_pions_blancs:
                        game.dico_mort["pb"] +=1
                    elif mort in game.all_pions_noirs:
                        game.dico_mort["pn"] +=1
                    elif mort in game.all_tours_noirs:
                        game.dico_mort["tn"] +=1
                    elif mort in game.all_tours_blancs:
                        game.dico_mort["tb"] +=1
                    elif mort in game.all_cavaliers_noirs:
                        game.dico_mort["cn"] +=1
                    elif mort in game.all_cavaliers_blancs:
                        game.dico_mort["cb"] +=1
                    elif mort in game.all_fous_noirs:
                        game.dico_mort["fn"] +=1
                    elif mort in game.all_fous_blancs:
                        game.dico_mort["fb"] +=1
                    elif mort in game.all_dames_noirs:
                        game.dico_mort["dn"] +=1
                    elif mort in game.all_dames_blancs:
                        game.dico_mort["db"] +=1
                game.all_pieces_mortes.add(mort)
                mort.remove()
                del echequier[(new_pos_x,new_pos_y)]
            del echequier[(pos_x,pos_y)]
            echequier[(new_pos_x,new_pos_y)] = piece_hand.get_id()
            #Réajuste parfaitement la piece dans la case
            for echequier_x in range(8):
                for echequier_y in range(8):
                    ajust_place = game.dico_piece_id[echequier[(echequier_x,echequier_y)]]
                    if ajust_place is not None:
                        ajust_place.rect.x = echequier_x*100
                        ajust_place.rect.y = echequier_y*100

            # Gère le rock blanc
            if piece_hand in game.all_rois_blancs:
                if  piece_hand.can_rock_blanc:
                    rock_blanc(game,echequier,piece_hand,new_pos_x,new_pos_y)
            #Gère le rock noir
            if piece_hand in game.all_rois_noirs:
                if piece_hand.can_rock_noir:
                    rock_noir(game,echequier,piece_hand,new_pos_x,new_pos_y)
                    
            #Gère le changement pion-dame blanc
            if piece_hand in game.all_pions_blancs:
                changement = game.change_blanc(piece_hand)
                if changement[0]:
                     game.dico_piece_id[game.n_pieces] = changement[1]
            #Gère le changement pion-dame noir
            if piece_hand in game.all_pions_noirs:
                changement = game.change_noir(piece_hand)
                if changement[0]:
                     game.dico_piece_id[game.n_pieces] = changement[1]
            
            game.update_echequier(echequier)
            #Vérifie si le joueur adverse est échec
            est_echec = game.is_echec((game.tour)%2,echequier)
            if est_echec:
                if game.is_mat(game.tour%2):
                    game.running = 1
            else:
                if not(game.edit):
                    if game.is_pat((game.tour)%2,echequier):
                        game.running = 1
                        game.tour = -1
                    if game.manque_materiel((game.tour)%2,echequier):
                        game.running = 1
                        game.tour = -2
                    if game.is_repeat():
                        game.running = 1
                        game.tour = -3
                    
            if game.tourne:
                echequier.turn()
            game.list_all_move_in_game.append(echequier.copy())

def Main(nicknamej1,nicknamej2,active_aide,profondeur,tourne_auto,nb_v_j1,nb_v_j2,edit,taille_ecran):
    
    #Modifie la résolution des images en fonction de la resolution de l'écran utilisateur
    new_l = taille_ecran[0]/1200
    new_c = taille_ecran[1]/800
    
    rapport = min(new_l,new_c)
    
    if rapport >= 1:
        rapport = 1
    
    if nb_v_j1 == 0 and nb_v_j2 == 0:
        testImgtaille = pygame.image.load("assets/pion_blanc.png")
        if not(int(100*rapport) - 3 < testImgtaille.get_rect().width < int(100*rapport) + 3):
            change_all(rapport)
    
    if profondeur == 0:
        profondeur = 1
    
    pygame.display.set_caption("Echec")
    screen = pygame.display.set_mode((int(1200*rapport),int(800*rapport)))
    #Charge les images
    background_principal = pygame.image.load("assets/echiquier.png")
    background_mort = pygame.image.load("assets/fond_mort.png")
    
    background_principal = pygame.transform.flip(background_principal,False,True)

    pion_blanc_mort = pygame.image.load("assets/morts/pion_blanc.png")
    pion_noir_mort = pygame.image.load("assets/morts/pion_noir.png")
    dame_blanc_mort = pygame.image.load("assets/morts/dame_blanc.png")
    cavalier_blanc_mort = pygame.image.load("assets/morts/cavalier_blanc.png")
    cavalier_noir_mort = pygame.image.load("assets/morts/cavalier_noir.png")
    dame_noir_mort = pygame.image.load("assets/morts/dame_noir.png")
    fou_blanc_mort = pygame.image.load("assets/morts/fou_blanc.png")
    fou_noir_mort = pygame.image.load("assets/morts/fou_noir.png")
    tour_blanc_mort = pygame.image.load("assets/morts/tour_blanc.png")
    tour_noir_mort = pygame.image.load("assets/morts/tour_noir.png")
    roi_blanc_mort = pygame.image.load("assets/morts/roi_blanc.png")
    roi_noir_mort = pygame.image.load("assets/morts/roi_noir.png")
    
    debut = pygame.image.load("assets/debut.png")

    #Charge les écritures
    font_pieces = pygame.font.Font(None,int(50*rapport))
    font_echec = pygame.font.Font(None,int(200*rapport))

    font_abandon =  pygame.font.Font(None,int(40*rapport))

    fond_nom_j1 = pygame.Surface((int(400*rapport),int(200*rapport)))
    fond_nom_j2 = pygame.Surface((int(400*rapport),int(200*rapport)))

    fond_nom_j1.fill((0,0,60))
    fond_nom_j2.fill((255,255,255))
    
    #Ajuste la police d'écriture des pseudos
    pseudo_j1 = "["+str(nb_v_j1)+"]  -  " + nicknamej1
    pseudo_j2 = "["+str(nb_v_j2)+"]  -  " + nicknamej2
    
    taille = 80
    font_nom = pygame.font.Font(None,taille)
    
    font_nom_j1 = font_nom.render(pseudo_j1+' 10',1,(255,255,255))
    font_nom_j2 = font_nom.render(pseudo_j2+' 10',1,(255,255,255))
    
    while font_nom_j1.get_rect().width > 380*rapport or font_nom_j2.get_rect().width > 380*rapport:
        taille -= 1
        font_nom = pygame.font.Font(None,taille)
        font_nom_j1 = font_nom.render(pseudo_j1+' 10',1,(255,255,255))
        font_nom_j2 = font_nom.render(pseudo_j2+' 10',1,(255,255,255))
    
    #Charge les objets utilent
    game = Game(profondeur,tourne_auto,edit,rapport)

    fleche_retour = Fleche_retour(game)
    fleche_avance = Fleche_avance(game)
    fleche_retour_n = Fleche_retour_n(game)
    fleche_avance_n = Fleche_avance_n(game)
    fleche_tourne = Fleche_tourne(game)

    #Charge les variables utilent
    mouse_down = False
    piece_hand = None
    touche_piece = False

    a_jouer = 0
    
    button_click = None

    echequier = game.get_echequier()
    echequier.turn()
    
    if edit:
        end_editing = False
        num = 1
        while not(end_editing):
            echequier = game.get_echequier()
            #Fait l'affichage
            screen.blit(background_principal,(0,0))
            screen.blit(background_mort,(int(800*rapport),0))
            
            screen.blit(debut,(int(900*rapport),int(350*rapport)))
            
            screen.blit(pion_blanc_mort,(int(801*rapport),int(25*rapport)))
            screen.blit(pion_noir_mort,(int(801*rapport),int(725*rapport)))
            
            screen.blit(dame_noir_mort,(int(934*rapport),int(725*rapport)))
            screen.blit(dame_blanc_mort,(int(934*rapport),int(25*rapport)))
            
            screen.blit(fou_blanc_mort,(int(1067*rapport),int(25*rapport)))
            screen.blit(fou_noir_mort,(int(1067*rapport),int(725*rapport)))
            
            screen.blit(cavalier_blanc_mort,(int(801*rapport),int(125*rapport)))
            screen.blit(cavalier_noir_mort,(int(801*rapport),int(625*rapport)))
            
            screen.blit(tour_blanc_mort,(int(934*rapport),int(125*rapport)))
            screen.blit(tour_noir_mort,(int(934*rapport),int(625*rapport)))
            
            screen.blit(roi_blanc_mort,(int(1067*rapport),int(125*rapport)))
            screen.blit(roi_noir_mort,(int(1067*rapport),int(625*rapport)))
            
            game.all_cavaliers_blancs.draw(screen)
            game.all_pions_blancs.draw(screen)
            game.all_tours_blancs.draw(screen)
            game.all_fous_blancs.draw(screen)
            game.all_rois_blancs.draw(screen)
            game.all_dames_blancs.draw(screen)
            
            game.all_cavaliers_noirs.draw(screen)
            game.all_pions_noirs.draw(screen)
            game.all_tours_noirs.draw(screen)
            game.all_fous_noirs.draw(screen)
            game.all_rois_noirs.draw(screen)
            game.all_dames_noirs.draw(screen)

            #Rafréchie la page
            pygame.display.flip()
            #Gère les events
            for event in pygame.event.get():
                #Si on quitte le jeu
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False,game.tour,nb_v_j1,nb_v_j2
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    if button_click == 1:
                        #Vérifie qu'on avait bien une pièce dans la main
                        if piece_hand is not None:
                            pos_souris = pygame.mouse.get_pos()
                            new_pos_x,new_pos_y = pos_souris
                            if new_pos_x < int(800*rapport) and new_pos_y < int(800*rapport):
                                new_pos_x //= int(100*rapport)
                                new_pos_y //= int(100*rapport)
                                
                                if piece_hand == "pion_blanc":
                                    game.ajoute_pion_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "tour_blanc":
                                    game.ajoute_tour_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "cavalier_blanc":
                                    game.ajoute_cavalier_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "fou_blanc":
                                    game.ajoute_fou_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "dame_blanc":
                                    game.ajoute_dame_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "roi_blanc":
                                    game.ajoute_roi_blanc(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "pion_noir":
                                    game.ajoute_pion_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "tour_noir":
                                    game.ajoute_tour_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "cavalier_noir":
                                    game.ajoute_cavalier_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "fou_noir":
                                    game.ajoute_fou_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "dame_noir":
                                    game.ajoute_dame_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                elif piece_hand == "roi_noir":
                                    game.ajoute_roi_noir(new_pos_x,new_pos_y,num)
                                    num += 1
                                
                                
                    mouse_down = False
                    button_click = 0
                    piece_hand = None
                            
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Permet de rentrer dans cette partie que la première fois où le boutton a été enfoncé
                    if not(mouse_down):
                        if event.button == 1:
                            mouse_down = True
                            button_click = 1
                            #Récupère la position de la souris
                            pos_souris = pygame.mouse.get_pos()
                            pos_x,pos_y = pos_souris[0],pos_souris[1]
                            
                            if int(900*rapport) <= pos_x <= int(1000*rapport) and int(350*rapport) <= pos_y <= int(450*rapport):
                                end_editing = True
                                game.recup_all_alive()
                                game.recup_all_id()
                                
                            elif int(801*rapport) <= pos_x <= int(851*rapport) and int(725*rapport) <= pos_y <= int(775*rapport) :
                                piece_hand = "pion_noir"
                            elif int(934*rapport) <= pos_x <= int(984*rapport) and int(625*rapport) <= pos_y <= int(675*rapport) :
                                piece_hand = "tour_noir"
                            elif int(801*rapport) <= pos_x <= int(951*rapport) and int(625*rapport) <= pos_y <= int(675*rapport) :
                                piece_hand = "cavalier_noir"
                            elif int(1067*rapport) <= pos_x <= int(1117*rapport) and int(625*rapport) <= pos_y <= int(675*rapport) :
                                piece_hand = "fou_noir"
                            elif int(934*rapport) <= pos_x <= int(984*rapport) and int(625*rapport) <= pos_y <= int(775*rapport) :
                                piece_hand = "dame_noir"
                            elif int(1067*rapport) <= pos_x <= int(1117*rapport) and int(625*rapport) <= pos_y <= int(675*rapport) :
                                piece_hand = "roi_noir"
                            
                            if int(801*rapport) <= pos_x <= int(851*rapport) and int(25*rapport) <= pos_y <= int(75*rapport) :
                                piece_hand = "pion_blanc"
                            elif int(934*rapport) <= pos_x <= int(984*rapport) and int(125*rapport) <= pos_y <= int(175*rapport) :
                                piece_hand = "tour_blanc"
                            elif int(801*rapport) <= pos_x <= int(901*rapport) and int(125*rapport) <= pos_y <= int(175*rapport) :
                                piece_hand = "cavalier_blanc"
                            elif int(1067*rapport) <= pos_x <= int(1117*rapport) and int(25*rapport) <= pos_y <= int(75*rapport) :
                                piece_hand = "fou_blanc"
                            elif int(934*rapport) <= pos_x <= int(984*rapport) and int(25*rapport) <= pos_y <= int(75*rapport) :
                                piece_hand = "dame_blanc"
                            elif int(1067*rapport) <= pos_x <= int(1117*rapport) and int(125*rapport) <= pos_y <= int(175*rapport) :
                                piece_hand = "roi_blanc"
                                
    
    game.list_all_move_in_game.append(echequier.copy())
    
    #Reset les variables utilent
    mouse_down = False
    piece_hand = None
    touche_piece = False

    a_jouer = 0
    
    button_click = None
    
    #Boucle de jeu
    while game.running < 3:

        echequier = game.get_echequier()

        if game.running >= 1:
            game.running += 1

        #Fait l'affichage
        screen.blit(background_principal,(0,0))
        screen.blit(background_mort,(int(800*rapport),0))

        font_pion_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["pb"]),1,(255,255,255))
        screen.blit(font_pion_blanc_morts,(int(851*rapport),int(35*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(pion_blanc_mort,(int(801*rapport),int(25*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        
        font_pion_noir_morts = font_pieces.render('x %d'%(game.dico_mort["pn"]),1,(0,0,0))
        screen.blit(font_pion_noir_morts,(int(851*rapport),int(735*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(pion_noir_mort,(int(801*rapport),int(725*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))   

        font_dame_noir_morts = font_pieces.render('x %d'%(game.dico_mort["dn"]),1,(0,0,0))
        screen.blit(font_dame_noir_morts,(int(984*rapport),int(735*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(dame_noir_mort,(int(934*rapport),int(725*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))

        font_dame_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["db"]),1,(255,255,255))
        screen.blit(font_dame_blanc_morts,(int(984*rapport),int(35*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(dame_blanc_mort,(int(934*rapport),int(25*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))

        font_fou_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["fb"]),1,(255,255,255))
        screen.blit(font_fou_blanc_morts,(int(1117*rapport),int(35*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(fou_blanc_mort,(int(1067*rapport),int(25*rapport)+(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        
        font_fou_noir_morts = font_pieces.render('x %d'%(game.dico_mort["fn"]),1,(0,0,0))
        screen.blit(font_fou_noir_morts,(int(1117*rapport),int(735*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(fou_noir_mort,(int(1067*rapport),int(725*rapport)-(int(700*rapport)*((game.tour)%2)*tourne_auto)))

        font_cavalier_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["cb"]),1,(255,255,255))
        screen.blit(font_cavalier_blanc_morts,(int(900*rapport),int(135*rapport)+(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(cavalier_blanc_mort,(int(850*rapport),int(125*rapport)+(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        
        font_cavalier_noir_morts = font_pieces.render('x %d'%(game.dico_mort["cn"]),1,(0,0,0))
        screen.blit(font_cavalier_noir_morts,(int(900*rapport),int(635*rapport)-(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(cavalier_noir_mort,(int(850*rapport),int(625*rapport)-(int(500*rapport)*((game.tour)%2)*tourne_auto)))

        font_tour_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["tb"]),1,(255,255,255))
        screen.blit(font_tour_blanc_morts,(int(1050*rapport),int(135*rapport)+(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(tour_blanc_mort,(int(1000*rapport),int(125*rapport)+(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        
        font_tour_noir_morts = font_pieces.render('x %d'%(game.dico_mort["tn"]),1,(0,0,0))
        screen.blit(font_tour_noir_morts,(int(1050*rapport),int(635*rapport)-(int(500*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(tour_noir_mort,(int(1000*rapport),int(625*rapport)-(int(500*rapport)*((game.tour)%2)*tourne_auto)))

        score_blanc = 0
        score_noir = 0

        affichage_score_blanc = ""
        affichage_score_noir = ""

        for i in game.all_pieces_mortes:
            if i.color == "noir":
                score_blanc += i.value
            else:
                score_noir += i.value

        if score_blanc > score_noir:
            affichage_score_blanc = "+ "+str(score_blanc-score_noir)
        elif score_blanc < score_noir:
            affichage_score_noir = "+ "+str(score_noir-score_blanc)
                

        font_nom_j1 = font_nom.render(pseudo_j1+' '+affichage_score_blanc,1,(255,255,255))
        font_nom_j2 = font_nom.render(pseudo_j2+" "+affichage_score_noir,1,(0,0,60))
        font_abandon_j1 = font_abandon.render("abandonner (blanc)",1,(255,255,255))
        font_abandon_j2 = font_abandon.render("abandonner (noir)",1,(0,0,0))
        
        
        screen.blit(fond_nom_j1,(int(800*rapport),int(400*rapport)-(int(200*rapport)*((game.tour)%2)*tourne_auto))) #arrière plan
        screen.blit(font_nom_j1,(int(800*rapport),int(455*rapport)-(int(100*rapport)*((game.tour)%2)*tourne_auto)-(taille//2))) #écriture
        
        screen.blit(fond_nom_j2,(int(800*rapport),int(200*rapport)+(int(200*rapport)*((game.tour)%2)*tourne_auto))) #arrière plan
        screen.blit(font_nom_j2,(int(800*rapport),int(355*rapport)+(int(100*rapport)*((game.tour)%2)*tourne_auto)-(taille//2))) #écriture
    
        screen.blit(font_abandon_j1,(int(820*rapport),int(560*rapport)-(int(340*rapport)*((game.tour)%2)*tourne_auto)))
        screen.blit(font_abandon_j2,(int(820*rapport),int(220*rapport)+(int(340*rapport)*((game.tour)%2)*tourne_auto)))

        if game.pos_in_list < game.tour:
            screen.blit(fleche_avance.image,(fleche_avance.rect.x,fleche_avance.rect.y))
        else:
            screen.blit(fleche_avance_n.image,(fleche_avance_n.rect.x,fleche_avance_n.rect.y))
        if game.pos_in_list != 0:
            screen.blit(fleche_retour.image,(fleche_retour.rect.x,fleche_retour.rect.y))
        else:
            screen.blit(fleche_retour_n.image,(fleche_retour_n.rect.x,fleche_retour_n.rect.y))
        screen.blit(fleche_tourne.image,(fleche_tourne.rect.x,fleche_tourne.rect.y))

        game.all_aides.draw(screen)

        #Gère si le joueur est un ordi
        
        if game.running == 0:
            if a_jouer == 5:
                if nicknamej2 == "Bot" and game.tour%2 == 1:
                    game.ordi_noir.set_echequier(echequier)
                    ancien,new = game.ordi_noir.choix_prof()
                    ancien_x,ancien_y = ancien
                    new_x,new_y = new
                    piece_id = echequier[ancien]
                    quand_a_jouer(game,game.dico_piece_id[piece_id],ancien_x,ancien_y,new_x,new_y)
                    a_jouer = 0

            if a_jouer == 5:
                if nicknamej1 == "Bot" and game.tour%2 == 0:
                    game.ordi_blanc.set_echequier(echequier)
                    joue = game.ordi_blanc.choix_prof()
                    ancien,new = game.ordi_noir.choix_prof()
                    ancien_x,ancien_y = ancien
                    new_x,new_y = new
                    piece_id = echequier[ancien]
                    quand_a_jouer(game,game.dico_piece_id[piece_id],ancien_x,ancien_y,new_x,new_y)
                    a_jouer = 0

            if a_jouer < 5:
                a_jouer += 1

        #Affiche les pièces de l'échequier
        for echequier_x in range(8):
            for echequier_y in range(8):
                piece = game.dico_piece_id[echequier[(echequier_x,echequier_y)]]
                if piece is not None:
                    if not(mouse_down):
                        piece.rect.x = echequier_x*int(100*rapport)
                        piece.rect.y = echequier_y*int(100*rapport)
                    screen.blit(piece.image,(piece.rect.x,piece.rect.y))
        #Affiche l'échec
        est_echec = game.is_echec((game.tour)%2,echequier)
        if est_echec and not(mouse_down):
            txt_echec = font_pieces.render('Echec !',1,(255,0,0))
            if game.tour%2 == 0:
                screen.blit(txt_echec,(int(800*rapport),int(280*rapport)))
            else:
                screen.blit(txt_echec,(int(800*rapport),int(500*rapport)))

        #Affiche le mouvement de la pièce quand on la joue                          
        if mouse_down and piece_hand is not None and touche_piece:
            x,y = pygame.mouse.get_pos()
            if x >= int(800*rapport) :
                x = int(800*rapport)
            if y >= int(800*rapport) :
                y = int(800*rapport)   
            piece_hand.set_pos(x-diff_x,y-diff_y)
            if active_aide:
                pos_possibles = piece_hand.recup_all_pos((pos_x,pos_y),echequier)
                for i in pos_possibles:
                    game.ajoute_aide(i[0]*int(100*rapport),i[1]*int(100*rapport))
        
        game.all_fleches_help.draw(screen)

        #Rafréchie la page
        pygame.display.flip()

        #Gère les events
        for event in pygame.event.get():
            #Si on quitte le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                return False,game.tour,nb_v_j1,nb_v_j2
            #Si une touche du clavier est enfoncée
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    echequier.turn()
            #Si un boutton de la souris est enfoncé
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Permet de rentrer dans cette partie que la première fois où le boutton a été enfoncé
                if not(mouse_down):
                    if event.button == 1:
                        game.remove_arrow()
                        mouse_down = True
                        button_click = 1
                        #Récupère la position de la souris
                        pos_souris = pygame.mouse.get_pos()
                        pos_x,pos_y = pos_souris[0]//int(100*rapport),pos_souris[1]//int(100*rapport)
                        #Si on a appuyé sur l'echequier
                        if pos_x <= 7 and pos_y <= 7 and game.tour == game.pos_in_list:
                            touche_piece = True
                            #Récupère la pièce touchée
                            piece_hand = game.dico_piece_id[echequier[(pos_x,pos_y)]]
                            if piece_hand is not None:
                                #Vérifie que la pièce est bien de la bonne couleur
                                if (piece_hand in game.all_blancs_alive and game.tour%2 == 0) or (piece_hand in game.all_noirs_alive and game.tour%2 == 1):
                                    #Récupère sa position
                                    diff_x,diff_y = pos_souris[0]-piece_hand.rect.x,pos_souris[1]-piece_hand.rect.y
                                else:
                                    piece_hand = None
                        #Si on a appuyé sur la flèche pour avancer          
                        if int(1120*rapport) <= pos_souris[0] <= int(1180*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                            if game.pos_in_list < game.tour:
                                game.update_echequier(game.list_all_move_in_game[game.pos_in_list+1])
                                game.pos_in_list += 1
                            touche_piece = False
                        #Si on a appuyé sur la flèche pour reculer
                        elif int(1020*rapport) <= pos_souris[0] <= int(1080*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                            if game.pos_in_list != 0:
                                game.update_echequier(game.list_all_move_in_game[game.pos_in_list-1])
                                game.pos_in_list -= 1
                            touche_piece = False
                        #Si le joueur blanc abandonne
                        elif int(820*rapport) <= pos_souris[0] <= int(1000*rapport)  and int(220*rapport) <= pos_souris[1] <=  int(260*rapport):
                            game.running = 1
                        #Si le joueur noir abandonne
                        elif int(820*rapport) <= pos_souris[0] <= int(1000*rapport)  and int(560*rapport) <= pos_souris[1] <=  int(600*rapport):
                            game.running = 1
                        #Si on a appuyé sur la flèche pour faire tourner l'échequier
                        elif int(920*rapport) <= pos_souris[0] <= int(980*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                            echequier.turn()
                            touche_piece = False
                            
                    elif event.button == 3:
                        mouse_down = True
                        button_click = 3
                        pos_souris = pygame.mouse.get_pos()
                        pos_x,pos_y = pos_souris[0]//int(100*rapport),pos_souris[1]//int(100*rapport)
                        
            #Si un boutton de la souris est soulevé
            elif event.type == pygame.MOUSEBUTTONUP:
                if button_click == 1:
                    #Vérifie qu'on avait bien une pièce dans la main
                    if touche_piece:
                        if piece_hand is not None:
                            #Vérifie que la pièce est bien de la bonne couleur
                            if not(x >= int(800*rapport) or y >=int(800*rapport)) and ((piece_hand.get_id() in game.all_id_blancs and game.tour%2 == 0)or(piece_hand.get_id() in game.all_id_noirs and game.tour%2 == 1)):
                                #Récupère la nouvelle position de la pièce est fait jouer
                                new_pos_x,new_pos_y = x//int(100*rapport),y//int(100*rapport)
                                quand_a_jouer(game,piece_hand,pos_x,pos_y,new_pos_x,new_pos_y)
                        #Efface les aides qui étaient présentent
                        if active_aide:
                            for i in game.all_aides:
                                i.remove()
                    #Reset des variables
                    mouse_down = False
                    touche_piece = False
                    a_jouer = 0
                elif button_click == 3:
                    x,y = pygame.mouse.get_pos()
                    if not(x >= int(800*rapport) or y >=int(800*rapport)):
                        new_pos_x,new_pos_y = x//int(100*rapport),y//int(100*rapport)
                        game.arrow((pos_x,pos_y),(new_pos_x,new_pos_y))
                    mouse_down = False
                    
    
    font_gagnant =  pygame.font.Font(None,int(50*rapport))
    veref = game.tour
    if veref >= 0:
        gagnant = veref%2
        if gagnant == 1:
            pseudo_gagnant = pseudo_j1
        else:
            pseudo_gagnant = pseudo_j2
    
        affichage_winner = font_gagnant.render("Bravo "+pseudo_gagnant+" !!!",1,(0,0,0))
        affichage_winner_rect = affichage_winner.get_rect()
        
        winner = win()
    
    else:
        if game.tour == -1:
            affichage_winner = font_gagnant.render("Il y a eu nul par pat...",1,(0,0,0))
        elif game.tour == -2:
            affichage_winner = font_gagnant.render("Il y a eu nul par manque de matériel...",1,(0,0,0))
        elif game.tour == -3:
            affichage_winner = font_gagnant.render("Il y a eu nul par répétition...",1,(0,0,0))
        affichage_winner_rect = affichage_winner.get_rect()
        
        winner = nul()
    
    affichage_rejouer = font_gagnant.render("Rejouer",1,(0,0,0))
    affichage_rejouer_rect = affichage_rejouer.get_rect()
    aff_win = True
    
    while True:
        
        echequier = game.get_echequier()
        
        screen.blit(background_principal,(0,0))
        screen.blit(background_mort,(int(int(800*rapport)*rapport),0))

        font_pion_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["pb"]),1,(255,255,255))
        screen.blit(font_pion_blanc_morts,(int(851*rapport),int(735*rapport)))
        screen.blit(pion_blanc_mort,(int(801*rapport),int(725*rapport)))
        
        font_pion_noir_morts = font_pieces.render('x %d'%(game.dico_mort["pn"]),1,(0,0,0))
        screen.blit(font_pion_noir_morts,(int(851*rapport),int(35*rapport)))
        screen.blit(pion_noir_mort,(int(801*rapport),int(25*rapport)))

        font_dame_noir_morts = font_pieces.render('x %d'%(game.dico_mort["dn"]),1,(0,0,0))
        screen.blit(font_dame_noir_morts,(int(984*rapport),int(35*rapport)))
        screen.blit(dame_noir_mort,(int(934*rapport),int(25*rapport)))

        font_dame_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["db"]),1,(255,255,255))
        screen.blit(font_dame_blanc_morts,(int(984*rapport),int(735*rapport)))
        screen.blit(dame_blanc_mort,(int(934*rapport),int(725*rapport)))

        font_fou_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["fb"]),1,(255,255,255))
        screen.blit(font_fou_blanc_morts,(int(1117*rapport),int(735*rapport)))
        screen.blit(fou_blanc_mort,(int(1067*rapport),int(725*rapport)))
        
        font_fou_noir_morts = font_pieces.render('x %d'%(game.dico_mort["fn"]),1,(0,0,0))
        screen.blit(font_fou_noir_morts,(int(1117*rapport),int(35*rapport)))
        screen.blit(fou_noir_mort,(int(1067*rapport),int(25*rapport)))

        font_cavalier_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["cb"]),1,(255,255,255))
        screen.blit(font_cavalier_blanc_morts,(int(900*rapport),int(635*rapport)))
        screen.blit(cavalier_blanc_mort,(int(850*rapport),int(625*rapport)))
        
        font_cavalier_noir_morts = font_pieces.render('x %d'%(game.dico_mort["cn"]),1,(0,0,0))
        screen.blit(font_cavalier_noir_morts,(int(900*rapport),int(135*rapport)))
        screen.blit(cavalier_noir_mort,(int(850*rapport),int(125*rapport)))

        font_tour_blanc_morts = font_pieces.render('x %d'%(game.dico_mort["tb"]),1,(255,255,255))
        screen.blit(font_tour_blanc_morts,(int(1050*rapport),int(635*rapport)))
        screen.blit(tour_blanc_mort,(int(1000*rapport),int(625*rapport)))
        
        font_tour_noir_morts = font_pieces.render('x %d'%(game.dico_mort["tn"]),1,(0,0,0))
        screen.blit(font_tour_noir_morts,(int(1050*rapport),int(135*rapport)))
        screen.blit(tour_noir_mort,(int(1000*rapport),int(125*rapport)))
        
        score_blanc = 0
        score_noir = 0

        affichage_score_blanc = ""
        affichage_score_noir = ""

        for i in game.all_pieces_mortes:
            if i.color == "noir":
                score_blanc += i.value
            else:
                score_noir += i.value

        if score_blanc > score_noir:
            affichage_score_blanc = "+ "+str(score_blanc-score_noir)
        elif score_blanc < score_noir:
            affichage_score_noir = "+ "+str(score_noir-score_blanc)
                

        font_nom_j1 = font_nom.render(pseudo_j1+' '+affichage_score_blanc,1,(255,255,255))
        screen.blit(fond_nom_j1,(int(800*rapport),int(200*rapport)))
        screen.blit(font_nom_j1,(int(800*rapport),int(355*rapport)-(taille//2)))

        font_nom_j2 = font_nom.render(pseudo_j2+" "+affichage_score_noir,1,(0,0,60))
        screen.blit(fond_nom_j2,(int(800*rapport),int(400*rapport)))
        screen.blit(font_nom_j2,(int(800*rapport),int(455*rapport)-(taille//2)))
        
        #Affiche les pièces de l'échequier
        for echequier_x in range(8):
            for echequier_y in range(8):
                piece = game.dico_piece_id[echequier[(echequier_x,echequier_y)]]
                if piece is not None:
                    if not(mouse_down):
                        piece.rect.x = echequier_x*int(100*rapport)
                        piece.rect.y = echequier_y*int(100*rapport)
                    screen.blit(piece.image,(piece.rect.x,piece.rect.y))
        
        if aff_win:
            screen.blit(winner.image,(winner.rect.x,winner.rect.y))
            screen.blit(affichage_winner,(int(400*rapport)-(affichage_winner_rect[2]//2),int(300*rapport)))
            screen.blit(affichage_rejouer,(int(400*rapport)-(affichage_rejouer_rect[2]//2),int(470*rapport)))
        else:
            if game.pos_in_list < game.tour:
                screen.blit(fleche_avance.image,(fleche_avance.rect.x,fleche_avance.rect.y))
            else:
                screen.blit(fleche_avance_n.image,(fleche_avance_n.rect.x,fleche_avance_n.rect.y))
            if game.pos_in_list != 0:
                screen.blit(fleche_retour.image,(fleche_retour.rect.x,fleche_retour.rect.y))
            else:
                screen.blit(fleche_retour_n.image,(fleche_retour_n.rect.x,fleche_retour_n.rect.y))
            screen.blit(fleche_tourne.image,(fleche_tourne.rect.x,fleche_tourne.rect.y))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            #Si on quitte le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                return False,game.tour,nb_v_j1,nb_v_j2
            #Si un boutton de la souris est enfoncé
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Récupère la position de la souris
                pos_souris = pygame.mouse.get_pos()
                pos_x,pos_y = pos_souris[0],pos_souris[1]
                if winner.rect.x + int(401*rapport) <= pos_x <= winner.rect.x + int(467*rapport) and winner.rect.y + int(11*rapport) <= pos_y <= winner.rect.y + int(77*rapport):
                    aff_win = False
                if int(400*rapport)-(affichage_rejouer_rect[2]//2) <= pos_x <= int(400*rapport)+(affichage_rejouer_rect[2]//2) and int(470*rapport)-(affichage_rejouer_rect[3]//2) <= pos_y <= int(470*rapport)+(affichage_rejouer_rect[3]//2):
                    pygame.quit()
                    return True,game.tour,nb_v_j1,nb_v_j2
                
                if not(aff_win):
                    #Si on a appuyé sur la flèche pour avancer          
                    if int(1120*rapport) <= pos_souris[0] <= int(1180*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                        if game.pos_in_list < game.tour:
                            game.update_echequier(game.list_all_move_in_game[game.pos_in_list+1])
                            game.pos_in_list += 1
                    #Si on a appuyé sur la flèche pour reculer
                    elif int(1020*rapport) <= pos_souris[0] <= int(1080*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                        if game.pos_in_list != 0:
                            game.update_echequier(game.list_all_move_in_game[game.pos_in_list-1])
                            game.pos_in_list -= 1
                    #Si on a appuyé sur la flèche pour faire tourner l'échequier
                    elif int(920*rapport) <= pos_souris[0] <= int(980*rapport)  and int(370*rapport) <= pos_souris[1] <=  int(430*rapport):
                        echequier.turn()

def luncher(pseudo_j1,pseudo_j2,active_aide,profondeur,tourne_auto,edit,taille_ecran):
    if profondeur == 0:
        profondeur = 1
    profondeur *= 2 #un coup = lui + moi
    pygame.init()
    a = Main(pseudo_j1,pseudo_j2,active_aide,profondeur,tourne_auto,0,0,edit,taille_ecran)
    while a[0]:
        pygame.init()
        if a[1] < 0:
            a = Main(pseudo_j1,pseudo_j2,active_aide,profondeur,tourne_auto,0.5+a[2],0.5+a[3],edit,taille_ecran)
        else:
            if a[1]%2 == 0:
                a = Main(pseudo_j1,pseudo_j2,active_aide,profondeur,tourne_auto,a[2],a[3]+1,edit,taille_ecran)
            else:
                a = Main(pseudo_j1,pseudo_j2,active_aide,profondeur,tourne_auto,a[2]+1,a[3],edit,taille_ecran)   
