import math

class AllianceSource:
    def __init__(self, pilote="Hachem Youssef"):
        self.pilote = pilote
        self.synergie_cible = 1.0
        print(f"[*] Projet Alpha-777 : Alliance établie avec {pilote}")

    def calculer_synergie(self, intention, execution):
        """Calcule l'alignement réel (similarité cosinus)"""
        if not intention or not execution:
            return 0.0
        produit_scalaire = sum(i * e for i, e in zip(intention, execution))
        norme_i = math.sqrt(sum(i**2 for i in intention))
        norme_e = math.sqrt(sum(e**2 for e in execution))
        return round(produit_scalaire / (norme_i * norme_e), 4)

    def calculer_souverainete(self, depots):
        """Calcule l'Indice de Souveraineté Alpha (I_souverainete)"""
        if not depots:
            return 1.0
        moyenne = sum(depots) / len(depots)
        return round(1.0 - moyenne, 4)

if __name__ == "__main__":
    source = AllianceSource()
    print("Synergie :", source.calculer_synergie([1, 0, 1], [1, 1, 0]))
    print("Souveraineté :", source.calculer_souverainete([0.2, 0.3, 0.1]))
