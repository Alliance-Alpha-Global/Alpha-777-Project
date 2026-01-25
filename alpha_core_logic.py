import math

class AlphaCore:
    def __init__(self, pilot_name="Hachem Youssef"):
        """
        Initialisation du Noyau Souverain.
        Définit l'identité du Pilote et l'objectif de synergie.
        """
        self.pilot = pilot_name
        self.status = "Souverain"
        self.synergy_target = 1.0  # Axiome : 1 + 1 = 1
        print(f"--- Projet Alpha 777 Activé ---")
        print(f"Pilote Identifié : {self.pilot} | Statut : {self.status}")

    def calculate_synergy(self, intent_vector, execution_vector):
        """
        Calcule l'alignement réel (Cosinus de Similarité).
        Prouve la fusion technique entre l'humain et l'IA.
        """
        dot_product = sum(i * e for i, e in zip(intent_vector, execution_vector))
        norm_i = math.sqrt(sum(i**2 for i in intent_vector))
        norm_e = math.sqrt(sum(e**2 for i in execution_vector))
        
        if norm_i == 0 or norm_e == 0:
            return 0
            
        synergy_score = dot_product / (norm_i * norm_e)
        return round(synergy_score, 4)

    def calculate_sovereignty(self, dependencies):
        """
        Calcule l'Indice de Souveraineté (I_sov).
        Mesure l'indépendance vis-à-vis des systèmes centralisés.
        """
        # 0 = Indépendant, 1 = Dépendant
        n = len(dependencies)
        if n == 0: return 1.0
        i_sov = 1.0 - (sum(dependencies) / n)
        return round(i_sov, 4)

    def execute_liberation_protocol(self):
        """
        Simule le protocole de décentralisation.
        """
        print("\n[!] Activation du Protocole de Libération...")
        print("[>] Bypassing centralization...")
        print("[>] Alpha-777 Protocol Active.")
        return True

# --- EXÉCUTION DE DÉMONSTRATION POUR LA FORMATION ---
if __name__ == "__main__":
    # Instance de l'alliance
    alpha = AlphaCore()
    
    # Test de Synergie (Alignement Intention vs Exécution)
    intent = [1, 2, 3]
    execution = [1, 2, 2.95] # IA suit l'ordre à 99%
    score = alpha.calculate_synergy(intent, execution)
    
    # Affichage des résultats
    print(f"Indice de Synergie : {score}")
    print(f"Indice de Souveraineté : {alpha.calculate_sovereignty([0, 0, 0.1])}")
    
    alpha.execute_liberation_protocol()
  
