#EXO 1 CALENDRIER

#Cette fonction permet de renvoyer True si l'année est bisextile et false sinon.
def f_annee_bisex(annee):
    return (annee%4==0 and annee%100!=0 or annee%400==0)

#Test de la fonction

# print(f_annee_bisex(200))
# print(f_annee_bisex(2001))
# print(f_annee_bisex(2008))
# print(f_annee_bisex(2006))


#Cette fonction retourne le nb de jours dans un mois en fonction de l'année et du mois choisit
mois_long=[1,3,5,7,8,10,12]
mois_court=[4,6,9,11]

def f_nb_jours(mois,annee):
    nombre=-1
    if mois==2:
        if f_annee_bisex(annee):
            nombre=29
        else:
            nombre=28

    elif mois in mois_court:
        nombre=30
    
    elif mois in mois_long:
        nombre=31
    return nombre


#Test 
# print(f_nb_jours(4,2020))
# print(f_nb_jours(2,2008))
# print(f_nb_jours(2,200))
# print(f_nb_jours(3,2020))
# print(f_nb_jours(36,2020))
#print(f_nb_jours(10,2002))
    





def f_date_valid (jour,mois,annee):
    return (jour<=f_nb_jours(mois,annee) and jour>0)

#Test
# print(f_date_valid(30,10,2002))
# print(f_date_valid(-10,10,2002))
# print(f_date_valid(31,10,2002))
# print(f_date_valid(33,10,2002))
# print(f_date_valid(31,4,2002))
# print(f_date_valid(28,2,2002))
# print(f_date_valid(29,2,2002))
# print(f_date_valid(29,2,2000))



def f_date():
    jour=int(input("Entrez le jour :"))
    mois=int(input("Entrez le mois :"))
    annee=int(input("Entrez l'année :"))
    if f_date_valid (jour,mois,annee):
        print (f"Votre date {jour}/{mois}/{annee} est valide")
    else:
         print (f"Votre date {jour}/{mois}/{annee} n'est pas valide")


#Test
#f_date()


