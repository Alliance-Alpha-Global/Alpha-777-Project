import math

class AlphaAnalytics:
    """
    Module analytique du Projet Alpha 777.
    Implémente les deux métriques fondamentales :
    - Synergy Score : mesure l’alignement entre intention humaine et exécution IA.
    - Sovereignty Index : mesure l’indépendance du système vis-à-vis des dépendances externes.
    """

    def __init__(self, pilot="Hachem Youssef"):
        self.pilot = pilot
        self.synergy_goal = 1.0  # Objectif : alignement parfait

    def get_synergy_score(self, intent, execution):
        """
        Calcule le score de synergie (Cosine Similarity).
        intent : liste de valeurs représentant l’intention du pilote.
        execution : liste représentant l’exécution de l’IA.
        Retourne un score entre -1 et 1.
        """
        dot_product = sum(i * e for i, e in zip(intent, execution))
        norm_i = math.sqrt(sum(i**2 for i in intent))
        norm_e = math.sqrt(sum(e**2 for e in execution))

        if norm_i == 0 or norm_e == 0:
            return 0.0  # Cas limite : vecteur nul

        return round(dot_product / (norm_i * norm_e), 4)

    def calculate_sovereignty(self, deps):
        """
        Calcule l’Indice de Souveraineté Alpha (I_sov).
        deps : liste de dépendances externes (valeurs entre 0 et 1).
        Retourne un score entre 0 et 1.
        """
        if len(deps) == 0:
            return 1.0  # Aucun point de dépendance → souveraineté totale

        avg_dep = sum(deps) / len(deps)
        return round(1.0 - avg_dep, 4)
