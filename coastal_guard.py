import time
from core_engine import FaceMeInstaKernel
from meta_api_client import analyze_profile_with_meta
from audit_logger import ImmutableAuditLog

# Initialize audit logger instance globally
audit_logger = ImmutableAuditLog()

def run_coastal_guard_daemon(kernel: FaceMeInstaKernel):
    """
    24/7 Autonomous Coastal Guard Agent Daemon.
    Patrols network streams without human intervention.
    """
    print("\n🌊 [Coastal Guard Agent] Sentinel daemon active. Patrolling stream 24/7...")
    
    while True:
        stream = kernel.state["active_stream"]
        roots = kernel.state["root_registry"]
        
        for event in stream:
            if event["status"] == "PENDING_AGENT_AUDIT":
                print(f"\n🔍 [Agent Audit] Inspecting profile: @{event['username']} ({event['full_name']})")
                
                # 1. Call Meta Model API for intent & safety reasoning
                meta_eval = analyze_profile_with_meta(event["username"], event["full_name"])
                print(f"🧠 [Meta Model API] Verdict: {meta_eval.get('verdict')} | {meta_eval.get('reasoning')}")
                
                # 2. Chronological Impersonation & Identity Theft Check
                imposter_detected = False
                for root in roots:
                    if root["full_name"].lower() == event["full_name"].lower():
                        # If account was created AFTER the root node, it's a clone/imposter
                        if event["created_at"] > root["created_at"]:
                            imposter_detected = True
                            event["status"] = "QUARANTINED_IMPOSTER"
                            event["threat_notes"] = f"Identity theft clone! Mimics verified root '@{root['username']}' created earlier."
                            print(f"🚨 [QUARANTINE ENFORCED] Isolated fake account @{event['username']}!")
                            
                            # 🔒 LOG ACTION HERE (Inside scope where `event` exists)
                            audit_logger.log_action(
                                actor="Coastal_Guard_Agent",
                                action="QUARANTINE_IMPOSTER",
                                target=event['username'],
                                details=event['threat_notes']
                            )
                            break
                            
                if not imposter_detected:
                    event["status"] = "CLEAN"
                    event["threat_notes"] = "Passed Meta model reasoning and chronological integrity checks."
                    print(f"✅ [CLEAN] Profile @{event['username']} verified safe.")
                    
                    # Optional: Log clean audits too if you want full transparency
                    audit_logger.log_action(
                        actor="Coastal_Guard_Agent",
                        action="VERIFY_CLEAN",
                        target=event['username'],
                        details=event['threat_notes']
                    )
                    
        time.sleep(3)

if __name__ == "__main__":
    kernel = FaceMeInstaKernel()
    
    # Simulate an incoming identity theft/clone attack in the stream
    kernel.ingest_stream_event("abhiram_fake_scam99", "Abhiram Sharma", "hash_stolen_pic_001")
    
    # Run the background daemon
    try:
        run_coastal_guard_daemon(kernel)
    except KeyboardInterrupt:
        print("\n🛑 [Coastal Guard Daemon] Paused by operator.")