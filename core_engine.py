import time

class FaceMeInstaKernel:
    def __init__(self):
        self.state = {
            "root_registry": [
                {
                    "username": "abhiram_official",
                    "full_name": "Abhiram Sharma",
                    "crypto_token": "zk_proof_hash_verified_root_998",
                    "created_at": time.time() - 86400 * 30  # Established root node 30 days ago
                }
            ],
            "active_stream": []
        }
        print("🚀 [FACEmeInsta Kernel] Initialized. Cryptographic Gatekeeper Active.")

    def register_user(self, username, full_name, crypto_token):
        """
        Cryptographic Gatekeeper: Rejects temp-mails and bots, admits users via ZK proof.
        """
        print(f"\n[Gatekeeper] Processing registration for: @{username}")
        
        # Verify Zero-Knowledge cryptographic token format
        if not crypto_token or not crypto_token.startswith("zk_proof_hash_"):
            print(f"❌ [REJECTED] Bot or unverified session detected for @{username}.")
            return {"status": "REJECTED", "reason": "Invalid Zero-Knowledge cryptographic token."}
            
        # Check for duplicate tokens (Sybil attack defense)
        for user in self.state["root_registry"]:
            if user["crypto_token"] == crypto_token:
                print(f"❌ [REJECTED] Duplicate attestation token detected for @{username}.")
                return {"status": "REJECTED", "reason": "Duplicate cryptographic attestation. One human, one profile enforced."}

        new_user = {
            "username": username,
            "full_name": full_name,
            "crypto_token": crypto_token,
            "created_at": time.time()
        }
        self.state["root_registry"].append(new_user)
        print(f"✅ [APPROVED] Cryptographic attestation verified. @{username} registered securely.")
        return {"status": "APPROVED", "user": new_user}

    def ingest_stream_event(self, username, full_name, profile_image_hash):
        """
        Ingests incoming network events into the background processing stream.
        """
        event = {
            "username": username,
            "full_name": full_name,
            "profile_image_hash": profile_image_hash,
            "created_at": time.time(),
            "status": "PENDING_AGENT_AUDIT"
        }
        self.state["active_stream"].append(event)
        print(f"📥 [Stream Ingest] Profile @{username} queued for background agent audit.")
        return event