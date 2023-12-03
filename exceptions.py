class ErreurDate(RuntimeError):

    def __init__(self, message="la date spécifiée est postérieure à la date du jour!"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return str(self.message)
    
class ErreurQuantite(RuntimeError):

    def __init__(self, message="le portefeuille ne possède pas suffisamment d'actions de ce titre!"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return str(self.message)

class LiquiditeInsuffisante(RuntimeError):

    def __init__(self, message ="le portefeuille ne contient pas suffisamment de liquidités!"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return str(self.message)