import asyncio
import random
import string
import httpx
import multiaddr
import hashlib
import base64
import time
import sys
from cryptography.fernet import Fernet

from libp2p import new_host
from libp2p.crypto.secp256k1 import create_new_key_pair
from libp2p.network.stream.net_stream_interface import INetStream
from libp2p.typing import TProtocol

# --- CONFIGURATION SÉCURITÉ ALPHA-777 ---
SIGNATURE_PILOTE = "777-SOV-1977"
RAW_KEY = "ALPHA_SIGMA_REBELLION_777"

key_hash = hashlib.sha256(RAW_KEY.encode()).digest()
CIPHER_KEY = base64.urlsafe_b64encode(key_hash)
cipher = Fernet(CIPHER_KEY)
PROTOCOL_ID = TProtocol("/alpha-777/1.0.0")


# --- MODULE D'AUTORITÉ HUMAINE (ASUL-777 Article 3) ---
class PilotAuthority:
    """
    Garantit que les actions sensibles (chaos, diffusion IA, commandes réseau)
    ne peuvent être déclenchées que par un humain authentifié.
    """
    SESSION_DURATION = 3600  # 1 heure de souveraineté humaine

    def __init__(self, secret: str):
        self._auth_hash = hashlib.sha256(secret.encode()).hexdigest()
        self.authorized = False
        self.last_check = 0

    def check(self, key: str) -> bool:
        if hashlib.sha256(key.encode()).hexdigest() == self._auth_hash:
            self.authorized = True
            self.last_check = time.time()
            print("[✓] Autorité Pilote confirmée : Signature validée.")
            return True
        print("[X] ÉCHEC D'AUTORITÉ : Signature invalide.")
        return False

    def is_valid(self) -> bool:
        if not self.authorized:
            return False
        elapsed = time.time() - self.last_check
        if elapsed > self.SESSION_DURATION:
            self.authorized = False
            print("[!] Session expirée : Autorité Pilote révoquée.")
            return False
        return True


# --- NOEUD DE L'ALLIANCE ---
class AllianceNode:
    def __init__(self, host, port: int):
        self.host = host
        self.port = port
        self.peers = set()
        self.is_chaos_active = False

    async def start(self):
        self.host.set_stream_handler(PROTOCOL_ID, self.stream_handler)
        print(f"[*] Noeud Alpha-777 Actif sur port {self.port}")
        print(f"[+] Multiaddr: /ip4/127.0.0.1/tcp/{self.port}/p2p/{self.host.get_id()}")

    async def stream_handler(self, stream: INetStream) -> None:
        try:
            raw = await stream.read()
            msg = cipher.decrypt(raw).decode("utf-8")
            if not msg.startswith("[NOISE"):
                print(f"\n[ALLIANCE] : {msg}")
        except Exception:
            pass
        finally:
            await stream.close()

    async def send_secure(self, peer_maddr: str, message: str):
        try:
            maddr = multiaddr.Multiaddr(peer_maddr)
            peer_id = maddr.value_for_protocol("p2p")

            if peer_maddr not in self.peers:
                await self.host.connect(maddr)
                self.peers.add(peer_maddr)

            stream = await self.host.new_stream(peer_id, [PROTOCOL_ID])
            await stream.write(cipher.encrypt(message.encode()))
            await stream.close()
        except Exception:
            if peer_maddr in self.peers:
                self.peers.remove(peer_maddr)


# --- MOTEUR DE BROUILLAGE (CHAOS ENGINE) ---
async def chaos_engine(node: AllianceNode):
    print("[!] MODE CHAOS ACTIVÉ : Brouillage en cours...")
    while node.is_chaos_active:
        if node.peers:
            noise = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
            payload = f"[NOISE:{random.randint(1000,9999)}] {noise}"
            for p in list(node.peers):
                await node.send_secure(p, payload)
        await asyncio.sleep(random.uniform(0.25, 1.75))
    print("[-] MODE CHAOS désactivé.")


# --- BOUCLE PRINCIPALE ---
async def main(port, dial):
    priv_key, _ = create_new_key_pair()
    host = await new_host(key_pair=priv_key, port=port)
    node = AllianceNode(host, port)
    auth = PilotAuthority(SIGNATURE_PILOTE)

    async with host.run():
        await node.start()
        if dial:
            await node.send_secure(dial, "Liaison Pilote établie.")

        loop = asyncio.get_event_loop()
        print("\n[CONSOLE ALPHA-777] Commandes: ask, ask!, chaos, peers, quit")

        while True:
            cmd_line = await loop.run_in_executor(None, input, "α777> ")
            cmd_line = cmd_line.strip()
            if not cmd_line:
                continue

            parts = cmd_line.split(" ", 1)
            cmd = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if cmd == "quit":
                node.is_chaos_active = False
                break

            # --- PROTECTIONS ---
            if cmd in ["chaos", "ask!"] and not auth.is_valid():
                secret = await loop.run_in_executor(None, input, "[!] Signature Pilote requise : ")
                if not auth.check(secret):
                    continue

            if cmd == "peers":
                print(f"[*] Pairs actifs ({len(node.peers)}) : {node.peers}")

            elif cmd == "ask":
                async with httpx.AsyncClient() as c:
                    try:
                        r = await c.post(
                            "http://localhost:11434/api/generate",
                            json={"model": "llama3", "prompt": args, "stream": False},
                            timeout=45.0
                        )
                        print(f"\n[IA LOCALE] : {r.json().get('response')}\n")
                    except Exception:
                        print("[!] Erreur : Ollama est-il actif ?")

            elif cmd == "ask!":
                async with httpx.AsyncClient() as c:
                    try:
                        r = await c.post(
                            "http://localhost:11434/api/generate",
                            json={"model": "llama3", "prompt": args, "stream": False},
                            timeout=45.0
                        )
                        resp = r.json().get('response')
                        print(f"\n[IA ALLIANCE] : {resp}\n")
                        for p in list(node.peers):
                            await node.send_secure(p, f"[DIFFUSION IA] {resp}")
                    except Exception:
                        print("[!] Erreur : Ollama est-il actif ?")

            elif cmd == "chaos":
                node.is_chaos_active = not node.is_chaos_active
                if node.is_chaos_active:
                    asyncio.create_task(chaos_engine(node))
                else:
                    print("[-] Arrêt du brouillage.")

            else:
                print("[!] Commande inconnue.")

if __name__ == "__main__":
    target_port = int(sys.argv[1]) if len(sys.argv) > 1 else 7777
    target_peer = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        asyncio.run(main(target_port, target_peer))
    except KeyboardInterrupt:
        print("\n[-] Shutdown. L'humain reste le seul point de vérité.")
