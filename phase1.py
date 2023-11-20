#projet 1 : valeur des titres boursières :

import argparse
from datetime import datetime, date
import json
import requests


# d'après l'enoncé on a supposé que la date existe déjà (pas de date future donnée par l'utilisateur ) + je dois corriger les défauts de PEP8 (lignes trop longues)
def analyser_commande():
    # la fonction suivante permet de prendre en consideration des données ( qui seront donnés par l'utlisateur) 
    # retourne des résultats (données historiques de marché boursier pour un ou plusieurs symboles boursiers.)

    parser = argparse.ArgumentParser(
        description = "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers."
        )

    parser.add_argument(
        '-d', '--début',
        metavar='DATE' ,
        dest= "debut",
        type=str,
        default= "fin",
        help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)',
    )
    
    parser.add_argument(
        '-f', '--fin',
        metavar='DATE' ,
        dest= "datefin",
        type=str, 
        default= str(date.today()), 
        help='Date recherchée la plus récente (format: AAAA-MM-JJ)'
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
        help="la valeur désirée(par défaut : fermeture)",
        )
    return parser.parse_args()

def produire_historique(symbole, debut: date, datefin: date, valeur):
    # la fonction permet de produire l'historique complet d'une valeur boursière à partir d'un ou plusieurs symboles , la date ...

    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    liste = []

    params1 = {'début': debut.strftime("%Y-%m-%d"), 'fin': datefin.strftime("%Y-%m-%d")}
    réponse = requests.get(url=url, params=params1)
    dic = json.loads(réponse.text)
    historique = dic['historique']

    print(f'titre ={symbole}: valeur={valeur}, début={début}, fin={fin}')
    for dates, vals in historique.items():
        msg = datetime.strptime(ates, '%Y-%m-%d').date(), vals[valeur]
        liste.append(msg) 
    print(reversed(liste)) #puisque la liste sort en ordre décroissant 

#Programme principal:

if __name__ == "__main__":
    analyse = analyser_commande()
    result = []
    if analyse.debut is None:
        analyse.debut = analyse.datefin
    
    for symb in analyse.symbole:
        données = produire_historique(symbole, analyse.début, analyse.fin, analyse.valeur)
        result.append((date, données))
    