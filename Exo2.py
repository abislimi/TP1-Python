#EXO2 IMPOT

#Renvoie les impots à payer en fct du revenu
def mesImpots(revenu):
    impot=-1
    if  0 <=revenu <= 10225:
        impot = 0
    elif 10226 <= revenu <= 26070:
        impot = (revenu - 10225) * 11/100
    elif 26071 <= revenu <= 74545 :
        impot = (revenu - 26070) * 30/100 + (26070-10226)*11/100
    elif 74546 <= revenu <= 160336:
        impot = (revenu-74545)*41/100 + (74545- 26070) * 30/100 + (26070-10226)*11/100
    elif revenu >= 160337:
        impot = (revenu-160336)*45/100 + (160336-74545)*41/100 + (74545- 26071) * 30/100 + (26070-10226)*11/100
    return int(impot)

#Test 
# print(mesImpots(20))
# print(mesImpots(20000))
# print(mesImpots(50000))
# print(mesImpots(100000))
# print(mesImpots(200000))
# print(mesImpots(-1100))


def f():
    revenu=int(input("Donner le montant de vos revenu :"))
    impot= mesImpots(revenu)
    print (f"Vous devez payer {impot}€ d'impôts")



#Test
#f()

