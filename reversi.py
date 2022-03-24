# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:47:04 2021

@author: Arthur
"""
import turtle


lettres = ['a','b','c','d','e','f','g','h']

#on transforme la lettre a en l'entier j, le numéro de colonne correspond à la lettre a
#si ce n'est pas une lettre, il renvoie une erreur.
def transforme(a):
    for i in range(8):
        if lettres[i] == a:
            return i
    print("erreur,",a,"ne convient pas")


#i = ligne (chiffre)
#j = colonne (lettre)


#j1 est le nom du joueur n°1, joueur est celui du joueur en train de jouer son tour
#plateau est un tableau contenant toute les informations du plateau de jeu 
#(des "X" sur les cases prises par le joueur n°1, et des "O" sur celle du joueur 2, des "_" sinon)
#compteur contient les scores à ce moment de la partie
def jouer_un_tour(joueur,j1,plateau,compteur):
    print("C'est à",joueur)
    r = input("Quelle case ? ")
    if len(r) != 2 or type(transforme(r[0])) != int:
        print("Ce n'est pas le nom d'une case !!")
        jouer_un_tour(joueur,j1,plateau,compteur)
    else:
        i = transforme(r[0])
        j = int(r[1])
        if plateau[i*8+j] != "_":
            print("Cette case est prise !!")
            jouer_un_tour(joueur,j1,plateau,compteur)
        else:
            if joueur == j1:
                if not case_interdite("X","O",i,j,plateau):
                    affiche(plateau,i,j,"X","O",compteur)
                    plateau[i*8+j] = "X"
                    check_ligne(i,j,"X","O",plateau)
                    check_colone(i,j,"X","O",plateau)
                    check_diago(i,j,"X","O",plateau)
                else:
                    print("Cette case n'est pas jouable!")
                    jouer_un_tour(joueur,j1,plateau,compteur)
            else:
                if not case_interdite("O","X",i,j,plateau):
                    affiche(plateau,i,j,"O","X",compteur)
                    plateau[i*8+j] = "O"
                    check_ligne(i,j,"O","X",plateau)
                    check_colone(i,j,"O","X",plateau)
                    check_diago(i,j,"O","X",plateau)
                else:
                    print("Cette case n'est pas jouable!")
                    jouer_un_tour(joueur,j1,plateau,compteur)
    

def affiche(plateau,i,j,X,O,compteur):
    #X est la couleur de jeton du joueur qui vient de jouer
    r = i*8+j
    E = []
    for k in plateau:
        E.append(k)
    E[r] = X
    check_ligne(i,j,X,O,E)
    check_colone(i,j,X,O,E)
    check_diago(i,j,X,O,E)
    for k in range(len(plateau)):
        i = k//8
        j = k%8
        if plateau[k] != E[k]:
            affiche_piece(i,j,X)
            if E[k] == 'X':
                compteur[0] += 1
                compteur[1] -= 1
            else:
                compteur[0] -= 1
                compteur[1] += 1
    if X == 'X':
        compteur[1] += 1
    else:
        compteur[0] += 1     


def check_ligne(i,j,X,O,plateau):
    #X est la couleur de jeton du joueur qui vient de jouer
    r = i*8+j
    gauche = i*8+j
    droite = i*8+j
    
    #gauche
    controle = 0
    if j != 0:
        gauche -= 1
        while plateau[gauche] == O:
            if gauche > i*8:
                gauche -= 1
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[gauche] == X:
                for k in range(gauche+1,r):
                    plateau[k] = X                
    #droite
    controle = 0
    if j != 7:
        droite += 1
        while plateau[droite] == O:
            if droite < (i+1)*8-1:
                droite += 1
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[droite] == X:
                for k in range(r+1,droite):
                    plateau[k] = X
    

def check_colone(i,j,X,O,plateau):
    #X est la couleur de jeton du joueur qui vient de jouer
    r = i*8+j
    haut = i*8+j
    bas = i*8+j
    
    #bas
    controle = 0
    if i != 0:
        bas -= 8
        while plateau[bas] == O:
            if bas > j:
                bas -= 8
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[bas] == X:
                for k in range(bas+8,r,8):
                    plateau[k] = X             
    #haut
    controle = 0
    if i != 7:
        haut += 8
        while plateau[haut] == O:
            if haut < j+7*8:
                haut += 8
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[haut] == X:
                for k in range(r+8,haut,8):
                    plateau[k] = X
                    

def check_diago(i,j,X,O,plateau):
    #X est la couleur de jeton du joueur qui vient de jouer
    r = i*8+j
    haut_gauche = i*8+j
    bas_droite = i*8+j
    haut_droite = i*8+j
    bas_gauche = i*8+j
    
    #haut_gauche
    controle = 0
    if j != 0 and i != 0:
        haut_gauche -= 9
        while plateau[haut_gauche] == O:
            if haut_gauche%8 != 0 and haut_gauche//8 != 0:
                haut_gauche -= 9
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[haut_gauche] == X:
                for k in range(haut_gauche+9,r,9):
                    plateau[k] = X                
    #bas_droite
    controle = 0
    if j != 7 and i != 7:
        bas_droite += 9
        while plateau[bas_droite] == O:
            if bas_droite//8 != 7 and bas_droite%8 != 7:
                bas_droite += 9
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[bas_droite] == X:
                for k in range(r+9,bas_droite,9):
                    plateau[k] = X                
    #haut_droite
    controle = 0
    if j != 7 and i != 0:
        haut_droite -= 7
        while plateau[haut_droite] == O:
            if haut_droite%8 != 7 and haut_droite//8 != 0:
                haut_droite -= 7
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[haut_droite] == X:
                for k in range(haut_droite+7,r,7):
                    plateau[k] = X             
    #bas_gauche
    controle = 0
    if j != 0 and i != 7:
        bas_gauche += 7
        while plateau[bas_gauche] == O:
            if bas_gauche%8 != 0 and bas_gauche//8 != 7:
                bas_gauche += 7
                controle = 1
            else:
                break
        if controle == 1 :
            if plateau[bas_gauche] == X:
                for k in range(r+7,bas_gauche,7):
                    plateau[k] = X


def case_interdite(X,O,i,j,plateau):
    #X est la couleur de jeton du joueur qui vient de jouer
    r = i*8+j
    if plateau[r] != "_":
        return True
    else:
        E = []
        for k in plateau:
            E.append(k)
        E[r] = X
        check_ligne(i,j,X,O,E)
        check_colone(i,j,X,O,E)
        check_diago(i,j,X,O,E)
        E[r] = "_"
        return E == plateau
        

#dessin du plateau avec turtle
def affiche_plateau():
    turtle.clear()
    turtle.penup()
    turtle.goto(-250,250)
    for k in range (4):
        turtle.pendown()
        turtle.fd(500)
        turtle.penup()
        turtle.rt(90)
        turtle.fd(62.5)
        turtle.rt(90)
        turtle.pendown()
        turtle.fd(500)
        turtle.penup()
        turtle.rt(-90)
        turtle.fd(62.5)
        turtle.rt(-90)
    turtle.pendown()
    turtle.fd(500)
    turtle.penup()
    turtle.goto(250,250)
    turtle.rt(90)
    for k in range (4):
        turtle.pendown()
        turtle.fd(500)
        turtle.penup()
        turtle.rt(90)
        turtle.fd(62.5)
        turtle.rt(90)
        turtle.pendown()
        turtle.fd(500)
        turtle.penup()
        turtle.rt(-90)
        turtle.fd(62.5)
        turtle.rt(-90)
    turtle.pendown()
    turtle.fd(500)
    turtle.penup()


def affiche_indices():
    for i in range(8):
        turtle.goto(-281.25,190-62.5*i)
        turtle.write(lettres[i],align = "center",font = ("Arial", 30, "normal"))
    for i in range(8):
        turtle.goto(-218.75+62.5*i,255)
        turtle.write(i,align = "center",font = ("Arial", 30, "normal"))
           
    
def affiche_piece(i,j,X):
    #X la couleur du jeton qui vient d'être joué
    x =- 218.75+62.5*j
    y = 218.75-62.5*i
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    if X == 'X':
        turtle.dot(45,'blue')
    else:
        turtle.dot(45,'red')


def affiche_score(j1,j2,compteur):
    turtle.penup()
    turtle.goto(450,27)
    turtle.pendown()
    turtle.dot(295,'white')
    
    turtle.penup()
    turtle.goto(290,50)
    turtle.pendown()
    turtle.write(j1+" : "+str(compteur[0]),font = ("Arial", 30, "normal"))
    
    turtle.penup()
    turtle.goto(290,-50)
    turtle.pendown()
    turtle.write(j2+" : "+str(compteur[1]),font = ("Arial", 30, "normal"))


def a_perdu(j,j1,plateau):
    if j == j1 :
        for i in range(64):
            if plateau[i] == "X":
                return False
        return True
    else:
        for i in range(64):
            if plateau[i] == "O":
                return False
        return True


def copie(t0):
    t = []
    for i in range(len(t0)):
        t.append(t0[i])
    return t


#si j n'a aucun coup possible, on doit sauter son tour
def peut_jouer(j,j1,plateau):
    if j == j1:
        for n in range(64):
            t = copie(plateau)
            y = n%8
            x = n//8
            if not case_interdite("X","O",x,y,t):
                return True
    else:
        for n in range(64):
            t = copie(plateau)
            y = n%8
            x = n//8
            if not case_interdite("O","X",x,y,t):
                return True
    return False


def reversi():
    compteur = [2,2]
    turtle.setworldcoordinates(-300, -400, 600, 400)
    turtle.ht()
    affiche_plateau()
    affiche_indices()
    affiche_piece(3,3,"X")
    affiche_piece(4,4,"X")
    affiche_piece(3,4,"O")
    affiche_piece(4,3,"O")
    plateau = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","X","O","_","_","_","_","_","_","O","X","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
    print("Bienvenue dans reversi, le joueur 1 jouera en bleu et le joueur 2 en rouge")
    j1 = input("Qui sera le joueur 1 ? (choisir un nom/pseudonyme de moins 6 lettres) : ")
    j2 = input("Qui sera le joueur 2 ? (choisir un nom/pseudonyme de moins 6 lettres) : ")
    affiche_score(j1,j2,compteur)
    c = 0
    for i in range(60): #a priori il y aura 60 coups car 60 case libre
        if c == 0 :
            if peut_jouer(j1,j1,plateau):
                c = 1
                jouer_un_tour(j1,j1,plateau,compteur)
                affiche_score(j1,j2,compteur)
                if a_perdu(j2,j1,plateau):
                    print("Félicitation joueur 1 !!")
                    return ()
            elif peut_jouer(j2,j1,plateau):
                jouer_un_tour(j2,j1,plateau,compteur)
                affiche_score(j1,j2,compteur)
                if a_perdu(j1,j1,plateau):
                    print("Félicitation joueur 2 !!")
                    return ()
            else :
                if compteur[0] > compteur[1]:
                    print("Félicitation joueur 1 !!")
                    return ()
                elif compteur[1] > compteur[0]:
                    print("Félicitation joueur 2 !!")
                    return ()
                else:
                    return "Parfaite égalité, félicitation à vous deux!!"
        else :
            if peut_jouer(j2,j1,plateau):
                c=0
                jouer_un_tour(j2,j1,plateau,compteur)
                affiche_score(j1,j2,compteur)
                if a_perdu(j1,j1,plateau):
                    print("Félicitation joueur 2 !!")
                    return ()
            elif peut_jouer(j1,j1,plateau):
                jouer_un_tour(j1,j1,plateau,compteur)
                affiche_score(j1,j2,compteur)
                if a_perdu(j2,j1,plateau):
                    print("Félicitation joueur 1 !!")
                    return ()
            else :
                if compteur[0] > compteur[1]:
                    print("Félicitation joueur 1 !!")
                    return ()
                elif compteur[1] > compteur[0]:
                    print("Félicitation joueur 2 !!")
                    return ()
                else:
                    print("Parfaite égalité, félicitation à vous deux!!")
                    return ()
    if compteur[0] > compteur[1]:
        print("Félicitation joueur 1 !!")
        return ()
    elif compteur[1] > compteur[0]:
        print("Félicitation joueur 2 !!")
        return ()
    else:
        print("Parfaite égalité, félicitation à vous deux!!")
        return ()


reversi()