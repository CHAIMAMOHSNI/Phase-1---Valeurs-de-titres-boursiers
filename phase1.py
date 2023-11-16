import argparse
import requests
from datetime import date


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('-h ', action="help", help='show this help message and exit')
    parser.add_argument('-d ', metavar= "DATE" ,dest= "début", type=date, default= "date_de_fin", help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f ', metavar="DATE" , dest= "fin", type=date, default= date.today() , help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('symbole', nargs='+' ,type=str, help="Nom d'un symbole boursier")
    parser.add_argument('-v ', dest="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="Nom d'un symbole boursier")
    return parser.parse_args()

def produire_historique (symbole, début, fin, v = fermeture):

    url = f"https://example.com/api/historique?symbole={nom_symbole}&debut={date_debut}&fin={date_fin}"

    try:
        response = requests.get(url)
            if valeur_desiree in historique:
                return [(entry['date'], entry[valeur_desiree]) for entry in historique[valeur_desiree]]
            else:
                print(f"La valeur '{valeur_desiree}' n'est pas disponible dans l'historique.")
                return None



