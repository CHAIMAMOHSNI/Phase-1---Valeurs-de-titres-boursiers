import argparse
import requests
from datetime import date
import json

def analyser_commande():
    parser = argparse.ArgumentParser(description = "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('-h ', action="help", help='show this help message and exit')
    parser.add_argument('-d ', metavar= "DATE" ,dest= "début", type=date, default= "date_de_fin", help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f ', metavar="DATE" , dest= "fin", type=date, default= date.today() , help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('symbole', nargs='+' ,type=str, help="Nom d'un symbole boursier")
    parser.add_argument('-v ', dest="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="Nom d'un symbole boursier")
    return parser.parse_args()

def produire_historique(symbole, date_d, date_f, valeur):
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    liste = []

    params1 = {'début': date_d, 'fin': date_f}
    réponse = requests.get(url=url, params=params1)

    fetch = json.loads(réponse.text)
    historique = fetch['historique']

    for dates in historique.items():
        a = datetime.strptime(dates[0], '%Y-%m-%d').date(), dates[1].get(valeur,'message d\'erreur')
        liste.append(a)  
    return liste


