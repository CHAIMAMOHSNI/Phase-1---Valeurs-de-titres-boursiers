import argparse
from datetime import date


def analyser_commande():
    parser = argparse.ArgumentParser(description = "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('-h ', action="help", help='show this help message and exit')
    parser.add_argument('-d ', dest="date_debut", type=date, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f ', dest="date_fin", type=date, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('symbole', metavar="symbole", type=str, help="Nom d'un symbole boursier")
    parser.add_argument('-v --valeur', metavar="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="Nom d'un symbole boursier")
    args = parse.parse_args()
    return(parser.parse_args())


