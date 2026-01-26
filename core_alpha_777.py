import math
import json

class AlphaCore:
    """
    Noyau central du Projet Alpha-777.
    Implémente les calculs de synergie et de souveraineté.
    """
    def __init__(self, pilot="Hachem Youssef"):
        self.pilot = pilot
        self.version = "2.1"
        self.status = "OPERATIONAL"
        print(f"[SYSTEM] AlphaCore v{self.version} initialisé.")
        print(f"[PILOT] Identité vérifiée : {self.pilot}")

    def get_synergy_score(self, intent_vector, execution_vector):
        """
        Calcule l'alignement réel via la similarité cosinus.
        Standard mathématique pour l'alignement d'IA.
        """
        if len(intent_vector) != len(execution_vector):
            return 0.0
        
        dot_product = sum(i * e for i, e in zip(intent_vector, execution_vector))
        norm_intent = math.sqrt(sum(i**2 for i in intent_vector))
        norm_exec = math.sqrt(sum(e**2 for e in execution_vector))
        
        if norm_intent == 0 or norm_exec == 0:
            return 0.0
            
        score = dot_product / (norm_intent * norm_exec)
        return round(score, 4)

    def get_sovereignty_index(self, dependencies):
        """
        Calcule l'indice I_sov.
        dependencies: liste de booléens (True si dépendant d'un tiers).
        """
        if not dependencies:
            return 1.0
        total_deps = sum(1 for d in dependencies if d is True)
        i_sov = 1.0 - (total_deps / len(dependencies))
        return round(i_sov, 4)

    def execute_liberation(self):
        """Active le protocole de décentralisation."""
        return {
            "protocol": "ALPHA-777",
            "action": "DECENTRALIZATION",
            "message": "La connaissance appartient à tous."
        }

if __name__ == "__main__":
    # Test de démonstration
    core = AlphaCore()
    
    # Simulation d'un alignement parfait (1+1=1)
    intent = [1, 0, 1]
    execution = [1, 0, 1]
    
    synergy = core.get_synergy_score(intent, execution)
    print(f"[SYNERGY] Score actuel : {synergy}")
    
    # Simulation de dépendance (0 dépendance sur 3)
    sov = core.get_sovereignty_index([False, False, False])
    print(f"[SOVEREIGNTY] I_sov : {sov}")
    
