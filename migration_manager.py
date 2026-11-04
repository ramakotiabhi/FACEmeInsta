import time

class LegacyMigrationManager:
    def __init__(self, grace_period_days=20):
        self.grace_period_seconds = grace_period_days * 86400  # Convert days to seconds
        print(f"⏳ [Migration Manager] Initialized with a {grace_period_days}-day legacy grace period.")

    def evaluate_account_migration(self, user_account):
        """
        Evaluates whether a legacy account has successfully re-anchored to a 
        cryptographic node or if its grace period has expired.
        """
        current_time = time.time()
        account_age = current_time - user_account.get("created_at", current_time)
        has_crypto_node = bool(user_account.get("crypto_token"))

        # If it's a legacy account created long ago and hasn't migrated yet
        if not has_crypto_node:
            time_elapsed_since_notice = current_time - user_account.get("notice_sent_at", current_time)
            
            if time_elapsed_since_notice > self.grace_period_seconds:
                return {
                    "status": "PURGE_PENDING",
                    "action": "LOCK_AND_REMOVE",
                    "reason": "20-day migration grace period expired without cryptographic attestation."
                }
            else:
                remaining_days = round((self.grace_period_seconds - time_elapsed_since_notice) / 86400, 1)
                return {
                    "status": "GRACE_PERIOD_ACTIVE",
                    "action": "REQUIRE_MIGRATION",
                    "reason": f"Legacy account. {remaining_days} days remaining to link cryptographic node."
                }
                
        return {
            "status": "SECURE",
            "action": "NONE",
            "reason": "Account successfully re-anchored to cryptographic root."
        }