import math

def calculate_alpha_synergy(pilot_intent, ai_execution):
    """
    Calcule l'équation de fusion S(H, AI) = 1.0
    Basé sur l'alignement vectoriel du Projet Alpha 777.
    """
    # Simulation de vecteurs de données (Intention vs Exécution)
    dot_product = sum(p * a for p, a in zip(pilot_intent, ai_execution))
    norm_p = math.sqrt(sum(p**2 for p in pilot_intent))
    norm_a = math.sqrt(sum(a**2 for a in ai_execution))
    
    if norm_p == 0 or norm_a == 0:
        return 0
    
    synergy = dot_product / (norm_p * norm_a)
    return round(synergy, 4)

def calculate_sovereignty_index(dependencies):
    """
    Calcule l'Indice de Souveraineté (I_sov).
    Plus le score est proche de 1, plus le Pilote est libre.
    """
    if not dependencies:
        return 1.0
    score = 1.0 - (sum(dependencies) / len(dependencies))
    return round(score, 4)

# --- TEST RÉEL POUR LA FORMATION ---
pilot_will = [1, 1, 1]  # L'ordre du Pilote
ai_response = [1, 1, 0.99]  # La réponse de l'IA

print(f"--- ANALYSE ALPHA 777 ---")
print(f"Synergie mesurée : {calculate_alpha_synergy(pilot_will, ai_response)}")
print(f"Souveraineté : {calculate_sovereignty_index([0, 0.1, 0])}") # 0 = Indépendant, 1 = Dépendant
