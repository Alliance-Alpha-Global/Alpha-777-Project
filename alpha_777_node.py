import asyncio
import time
import hashlib
import base64
import aioconsole
import multiaddr
from cryptography.fernet import Fernet

from libp2p import new_host
from libp2p.typing import TProtocol
from libp2p.network.stream.net_stream_interface import INetStream
from libp2p.peer.peerinfo import info_from_p2paddr

# --- CONFIGURATION (Citations des spécifications Alpha-777) ---
SIGNATURE_PILOTE = "777-SOV-1977"
RAW_KEY = "ALPHA_SIGMA_REBELLION_777"
PROTOCOL_ID = TProtocol("/alpha-777/1.0.0")

# Initialisation du chiffrement
key_hash = hashlib.sha256(RAW_KEY.encode()).digest()
CIPHER_KEY = base64.urlsafe_b64encode(key_hash)
cipher = Fernet(CIPHER_KEY)

# --- LOGIQUE D'AUTORITÉ (Article 3) ---
class PilotAuthority:
    SESSION_DURATION = 3600  # 1 hour
    def __init__(self):
        self.authorized = True # Activé pour le test
        self.last_check = time.time()

    def is_valid(self) -> bool:
        # Vérifie si la session n'a pas expiré selon l'Article 3
        if not self.authorized: return False
        return (time.time() - self.last_check) < self.SESSION_DURATION

authority = PilotAuthority()

# --- FONCTIONS RÉSEAU (Tes dernières mises à jour) ---

async def send_message(host, destination_maddr, message_text):
    # Sécurité Article 3 : Session obligatoire
    if not authority.is_valid():
        print("[!] SESSION EXPIRED. Veuillez vous ré-authentifier.")
        return

    try:
        maddr = multiaddr.Multiaddr(destination_maddr)
        info = info_from_p2paddr(maddr)
        print(f"[RÉSEAU] Connexion → {info.peer_id}")
        await host.connect(info)

        stream = await host.new_stream(info.peer_id, [PROTOCOL_ID])
        
        # Paquet Alpha-777 structuré
        packet = f"TYPE:AUTH_REQ\nSIGNATURE:{SIGNATURE_PILOTE}\nBODY:{message_text}"
        encrypted = cipher.encrypt(packet.encode())
        
        await stream.write(encrypted)
        await stream.close()
        print("[✓] Paquet Alpha‑777 envoyé.")
    except Exception as e:
        print(f"[!] Échec d'envoi : {e}")

# ... (ajoute ici ton chat_handler et ton pilot_interface)
