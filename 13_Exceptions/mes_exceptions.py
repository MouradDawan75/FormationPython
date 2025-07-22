class AucunChiffreException(Exception):

    def __str__(self):
        return "Exception aucun chiffre. Le paramètre fournit n'est pas valide"