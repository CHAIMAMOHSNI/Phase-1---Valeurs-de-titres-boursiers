import argparse
from datetime import date


def analyser_commande():

    parser = argparse.ArgumentParser("Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('-d --début', dest="date_debut", type=date, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    #parser.add_argument('-d --début', dest="date_debut", type=date, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f --fin', dest="date_fin", type=date, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('symbole', metavar="symbole", type=str, help="Nom d'un symbole boursier")
    parser.add_argument('-v --valeur', metavar="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="Nom d'un symbole boursier")
    args = parse.parse_args()
    return(parser.parse_args())



