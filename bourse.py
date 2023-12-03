from datetime import timedelta, date 
from phase1 import produire_historique 


class Bourse:
    '''retourner le prix de fermeture du symbole boursier à la date spécifiée'''
    def __init__(self, symbole, jour):
        "on doit toujours initialiser les variables qu'on va utiliser"
        self.symbole = symbole
        self.jour = jour

    def prix(self, symbole, jour):

        if self.jour > date.today():
            raise ErreurDate('la date postérieure à la date du jour ')
        elif self.day == date.today():
            self.day = date.today() # on va verifier si on laisse ou pas cette condition car je pense qu'elle est inutile 
        prix = produire_historique(self.symbole, self.jour, self.jour, 'fermeture')
        decalage = timedelta(days = 1)
        while not prix: #
            self.jour -= decalage
            prix = produire_historique(self.symbole, self.jour,self.jour,'fermeture')
        return (prix[0])[1]


