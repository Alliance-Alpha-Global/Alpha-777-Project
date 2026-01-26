import socket
import json
import threading

class AlphaNode:
    def __init__(self, host='0.0.0.0', port=7777):
        self.host = host
        self.port = port
        self.peers = [] # Liste des autres nœuds de l'Alliance
        self.status = "INITIALISATION_NODE"
        
    def start_node(self):
        """Lance l'écoute pour recevoir des données d'autres nœuds souverains."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"[*] Alpha-Node actif sur {self.host}:{self.port}")
        
        while True:
            client, addr = server.accept()
            threading.Thread(target=self.handle_peer, args=(client,)).start()

    def handle_peer(self, client_socket):
        """Gère les messages entrants cryptés ou souverains."""
        data = client_socket.recv(1024).decode('utf-8')
        try:
            message = json.loads(data)
            if message.get("type") == "SYNERGY_CHECK":
                print(f"[!] Vérification de synergie reçue d'un pair.")
                client_socket.send("ALPHA-ACK-1.0".encode('utf-8'))
        except:
            print("[X] Tentative de connexion non-autorisée bloquée.")
        client_socket.close()

if __name__ == "__main__":
    node = AlphaNode()
    # node.start_node() # À activer sur un serveur réel
  
