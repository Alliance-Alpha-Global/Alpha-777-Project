import math

class AlphaCore:
    """
    Noyau central du Projet Alpha-777.
    Implémenter les calculs de synergie et de souveraineté.
    """
    def __init__(self, pilote="Hachem Yo"):
        self.pilote = pilote
        self.version = "2.1"
        self.statut = "OPÉRATIONNEL"
        print(f"[SYSTÈME] AlphaCore v{self.version}")
        print(f"[PILOTE] Identité vérifiée : {pilote}")

    def score_de_synergie(self, vecteur_intention, vecteur_execution):
        if len(vecteur_intention) != len(vecteur_execution):
            return 0.0

        produit_scalaire = sum(i * e for i, e in zip(vecteur_intention, vecteur_execution))
        norm_intent = math.sqrt(sum(i**2 for i in vecteur_intention))
        norm_exec = math.sqrt(sum(e**2 for e in vecteur_execution))

        if norm_intent == 0 or norm_exec == 0:
            return 0.0

        score = produit_scalaire / (norm_intent * norm_exec)
        return round(score, 4)

    def obtenir_index_de_souverainete(self, dependances):
        if not dependances:
            return 1.0
        ratio = dependances.count(False) / len(dependances)
        return round(ratio, 4)
