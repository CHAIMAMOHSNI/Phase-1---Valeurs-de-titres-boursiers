#projet 1 : valeur des titres boursières :

import argparse
import requests
import datetime
from datetime import date
import json

# d'après l'enoncé on a supposé que la date existe déjà (pas de date future donnée par l'utilisateur ) + je dois corriger les défauts de PEP8 (lignes trop longues)
def analyser_commande():
    parser = argparse.ArgumentParser(
        description = "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers."
    )

    parser.add_argument(
        '-d', '--début',
        metavar='DATE' ,
        dest= "début",
        type=date,
        default= "fin",
        help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)',
    )
    
    parser.add_argument(
        '-f', '--fin',
        metavar='DATE' ,
        dest= "fin",
        type=date, 
        default= date.today() , 
        help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)'
    )

    parser.add_argument(
        'symbole',
        nargs='+',
        help="Nom d'un symbole boursier",
        )
    
    parser.add_argument(
        '-v ', '--valeur',
        dest='valeur',
        choices=["fermeture", "ouverture", "min", "max", "volume"],
        default="fermeture",
        help="Nom d'un symbole boursier",
        )
    return parser.parse_args()

def produire_historique(symbole, début, fin, valeur):
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    liste = []

    params1 = {'début': début, 'fin': fin}
    réponse = requests.get(url=url, params=params1)
    dic = json.loads(réponse.text)
    historique = dic['historique']
    print(f'titre ={symbole}: valeur={valeur}, début={début}, fin={fin}')
    for dates, vals in historique.keys():
        msg = datetime.strptime(dates, '%Y-%m-%d').date(), vals.get(valeur,'message d\'erreur')
        liste.append(msg)  
    return liste

#Programme principal:

analyse = analyser_commande()
result = []
for symbole in analyse.symbole:
    données = produire_historique(symbole, analyse.début, analyse.fin, analyse.valeur)
    result.append((symbole, données))
 