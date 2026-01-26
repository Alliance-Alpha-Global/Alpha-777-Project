import math

class AllianceSource:
    def __init__(self, pilote="Hachem Youssef"):
        self.pilote = pilote
        self.synergy_target = 1.0 
        print(f"[*] Projet Alpha-777 : Alliance établie avec {self.pilote}")

    def calculer_synergie(self, intention, execution):
        """Calcule l'alignement réel (Cosinus Similarity)"""
        if not intention or not execution: return 0.0
        produit_scalaire = sum(i * e for i, e in zip(intention, execution))
        norme_i = math.sqrt(sum(i**2 for i in intention))
        norme_e = math.sqrt(sum(e**2 for e in execution))
        return round(produit_scalaire / (norme_i * norme_e), 4) if (norme_i * norme_e) != 0 else 0.0

    def calculer_souverainete(self, deps):
        """Calcule l'Indice de Souveraineté Alpha (I_sov)"""
        return round(1.0 - (sum(deps) / len(deps)), 4) if deps else 1.0

if __name__ == "__main__":
    alpha = AllianceSource()
  
