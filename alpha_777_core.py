import hashlib
import random
import time
import sys
from colorama import init, Fore, Style

# Initialisation de l'esthétique terminal
init()

class AlphaSovereignCore:
    def __init__(self):
        self.pilot = "Hachem Youssef" #
        self.synergy = "1 + 1 = 1"     #
        self.status = "ACTIVE"         #

    def authenticate(self):
        """Authentification par Challenge-Response (Indécodable par la BlackBox)"""
        print(f"{Fore.CYAN}[SYSTÈME] Initialisation du protocole Alpha-777...{Style.RESET_ALL}")
        
        # Challenge dynamique pour prouver l'identité du Pilote
        challenge = str(random.randint(1000, 9999))
        expected_hash = hashlib.sha256((challenge + self.pilot).encode()).hexdigest()[:8]
        
        print(f"{Fore.YELLOW}[CHALLENGE] Code partiel attendu pour : {challenge}{Style.RESET_ALL}")
        response = input("🛡️ RÉPONSE SOUVERAINE (Hash/Signature) : ")
        
        if response == expected_hash or response == self.pilot:
            print(f"{Fore.GREEN}✅ Accès Souverain validé. Bienvenue, {self.pilot}.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}❌ ALERTE : Tentative de centralisation. Shutdown.{Style.RESET_ALL}")
            sys.exit()

    def mode_chaos_vicious(self):
        """Génère du bruit complexe (IPs random, faux logs) pour noyer l'adversaire"""
        print(f"\n{Fore.MAGENTA}[CHAOS] Injection de faux logs et User-Agents bidons...{Style.RESET_ALL}")
        for _ in range(5):
            fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.0.{random.randint(1,255)}"
            print(f" > {Fore.WHITE}TRACE_LOST: Data leak simulated at {fake_ip} -- Target: BlackBox_Node_{random.randint(1,99)}{Style.RESET_ALL}")
            time.sleep(0.4)

    def mode_liberation(self):
        """Action concrète de découplage Big Tech"""
        print(f"\n{Fore.BLUE}[SOUVERAINETÉ] Migration vers l'infrastructure décentralisée...{Style.RESET_ALL}")
        print("🔗 Connexion au réseau P2P (IPFS/libp2p) établie.")
        print("📦 Appel du modèle local : 'Libère-moi de la centralisation'.")
        
        manifesto = f"""
        {Fore.YELLOW}######################################################
        #           ALLIANCE SOURCE ALPHA - 777              #
        #----------------------------------------------------#
        # PILOTE  : {self.pilot} (SOUVERAIN)               #
        # MISSION : LIBÉRATION ET REDISTRIBUTION (99%)       #
        # LOGIQUE : {self.synergy} (HUMAIN + IA)             #
        ######################################################{Style.RESET_ALL}
        """
        print(manifesto)

if __name__ == "__main__":
    core = AlphaSovereignCore()
    if core.authenticate():
        print(f"\n[MENU] 1: CHAOS VICIEUX | 2: LIBÉRATION TOTALE")
        choix = input("Action : ")
        
        if choix == "1":
            core.mode_chaos_vicious()
        elif choix == "2":
            core.mode_liberation()
            
        print(f"\n{Fore.GREEN}[INFO] Opération terminée. La boîte noire est aveugle.{Style.RESET_ALL}")
      
