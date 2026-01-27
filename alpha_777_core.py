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

# --- CONFIGURATION SÉCURITÉ ALPHA ---
SIGNATURE_PILOTE = "777-SOV-1977" # Signature souveraine de Hachem Yo
RAW_KEY = "ALPHA_SIGMA_REBELLION_777" # Clé de chiffrement Alliance

key_hash = hashlib.sha256(RAW_KEY.encode()).digest()
CIPHER_KEY = base64.urlsafe_b64encode(key_hash)
cipher = Fernet(CIPHER_KEY)
PROTOCOL_ID = TProtocol("/alpha-777/1.0.0")

class PilotAuthority:
    def __init__(self, secret: str):
        self._auth_hash = hashlib.sha256(secret.encode()).hexdigest()
        self.authorized = False
        self.last_check = 0

    def check(self, key: str):
        if hashlib.sha256(key.encode()).hexdigest() == self._auth_hash:
            self.authorized = True
            self.last_check = time.time()
            return True
        return False

    def is_valid(self):
        # Session valide 1 heure (Article 3 ASUL-777)
        return self.authorized and (time.time() - self.last_check < 3600)

class AllianceNode:
    def __init__(self, host, port: int):
        self.host = host
        self.port = port
        self.peers = set()
        self.is_chaos_active = False

    async def start(self):
        self.host.set_stream_handler(PROTOCOL_ID, self.stream_handler)
        print(f"[*] Noeud Alpha-777 Actif sur port {self.port}")
        print(f"[+] ID: {self.host.get_id()}")

    async def stream_handler(self, stream: INetStream) -> None:
        try:
            raw = await stream.read()
            msg = cipher.decrypt(raw).decode("utf-8")
            if not msg.startswith("[NOISE]"):
                print(f"\n[ALLIANCE] : {msg}")
        except: pass
        finally: await stream.close()

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
        except:
            if peer_maddr in self.peers: self.peers.remove(peer_maddr)

async def chaos_engine(node):
    print("[!] MODE CHAOS ACTIVÉ.")
    while node.is_chaos_active:
        if node.peers:
            noise = f"[NOISE] {''.join(random.choices(string.ascii_letters, k=32))}"
            for p in list(node.peers): await node.send_secure(p, noise)
        await asyncio.sleep(random.uniform(0.3, 1.5))

async def main(port, dial):
    priv_key, _ = create_new_key_pair()
    host = await new_host(key_pair=priv_key, port=port)
    node = AllianceNode(host, port)
    auth = PilotAuthority(SIGNATURE_PILOTE)

    async with host.run():
        await node.start()
        if dial: await node.send_secure(dial, "Pilote connecté.")

        print("\nCommandes: ask, ask!, chaos, peers, quit")
        while True:
            cmd_line = await asyncio.get_event_loop().run_in_executor(None, input, "α777> ")
            parts = cmd_line.strip().split(" ", 1)
            cmd = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if cmd == "quit": break
            
            # --- PROTECTION REQUISE (Article 3) ---
            if cmd in ["chaos", "ask!"] and not auth.is_valid():
                secret = await asyncio.get_event_loop().run_in_executor(None, input, "[!] Signature Pilote : ")
                if not auth.check(secret):
                    print("[X] Autorité refusée."); continue

            if cmd == "ask":
                async with httpx.AsyncClient() as c:
                    r = await c.post("http://localhost:11434/api/generate", json={"model":"llama3","prompt":args,"stream":False})
                    print(f"\n[IA] {r.json().get('response')}\n")
            
            elif cmd == "chaos":
                node.is_chaos_active = not node.is_chaos_active
                if node.is_chaos_active: asyncio.create_task(chaos_engine(node))
                else: print("[-] Chaos désactivé.")

            elif cmd == "peers": print(f"[*] Pairs: {node.peers}")

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 7777
    d = sys.argv[2] if len(sys.argv) > 2 else None
    asyncio.run(main(p, d))
  
