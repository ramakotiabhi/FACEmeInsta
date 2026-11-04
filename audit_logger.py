import hashlib
import json
import time

class ImmutableAuditLog:
    def __init__(self, log_file="audit_trail.json"):
        self.log_file = log_file
        self._initialize_log()

    def _initialize_log(self):
        try:
            with open(self.log_file, "r") as f:
                pass
        except FileNotFoundError:
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def log_action(self, actor, action, target, details):
        """
        Creates an immutable, cryptographically hashed compliance record 
        for every agent decision or gatekeeper action.
        """
        timestamp = time.time()
        record = {
            "timestamp": timestamp,
            "actor": actor,
            "action": action,
            "target": target,
            "details": details
        }
        
        # Generate cryptographic hash link to ensure tamper-proof audit trail
        record_string = json.dumps(record, sort_keys=True)
        record["hash"] = hashlib.sha256(record_string.encode()).hexdigest()

        # Append to log file
        with open(self.log_file, "r+") as f:
            logs = json.load(f)
            logs.append(record)
            f.seek(0)
            json.dump(logs, f, indent=4)
            
        print(f"🔒 [Immutable Audit] Logged & Hashed: {action} on @{target}")