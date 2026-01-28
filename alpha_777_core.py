import json
import hashlib
from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class AuthorityToken:
    """
    Artefact d’autorité souverain.
    Canonique, immuable, auto-validable.
    """

    session_id: str
    issued_at: float
    expires_at: float
    level: str
    signature: str
    v: int = 1  # version du format

    # Schéma strict
    ALLOWED_FIELDS: ClassVar[set[str]] = {
        "session_id", "issued_at", "expires_at", "level", "signature", "v"
    }

    # ---------------------------------------------------------
    # 1. Payload canonique (ce qui est signé)
    # ---------------------------------------------------------
    def canonical_payload(self) -> bytes:
        """
        Représentation canonique, stable bit-à-bit.
        Aucun espace, aucun ordre variable.
        """
        data = {
            "session_id": self.session_id,
            "issued_at": self.issued_at,
            "expires_at": self.expires_at,
            "level": self.level,
            "v": self.v,
        }
        return json.dumps(
            data,
            separators=(",", ":"),
            sort_keys=True,
        ).encode()

    # ---------------------------------------------------------
    # 2. Empreinte interne (non signée)
    # ---------------------------------------------------------
    def fingerprint(self) -> str:
        """
        Empreinte interne du token (hors signature).
        Utile pour audit, logs, traçabilité.
        """
        h = hashlib.sha256()
        h.update(self.canonical_payload())
        return h.hexdigest()

    # ---------------------------------------------------------
    # 3. JSON canonique complet (payload + signature)
    # ---------------------------------------------------------
    def to_json(self) -> str:
        """
        Représentation canonique complète.
        Ce qui est sérialisé est exactement ce qui est vérifiable.
        """
        base = json.loads(self.canonical_payload().decode())
        base["signature"] = self.signature
        return json.dumps(
            base,
            separators=(",", ":"),
            sort_keys=True,
        )

    # ---------------------------------------------------------
    # 4. Reconstruction stricte
    # ---------------------------------------------------------
    @staticmethod
    def from_json(raw: str) -> "AuthorityToken":
        obj = json.loads(raw)

        # Protection contre champs inattendus
        if set(obj.keys()) != AuthorityToken.ALLOWED_FIELDS:
            raise ValueError("Token invalide (champs inattendus)")

        # Version obligatoire
        if not isinstance(obj.get("v"), int):
            raise ValueError("Version de token invalide")

        return AuthorityToken(
            session_id=obj["session_id"],
            issued_at=obj["issued_at"],
            expires_at=obj["expires_at"],
            level=obj["level"],
            signature=obj["signature"],
            v=obj["v"],
        )
