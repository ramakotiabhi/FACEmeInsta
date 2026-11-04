<div align="center">

# 🛡️ FACEmeInsta
### Autonomous Trust & Safety Firewall & Cross-Platform Identity Mesh
*A new era of trust between people and platforms*

[![Live Production Deployment](https://img.shields.io/badge/Streamlit_Cloud-SYSTEM_ONLINE-00FFAA?style=for-the-badge&logo=streamlit&logoColor=white)](https://facemeinsta-g5zsuknlwywobur4rwmmtn.streamlit.app)
[![Demo Video](https://img.shields.io/badge/YouTube-3_Min_Architecture_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/2YXOH9TS9Hk)
[![Meta Models](https://img.shields.io/badge/Meta_AI-muse--spark--open--1026-0668E1?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/ramakotiabhi/FACEmeInsta)
[![Inference Engine](https://img.shields.io/badge/Baseten-High_Throughput_API-6E56CF?style=for-the-badge)](https://www.baseten.co/)
[![Python Runtime](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/ramakotiabhi/FACEmeInsta)

</div>

---

## 📸 Production Interface & System Preview


<img width="1671" height="941" alt="FACEmeInsta Trust   Safety Flow" src="https://github.com/user-attachments/assets/3b02517a-6ec5-4af9-b88b-875247c9b72f" />

<img width="959" height="892" alt="Screenshot 2026-11-04 225518" src="https://github.com/user-attachments/assets/8c06e3cf-e7a2-48e3-bc12-f5b7ef524147" />

### 1. Autonomous Trust & Safety Firewall Portal (`SYSTEM ONLINE`)
<!-- PASTE YOUR MAIN LANDING PAGE SCREENSHOT HERE -->
## above 18 years the agent workflow.
<img width="1521" height="813" alt="Screenshot 2026-11-03 174859" src="https://github.com/user-attachments/assets/f0d877e9-40b7-43ab-82eb-3c81e5c80648" />
<img width="719" height="629" alt="Screenshot 2026-11-04 141924" src="https://github.com/user-attachments/assets/feb58886-d50a-4372-875a-ecceb99fc641" />
# Name is matched with user id's and the age is above 18 + , then give access to create a new account in instagram
<img width="646" height="794" alt="Screenshot 2026-10-31 154007" src="https://github.com/user-attachments/assets/f31a8d5c-303c-446b-9f60-28f9046a9481" />

## below 18 years agent workflow.
<img width="1313" height="702" alt="Screenshot 2026-11-04 150343" src="https://github.com/user-attachments/assets/e85df679-88f2-4aa8-b686-b0358defd722" />

<img width="1134" height="595" alt="Screenshot 2026-11-04 150334" src="https://github.com/user-attachments/assets/c384d53e-cfd7-4064-9e95-90429913078e" />


### 2. Instagram Guard Agent & Multimodal Inspection Mesh
<!-- PASTE YOUR GUARD AGENT / DASHBOARD SCREENSHOT HERE -->


### 3. Cross-Platform Migration & Immutable Audit Ledger
<!-- PASTE YOUR AUDIT TRAIL / ID VAULT SCREENSHOT HERE -->

---

## 🎯 1. Aim of the Project
**FACEmeInsta** is an enterprise-grade **Autonomous Trust & Safety Firewall** engineered to protect Instagram and the broader social media ecosystem (X, YouTube, Threads, LinkedIn, and emerging platforms). 

Our core objective is to replace reactive, opaque post-incident moderation with a **proactive, cryptographically verifiable, and real-time defense mesh**. By uniting computer vision perceptual hashing, automated cross-platform state management, an interactive **Instagram Guard Agent**, and high-speed multimodal reasoning powered by **Meta open-weight models (`meta-models/muse-spark-open-1026`) on Baseten**, FACEmeInsta stops identity theft, deepfakes, and coordinated harassment before they reach the timeline.

---

## ⚠️ 2. The Real-World Problem
Social platforms and digital creators are currently fighting an asymmetric war against synthetic abuse:

1. **Cross-Platform Deepfake Impersonation & Identity Hijacking:** Bad actors scrape photos and video reels from Instagram to spin up fraudulent clones across multiple social networks within minutes, executing financial scams and reputational attacks.
2. **Coordinated Bot Swarms & Multimodal Harassment:** Legacy moderation relies on static text blocklists that completely miss visual harassment, embedded adversarial text in images, and frame-spliced toxic video uploads.
3. **Siloed Platform Moderation:** When a malicious actor or stolen media asset is detected on one platform, that threat intelligence rarely transfers across social ecosystems—allowing the attacker to simply migrate platforms.
4. **Black-Box Moderation & Zero Auditability:** Users and creators suffer from shadowbans, false-positive takedowns, and unverified moderation strikes without a transparent, tamper-proof audit trail proving *why* an action was taken.

---

## 💡 3. The Solution: FACEmeInsta Defense Mesh
FACEmeInsta operates as an intelligent security layer sitting between user uploads/interactions and the public social graph:

* **🤖 Interactive Instagram Guard Agent:** An always-on AI safety companion that inspects profile activity, evaluates incoming DMs/comments, and assists creators in locking down their digital identity in real time.
* **🌊 Perimeter Defense (`coastal_guard.py`):** Acts as the first line of ingress filtering, intercepting suspicious API payloads, bot-like request velocities, and unauthorized cross-platform scraping attempts.
* **👁️ Perceptual Vision Hashing & Pre-Flight Checks (`vision_hasher.py`):** Computes visual fingerprints and executes OpenCV multi-frame inspections on images and videos prior to publication, detecting manipulated media, deepfake artifacts, and stolen creator assets.
* **🧠 Cognitive Multimodal Core (`core_engine.py` & `meta_api_client.py`):** Routes complex visual and contextual payloads to `meta-models/muse-spark-open-1026` hosted on **Baseten**, enabling sub-second semantic reasoning over nuanced social engineering and implicit visual threats.
* **🔄 Cross-Platform Identity & State Synchronization (`migration_manager.py`):** Ensures verified identity vaults, safety rules, and threat signatures remain portable and synchronized across Instagram and external social networks alongside our persistent SQLite3 master engine (`facemeinsta_master.db`).
* **📜 Immutable Dual-Layer Audit Trail (`audit_logger.py` & `audit_trail.json`):** Every single inspection, hash verification, and Guard Agent intervention is permanently recorded into both a relational database (`facemeinsta_master.db`) and a structured JSON ledger (`audit_trail.json`) for complete regulatory and creator transparency.

---

## 🌟 4. Unique Engineering Features
* **Defense-in-Depth Modularity:** Decouples fast local computer vision pre-flight hashing (`vision_hasher.py`) from deep LLM multimodal inference (`meta_api_client.py`), drastically reducing API latency and compute costs on obvious violations.
* **Zero-Trust Cloud Credential Hygiene:** Engineered for production security—zero hardcoded tokens exist in the repository. All Baseten and Meta inference handshakes are injected at runtime via encrypted Streamlit Cloud `st.secrets` TOML environments.
* **Multi-Platform Portability (`migration_manager.py`):** Built not just as a single-app plugin, but as a portable safety protocol capable of migrating user trust profiles and schema states across social ecosystems.
* **Deterministic + Probabilistic Hybrid Engine:** Combines deterministic cryptographic/visual checks (`vision_hasher.py`, `coastal_guard.py`) with probabilistic AI reasoning (`core_engine.py`) so safety enforcement is both mathematically verifiable and contextually smart.

---

## 🏗️ 5. Production System Architecture & File Map

```text
                       ┌────────────────────────────────────────┐
                       │   Instagram & Social Media Ecosystems  │
                       │  (Creators, Feeds, Reels, DMs, APIs)   │
                       └───────────────────┬────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                        FACEmeInsta Autonomous Firewall (app.py)                      │
│                         [Streamlit Cloud Production Interface]                       │
└───────┬─────────────────────────┬──────────────────────────┬─────────────────────────┘
        │                         │                          │
        ▼                         ▼                          ▼
┌───────────────────┐   ┌────────────────────┐    ┌──────────────────────────┐
│  Perimeter Shield │   │  Visual Pre-Flight │    │   Core Safety Orchestrator│
│ (coastal_guard.py)│   │ (vision_hasher.py) │    │     (core_engine.py)     │
│                   │   │                    │    │                          │
│ • Ingress filter  │   │ • OpenCV / Pillow  │    │ • Threat scoring matrix  │
│ • Rate & anomaly  │   │ • Perceptual hash  │    │ • Policy enforcement     │
│   interception    │   │ • Frame buffer scan│    │ • Guard Agent routing    │
└─────────┬─────────┘   └─────────┬──────────┘    └────────────┬─────────────┘
          │                       │                            │
          └───────────────────────┼────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
      ┌───────────────────────────┐   ┌───────────────────────────────┐
      │   Multimodal AI Inference │   │  Persistence & Audit Layer    │
      │   (meta_api_client.py)    │   │  • audit_logger.py            │
      │                           │   │  • audit_trail.json           │
      │ • Baseten OpenAI SDK      │   │  • migration_manager.py       │
      │ • Meta Open-Weight Model: │   │  • facemeinsta_master.db      │
      │   muse-spark-open-1026    │   │    (SQLite3 Master Vault)     │
      └───────────────────────────┘   └───────────────────────────────┘

