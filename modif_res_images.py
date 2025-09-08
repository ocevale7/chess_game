from PIL import Image
import numpy as np

from class_fou_blanc import fou_blanc

def save_im(nom, im):
    im.save(nom)

def change_all(rapport):
    
    tour_b = la_modif("assets/_tour_blanche.png",(int(100*rapport),int(100*rapport)))
    tour_n = la_modif("assets/_tour_noire.png",(int(100*rapport),int(100*rapport)))
    fou_b = la_modif("assets/_fou_blanc.png",(int(100*rapport),int(100*rapport)))
    fou_n = la_modif("assets/_fou_noir.png",(int(100*rapport),int(100*rapport)))
    cavalier_b = la_modif("assets/_cavalier_blanc.png",(int(100*rapport),int(100*rapport)))
    cavalier_n = la_modif("assets/_cavalier_noir.png",(int(100*rapport),int(100*rapport)))
    pion_b = la_modif("assets/_pion_blanc.png",(int(100*rapport),int(100*rapport)))
    pion_n = la_modif("assets/_pion_noir.png",(int(100*rapport),int(100*rapport)))
    roi_b = la_modif("assets/_roi_blanc.png",(int(100*rapport),int(100*rapport)))
    roi_n = la_modif("assets/_roi_noir.png",(int(100*rapport),int(100*rapport)))
    dame_b = la_modif("assets/_dame_blanche.png",(int(100*rapport),int(100*rapport)))
    dame_n = la_modif("assets/_dame_noire.png",(int(100*rapport),int(100*rapport)))
    
    tour_bm = la_modif("assets/morts/_tour_blanc.png",(int(50*rapport),int(50*rapport)))
    tour_nm = la_modif("assets/morts/_tour_noir.png",(int(50*rapport),int(50*rapport)))
    fou_bm = la_modif("assets/morts/_fou_blanc.png",(int(50*rapport),int(50*rapport)))
    fou_nm = la_modif("assets/morts/_fou_noir.png",(int(50*rapport),int(50*rapport)))
    cavalier_bm = la_modif("assets/morts/_cavalier_blanc.png",(int(50*rapport),int(50*rapport)))
    cavalier_nm = la_modif("assets/morts/_cavalier_noir.png",(int(50*rapport),int(50*rapport)))
    pion_bm = la_modif("assets/morts/_pion_blanc.png",(int(50*rapport),int(50*rapport)))
    pion_nm = la_modif("assets/morts/_pion_noir.png",(int(50*rapport),int(50*rapport)))
    roi_bm = la_modif("assets/morts/_roi_blanc.png",(int(50*rapport),int(50*rapport)))
    roi_nm = la_modif("assets/morts/_roi_noir.png",(int(50*rapport),int(50*rapport)))
    dame_bm = la_modif("assets/morts/_dame_blanc.png",(int(50*rapport),int(50*rapport)))
    dame_nm = la_modif("assets/morts/_dame_noir.png",(int(50*rapport),int(50*rapport)))
    
    nulle = la_modif("assets/_nulle.png",(int(500*rapport),int(500*rapport)))
    millieu_fleche = la_modif("assets/_milieu_fleche.png",(int(100*rapport),int(100*rapport)))
    gagnant = la_modif("assets/_gagnant.png",(int(500*rapport),int(500*rapport)))
    fleche_tourne = la_modif("assets/_fleche_tourne.png",(int(60*rapport),int(60*rapport)))
    fleche_right = la_modif("assets/_fleche_right.png",(int(60*rapport),int(60*rapport)))
    fleche_right_n = la_modif("assets/_fleche_right_n.png",(int(60*rapport),int(60*rapport)))
    fleche_left = la_modif("assets/_fleche_left.png",(int(60*rapport),int(60*rapport)))
    fleche_left_n = la_modif("assets/_fleche_left_n.png",(int(60*rapport),int(60*rapport)))
    fin_fleche = la_modif("assets/_fin_fleche.png",(int(100*rapport),int(100*rapport)))
    debut_fleche = la_modif("assets/_debut_fleche.png",(int(100*rapport),int(100*rapport)))
    debut = la_modif("assets/_debut.png",(int(200*rapport),int(200*rapport)))
    case = la_modif("assets/_case.png",(int(100*rapport),int(100*rapport)))
    angle_fleche = la_modif("assets/_angle_fleche.png",(int(100*rapport),int(100*rapport)))
    aide = la_modif("assets/_aide.png",(int(100*rapport),int(100*rapport)))
    fond_mort = la_modif("assets/_fond_mort.png",(int(800*rapport),int(800*rapport)))
    echiquier = la_modif("assets/_echiquier.png",(int(800*rapport),int(800*rapport)))
    print(echiquier,tour_bm)
    
    save_im("assets/tour_blanche.png",tour_b)
    save_im("assets/tour_noire.png",tour_n)
    save_im("assets/fou_blanc.png",fou_b)
    save_im("assets/fou_noir.png",fou_n)
    save_im("assets/cavalier_blanc.png",cavalier_b)
    save_im("assets/cavalier_noir.png",cavalier_n)
    save_im("assets/pion_blanc.png",pion_b)
    save_im("assets/pion_noir.png",pion_n)
    save_im("assets/roi_blanc.png",roi_b)
    save_im("assets/roi_noir.png",roi_n)
    save_im("assets/dame_blanche.png",dame_b)
    save_im("assets/dame_noire.png",dame_n)
    
    save_im("assets/morts/tour_blanc.png",tour_bm)
    save_im("assets/morts/tour_noir.png",tour_nm)
    save_im("assets/morts/fou_blanc.png",fou_bm)
    save_im("assets/morts/fou_noir.png",fou_nm)
    save_im("assets/morts/cavalier_blanc.png",cavalier_bm)
    save_im("assets/morts/cavalier_noir.png",cavalier_nm)
    save_im("assets/morts/pion_blanc.png",pion_bm)
    save_im("assets/morts/pion_noir.png",pion_nm)
    save_im("assets/morts/roi_blanc.png",roi_bm)
    save_im("assets/morts/roi_noir.png",roi_nm)
    save_im("assets/morts/dame_blanc.png",dame_bm)
    save_im("assets/morts/dame_noir.png",dame_nm)
    
    save_im("assets/nulle.png",nulle)
    save_im("assets/milieu_fleche.png",millieu_fleche)
    save_im("assets/gagnant.png",gagnant)
    save_im("assets/fleche_tourne.png",fleche_tourne)
    save_im("assets/fleche_right.png",fleche_right)
    save_im("assets/fleche_right_n.png",fleche_right_n)
    save_im("assets/fleche_left.png",fleche_left)
    save_im("assets/fleche_left_n.png",fleche_left_n)
    save_im("assets/fin_fleche.png",fin_fleche)
    save_im("assets/debut_fleche.png",debut_fleche)
    save_im("assets/debut.png",debut)
    save_im("assets/case.png",case)
    save_im("assets/angle_fleche.png",angle_fleche)
    save_im("assets/aide.png",aide)
    save_im("assets/fond_mort.png",fond_mort)
    save_im("assets/echiquier.png",echiquier)

def la_modif(image_name:str,new_range:int):
    im = Image.open(image_name)
    new = im.resize(new_range)
    return new

if __name__ == '__main__':
    new_l = 1366/1200
    new_c = 768/800
    rapport = min(new_l,new_c)
    
    new_img = la_modif("assets/echiquier.png",(int(800*rapport),int(800*rapport)))
    new_img.save('_fou_noir.png')