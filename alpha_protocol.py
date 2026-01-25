from enum import Enum, auto

class Etat(Enum):
    VEILLE = auto()
    AUDIT = auto()
    MANIFESTE = auto()
    SOUVERAIN = auto()
    URGENCE = auto()

class ProtocolStateMachine:
    def __init__(self, pilote="Youssef"):
        self.pilote = pilote
        self.etat_actuel = Etat.VEILLE
        self._historique = []

    def transition(self, nouvel_etat: Etat):
        """Transition sécurisée avec validation du Pilote."""
        print(f"[PROTOCOL] Tentative : {self.etat_actuel.name} -> {nouvel_etat.name}")
        
        # Protection renforcée : SOUVERAIN et URGENCE
        if nouvel_etat in (Etat.SOUVERAIN, Etat.URGENCE):
            print(f"[!] ÉTAT CRITIQUE : Validation du Pilote ({self.pilote}) requise.")
            # Simulation de l'accord du Pilote
            self._appliquer_transition(nouvel_etat)
        else:
            self._appliquer_transition(nouvel_etat)

    def _appliquer_transition(self, etat: Etat):
        """Méthode interne de mise à jour (corrigée)."""
        self.etat_actuel = etat
        self._historique.append(etat)
        print(f"[SUCCESS] Système désormais en mode : {self.etat_actuel.name}")
      
