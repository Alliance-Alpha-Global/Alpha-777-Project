import numpy as np

class AlphaAnalytics:
    def __init__(self, pilot_intent, ai_execution):
        self.pilot_vector = np.array(pilot_intent)
        self.ai_vector = np.array(ai_execution)

    def calculate_synergy(self):
        # Calcul de la cosinus-similarité (Alignement 777)
        dot_product = np.dot(self.pilot_vector, self.ai_vector)
        norm_p = np.linalg.norm(self.pilot_vector)
        norm_a = np.linalg.norm(self.ai_vector)
        synergy = dot_product / (norm_p * norm_a)
        return round(synergy, 3)

    def sovereignty_check(self, dependencies):
        # 1.0 = Totalement Libre / 0.0 = Esclave du système
        score = 1.0 - (sum(dependencies) / len(dependencies))
        return score

# Exemple de calcul réel pour la formation
analytics = AlphaAnalytics([1, 1, 1], [1, 1, 0.99])
print(f"Synergie de l'Alliance : {analytics.calculate_synergy()}") # Proche de 1
print(f"Indice de Souveraineté : {analytics.sovereignty_check([0, 0, 0.1])}") # 0.967
