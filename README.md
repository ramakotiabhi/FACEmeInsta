<div align="center">



# 🛡️ FACEmeInsta
### Autonomous Trust & Safety Firewall & Sovereign Identity Mesh for Instagram
*A new era of trust between people and platforms*

[![Live Production Deployment](https://img.shields.io/badge/Streamlit_Cloud-SYSTEM_ONLINE-00FFAA?style=for-the-badge&logo=streamlit&logoColor=white)](https://facemeinsta-g5zsuknlwywobur4rwmmtn.streamlit.app)
[![Demo Video](https://img.shields.io/badge/YouTube-3_Min_Architecture_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/2YXOH9TS9Hk)
[![Meta Models](https://img.shields.io/badge/Meta_AI-muse--spark--open--1026-0668E1?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/ramakotiabhi/FACEmeInsta)
[![Inference Engine](https://img.shields.io/badge/Baseten-High_Throughput_API-6E56CF?style=for-the-badge)](https://www.baseten.co/)
[![Python Runtime](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/ramakotiabhi/FACEmeInsta)

</div>

---
<img width="1671" height="941" alt="FACEmeInsta Trust   Safety Flow" src="https://github.com/user-attachments/assets/7a6319dc-2750-450e-852c-24cb3f148fb5" />


---

## 🎯 1. Aim of the Project & The AI Era Imperative
For over a decade, Instagram and global social platforms have focused primarily on **growth, hyper-connectivity, and feature development**. However, we have now entered the **Advanced AI Era**. When bad actors could cause massive harm *without* advanced AI, giving malicious actors access to generative AI, deepfakes, and automated bot swarms threatens to collapse the entire social media trust ecosystem.
<img width="959" height="892" alt="Screenshot 2026-11-04 225518" src="https://github.com/user-attachments/assets/9b3292c4-2762-419a-8591-3b45c1aeec47" />
**FACEmeInsta** is built to solve this foundational crisis. It is a **Two-Pillar Autonomous Trust & Safety Firewall** designed to restore human authenticity, eradicate fake/clone accounts, enforce strict 18+ age verification with zero privacy leakage to social platforms, and intercept `#hashtag` (`#strings`) mismatches, phishing scams, and CSAM/NSFW media *before* they ever touch the public timeline.

<img width="1521" height="813" alt="Screenshot 2026-11-03 174859" src="https://github.com/user-attachments/assets/54d12c2b-f0dc-484f-8cec-23a7540b5548" />

---

## ⚠️ 2. The Real-World Problems Facing Instagram Today
1. **Unchecked Fake Accounts & Impersonation Scams:** Scammers scrape real users' photos and reels to spin up hundreds of fake clone accounts. Because Instagram lacks a cryptographic "one-human-one-gatepass" binding, distinguishing real accounts from clones is slow and reactive.
2. **Failure to Prevent Underage (<18) Account Creation:** Children and minors under 18 easily bypass birthday dropdowns to create accounts, exposing themselves to predatory behavior, toxic algorithms, and explicit content.
3. **Centralized Privacy Fears:** Users rightly fear uploading sensitive government IDs directly to Meta or global social platforms due to data breach and surveillance concerns.
4. **The `#strings` (Hashtag/Caption) Bait-and-Switch Scam:** Attackers upload a trending or innocent-looking Reel/Video while stuffing unrelated trending `#strings` (hashtags) and malicious phishing links into the caption—or vice versa—tricking users into clicking malware or financial scam traps.
5. **Post-Upload Reactive Moderation:** Harmful content (nudity, sexual abuse, child exploitation, deepfake defamation) is often flagged *after* thousands of people have already viewed it.

<img width="720" height="1600" alt="WhatsApp Image 2026-11-05 at 4 26 32 PM" src="https://github.com/user-attachments/assets/62125941-5d74-4a58-817e-af8316adf0ba" />
<img width="720" height="1600" alt="WhatsApp Image 2026-11-05 at 4 30 09 PM" src="https://github.com/user-attachments/assets/0a69170f-89b2-41af-bc99-e6c3e339adf1" />

---

## 🏛️ 3. The Two Core Pillars of FACEmeInsta (Step-by-Step Process)

### 🔐 Pillar 1: Sovereign ID Vault & Cryptographic Gatepass Key (18+ Enforcement & Fake Account Eradication)
Instead of handing personal IDs over to Meta or Instagram, FACEmeInsta introduces a **Country-Level Sovereign Trust Architecture** (`migration_manager.py` & `coastal_guard.py`).

#### Step-by-Step Workflow (Panel 1):
1. **Local Sovereign Cloud Verification:** When a person wants to create or verify an Instagram account, their identity document is verified strictly within their **home country's designated Trusted Sovereign Cloud Provider** (1 trusted cloud custodian per country). **Zero raw PII or government ID data ever goes to Instagram or Meta.**

<img width="688" height="686" alt="Screenshot 2026-10-31 160200" src="https://github.com/user-attachments/assets/960ff1d0-e9e1-4a2c-b29b-aa230ad857c1" />
<img width="690" height="537" alt="Screenshot 2026-10-31 160302" src="https://github.com/user-attachments/assets/d7077e3e-8c63-4b81-90ae-635bbce9b37c" />
<img width="694" height="392" alt="Screenshot 2026-10-31 160344" src="https://github.com/user-attachments/assets/f5fa11ad-8469-4490-b4f2-546d509fcdb7" />

3. **Name & Age Matching + 18+ Hard Gate:** The agent cross-matches the user's legal **Name** and **Date of Birth / Age** with cryptographic validation proof:
   * **Under 18 Years Old (`Age < 18`):** The system triggers an automatic hard block. No Gatepass Key is generated, making it mathematically impossible for minors/children under 18 to create an unverified adult Instagram account.
   * **Verified Adult (`Age >= 18`):** The sovereign node generates a unique, anonymized **Sovereign Gatepass Key** accompanied by cryptographic validation proof.
4. **Zero-Knowledge Account Binding:** Instagram only receives the **Sovereign Gatepass Key**—confirming *"This is a verified, unique human over 18"* without Meta ever seeing the person's national ID.
5. **Global Purge of Existing Fake Accounts:** If Instagram announces a platform-wide rollout where all existing users must link their **Sovereign Gatepass Key**, every real human links their key once. **All remaining unlinked accounts are immediately exposed as bot swarms, clone accounts, or scammers**, allowing Instagram to wipe out fake accounts globally in a single sweep.


<img width="839" height="685" alt="Screenshot 2026-11-04 143030" src="https://github.com/user-attachments/assets/a0e1e8dd-7cec-4d3e-ac58-78bfbff850ad" />
<img width="870" height="547" alt="Screenshot 2026-11-04 143418" src="https://github.com/user-attachments/assets/4021c784-836b-40c7-a5be-d456e4cbe1ad" />
<img width="696" height="417" alt="Screenshot 2026-11-04 150236" src="https://github.com/user-attachments/assets/57803f9e-af91-430b-9104-68869919a88c" />
<img width="646" height="794" alt="Screenshot 2026-10-31 154007" src="https://github.com/user-attachments/assets/2e8b91ae-5619-4175-83c4-179cdec3e7b4" />

## Below 18+ users, the facemeinsta doesn't generate a gatepass key.
<img width="1134" height="595" alt="Screenshot 2026-11-04 150334" src="https://github.com/user-attachments/assets/522148cf-059a-45da-9d6c-69b10f04822e" />


### 🤖 Pillar 2: 24/7 Pre-Flight Guard Agent, 6-Frame Video Inspection & Human-in-the-Loop Admin Panel
Once a verified user enters Instagram, the **FACEmeInsta Guard Agent** (`core_engine.py`, `vision_hasher.py`, `meta_api_client.py`) works **24/7 as a pre-upload firewall** powered by **Meta (`meta-models/muse-spark-open-1026`) via Baseten API**.

#### Step-by-Step Workflow (Panel 2 & Admin Panel):
1. **Pre-Upload Interception (Before Going Public):** When a user clicks upload on a Reel, Video, or Post, the content does *not* go straight to the public feed. The Guard Agent intercepts the media + caption + `#strings` (hashtags) first.
2. **6-Frame Computer Vision Extraction (`vision_hasher.py`):** For every video or Reel, the engine extracts **6 key sequential frames** across the video timeline alongside perceptual visual hashes, preventing attackers from hiding toxic frames in the middle of a clip.
3. **Baseten + Meta Multimodal Analysis (`meta_api_client.py`):** Using the secure Baseten API key, the Guard Agent analyzes the 6 video frames, generates an automated **Video Description**, and compares the actual visual content against the user's **Caption and `#strings` (hashtags)** as well as scanning for **Phishing/Malicious Links**.
4. **Structured JSON Safety Telemetry & Risk Percentage Ranking:** The agent outputs a comprehensive **JSON security payload** containing:
   * Automated visual description of the 6-frame sequence
   * Semantic match score between the Video Content and the Caption / `#strings`
   * Phishing URL / malicious function detection status
   * Explicit hazard flags: **Nudity, Sexual Content, Child Abuse (CSAM), Violence, or Deepfake Impersonation**
   * Overall **Safety & Risk Percentage Rank (`0% - 100%`)**
5. **Automated Routing Decision:**
   * **✅ Path A — Clean & Matched Content (Direct Public Publish):** If the video content matches the caption/`#strings`, contains zero malicious links, and passes all safety checks, the Guard Agent grants **immediate direct access** to publish to Instagram.
   * **🚨 Path B — Unmatched `#strings` or Malicious/Unsafe Flag (Admin Panel Escalation):** If the video content contradicts the `#strings`/caption (bait-and-switch scam) or triggers any safety threshold, the upload is **held back** and routed with its 6-frame analysis and JSON report directly to the **Human Admin Review Panel**.
6. **Human Admin Final Verdict & User Notification (`audit_logger.py`):**
   * Inside the **Admin Panel**, a human reviewer inspects the 6 extracted frames, the AI-generated JSON safety breakdown, the risk percentage rank, and Instagram Policy alignment.
   * **If Approved:** The admin overrides the hold and publishes the post.
   * **If Rejected:** The content is permanently removed, the event is logged in the immutable audit trail (`audit_trail.json` & `facemeinsta_master.db`), and an **automated notification** explaining the exact policy violation is dispatched to the user's account.

<img width="1458" height="639" alt="Screenshot 2026-11-02 165115" src="https://github.com/user-attachments/assets/9ce8a838-c128-4891-8f71-a073019594b8" />
<img width="1528" height="724" alt="Screenshot 2026-11-02 165253" src="https://github.com/user-attachments/assets/844675cf-869d-46f9-93cc-7926a83e5d31" />
<img width="1474" height="687" alt="Screenshot 2026-11-02 165246" src="https://github.com/user-attachments/assets/e195f00d-385d-44fc-8e67-7ac2cbaaa356" />

## agent analysed the user content is safe and related to the caption.
<img width="1507" height="721" alt="Screenshot 2026-11-02 164556" src="https://github.com/user-attachments/assets/47409bac-18ec-49b4-9e85-1fb10b5d88b6" />
<img width="1375" height="586" alt="Screenshot 2026-11-02 165121" src="https://github.com/user-attachments/assets/b5097a3c-7779-4ac1-8e6d-8b6aac55f631" />

---

## 🤖 4. FACEmeInsta Copilot (Interactive Guard Agent)
Alongside automated pre-flight checks, **FACEmeInsta Copilot** (`app.py`) serves as an interactive, conversational cybersecurity assistant embedded directly into the platform:
* **For Everyday Users & Creators:** Explains why a post or `#string` was flagged, checks suspicious DMs/links on demand, and guides users through Sovereign Gatepass verification.
* **For Platform Admins & Trust Teams:** Summarizes 6-frame JSON telemetry, highlights high-risk percentage uploads first, and provides instant policy citations during human-in-the-loop reviews.

<img width="1504" height="595" alt="Screenshot 2026-11-03 153959" src="https://github.com/user-attachments/assets/ad5de910-0866-413f-ba65-a58547904c6b" />
<img width="1441" height="685" alt="Screenshot 2026-11-03 154009" src="https://github.com/user-attachments/assets/e3ad4500-42d4-47d8-bb68-10f3e3f668bc" />
<img width="1514" height="515" alt="Screenshot 2026-11-03 154017" src="https://github.com/user-attachments/assets/2b41c61a-e8db-4602-bd6a-f586470b8b36" />
---

## ⚔️ 5. Comparison: Legacy Instagram AI vs. FACEmeInsta Guard Agent Workflow

| Security Dimension | Legacy Instagram AI (Current Model) | 🛡️ FACEmeInsta Guard Agent Workflow (Our Solution) |
| :--- | :--- | :--- |
| **Core Philosophy** | Reactive moderation *after* content is uploaded and reported by victims. | **Proactive Pre-Flight Firewall** that inspects media and captions *before* public release. |
| **`#strings` (Hashtag) & Caption Scams** | Treats hashtags and video streams largely separately; easily gamed by bait-and-switch scammers stuffing trending `#strings` with phishing links. | **Semantic Cross-Modal Verification:** Extracts **6 video frames**, generates a visual description via Meta/Baseten, and verifies that the video genuinely matches the caption and `#strings`. |
| **Fake & Clone Account Detection** | Relies on behavioral heuristics after the fake account has already scammed followers. | **Sovereign Gatepass Key:** 1 verified adult human = 1 cryptographic key. Unlinked accounts are instantly isolated as fake/bot accounts. |
| **Underage (<18) Protection** | Easily bypassed self-reported birthdates; struggles to keep children under 18 off adult feeds. | **Cryptographic 18+ Hard Gate:** Name & age are validated at the country's Sovereign Cloud before a Gatepass Key is issued. Under-18 attempts are blocked at the door. |
| **User ID Privacy** | Requires uploading sensitive IDs directly to centralized social platform servers. | **Zero-Knowledge Sovereign Storage:** IDs stay strictly inside the resident's domestic Trusted Cloud company. Meta only receives an anonymous **Sovereign Gatepass Key**. |
| **CSAM / Nudity / Malicious Video Inspection** | Automated black-box strikes or delayed takedowns after viral spread. | **6-Frame Deep Scan + JSON Risk Ranking + Human Admin Escalation:** Holds suspect uploads, generates structured JSON telemetry & risk percentages, and routes mismatches to a Human Admin Panel with user notifications. |

---

## 🏗️ 6. Step-by-Step System Architecture Diagram

<pre>
====================================================================================================
                  🏛️ PILLAR 1: SOVEREIGN GATEPASS KEY & 18+ IDENTITY FIREWALL
====================================================================================================

  [New or Existing User]
           │
           ▼  (Submits Government ID, Name & Age)
  ┌──────────────────────────────────────────────────────────┐
  │  COUNTRY-DESIGNATED TRUSTED SOVEREIGN CLOUD              │
  │  (Strict Domestic Residency — Zero Raw ID Sent to Meta)  │
  │                                                          │
  │  1. Cross-Matches Legal Name + Date of Birth             │
  │  2. Evaluates Age Gate (Is User >= 18 Years Old?)        │
  └────────┬────────────────────────────────────────┬────────┘
           │                                        │
     [AGE < 18]                               [AGE >= 18]
           │                                        │
           ▼                                        ▼
  ┌─────────────────────────┐          ┌──────────────────────────────────────────┐
  │ ❌ ACCESS DENIED        │          │ ✅ GENERATES SOVEREIGN GATEPASS KEY      │
  │ Blocks Underage / Child │          │ + Cryptographic Validation Proof         │
  │ Account Creation        │          │ (Links to Real Account / Exposes Fakes)  │
  └─────────────────────────┘          └────────────────────┬─────────────────────┘
                                                            │
                                                            ▼
====================================================================================================
             🤖 PILLAR 2: 24/7 PRE-UPLOAD GUARD AGENT & 6-FRAME MULTIMODAL FIREWALL
====================================================================================================

  [Verified User Uploads Video/Reel + Caption + #strings + Links]
                                │
                                ▼
  ┌───────────────────────────────────────────────────────────────────────────────┐
  │  STEP 1: PERIMETER & 6-FRAME VISION ENGINE (coastal_guard.py / vision_hasher) │
  │  • Intercepts upload BEFORE public release                                    │
  │  • Extracts 6 Sequential Video Frames + Perceptual Hashes                     │
  │  • Scans caption & #strings for phishing URLs and malicious payloads          │
  └─────────────────────────────────────┬─────────────────────────────────────────┘
                                        │
                                        ▼
  ┌───────────────────────────────────────────────────────────────────────────────┐
  │  STEP 2: COGNITIVE AI INFERENCE (meta_api_client.py + Baseten API Key)        │
  │  • Model: meta-models/muse-spark-open-1026                                    │
  │  • Generates 6-Frame Video Description                                        │
  │  • Checks: Does Video Content match Caption & #strings?                       │
  │  • Scans for: Nudity, Sexual Content, Child Abuse (CSAM), Violence            │
  │  • Outputs: Structured JSON Report + Risk/Safety Percentage Rank (0-100%)     │
  └─────────────────┬───────────────────────────────────────────┬─────────────────┘
                    │                                           │
      [100% MATCHED & SAFE]                       [UNMATCHED #strings OR UNSAFE]
                    │                                           │
                    ▼                                           ▼
  ┌───────────────────────────────────┐       ┌───────────────────────────────────┐
  │ ✅ DIRECT PUBLIC ACCESS           │       │ 🚨 STEP 3: HUMAN ADMIN PANEL      │
  │ Content published immediately to  │       │ (core_engine.py / audit_logger.py)│
  │ Instagram Feed / Reels            │       │                                   │
  └───────────────────────────────────┘       │ • Admin reviews 6 frames + JSON   │
                                              │   report + Risk % against Policy  │
                                              └────────┬─────────────────┬────────┘
                                                       │                 │
                                                  [APPROVED]        [REJECTED]
                                                       │                 │
                                                       ▼                 ▼
                                              ┌──────────────┐  ┌─────────────────────────┐
                                              │ ✅ Published │  │ ❌ Content Removed      │
                                              │ to Public    │  │ + User Notification Sent│
                                              │ Feed         │  │ + Logged in SQLite/JSON │
                                              └──────────────┘  └─────────────────────────┘
</pre>

<img width="1672" height="941" alt="FACEmeInsta Trust   Safety Flow (1)" src="https://github.com/user-attachments/assets/7db88a24-e288-45c1-9eb4-9c19bf6332e1" />


---

## 🌍 7. Real-World Impact: What Changes If Meta Approves & Deploys FACEmeInsta Globally?
If Meta officially adopts and integrates the **FACEmeInsta** architecture across Instagram's 2+ billion users:

1. **Overnight Elimination of Bot Farms & Impersonation Scams:** By requiring existing and new accounts to bind a **Sovereign Gatepass Key**, millions of fake accounts, romance scammers, and celebrity impersonators that cannot produce a unique human gatepass are immediately identified and purged.
2. **100% Enforceable Child & Under-18 Safety:** Regulators worldwide are demanding real age verification without compromising citizen privacy. FACEmeInsta gives Meta a plug-and-play solution that mathematically prevents under-18 account creation while keeping citizen IDs inside domestic sovereign clouds.
3. **Death of `#strings` Phishing & Bait-and-Switch Reels:** Scammers can no longer hijack trending hashtags with unrelated videos and phishing links, because the **6-frame Baseten/Meta pre-flight check** catches semantic mismatches before a single user sees the post.
4. **Zero-Tolerance Pre-Emptive CSAM & Non-Consensual Nudity Blocking:** Explicit and abusive videos are stopped in the pre-upload buffer and routed to human admins with full JSON telemetry—preventing viral trauma before it happens.
5. **A New Golden Standard of Platform Trust:** Users can finally browse, shop, and connect knowing every verified account is a real adult human and every video matches its caption—transforming Instagram into the world's most trusted social network.

---

## 🧰 8. Tech Stack & Repository File Map

| File | Role in the FACEmeInsta Architecture |
| :--- | :--- |
| **`app.py`** | Main Streamlit production application hosting Panel 1 (Sovereign Gatepass), Panel 2 (24/7 Pre-Upload Guard Agent), the Human Admin Review Panel, and FACEmeInsta Copilot. |
| **`coastal_guard.py`** | Perimeter ingress shield handling initial `#strings` link scanning, rate checks, and Gatepass Key boundary validation. |
| **`vision_hasher.py`** | OpenCV & Pillow computer vision module that extracts the **6 sequential frames** from uploaded Reels/Videos and computes perceptual hashes. |
| **`meta_api_client.py`** | Secure OpenAI-compatible client connecting via `BASETEN_API_KEY` to Meta's `meta-models/muse-spark-open-1026` to generate video descriptions, JSON safety reports, and risk percentage scores. |
| **`core_engine.py`** | Central decision orchestrator routing matched content to public feeds and unmatched/unsafe content to the Admin Panel queue. |
| **`migration_manager.py`** | Manages Sovereign Gatepass Key bindings, SQLite3 database schemas (`facemeinsta_master.db`), and cross-platform identity state. |
| **`audit_logger.py` & `audit_trail.json`** | Immutable compliance logging system recording every AI JSON verdict, admin override, takedown, and user notification. |
| **`requirements.txt` & `runtime.txt`** | Cloud production config locking Python `3.11` and pre-compiled wheels for Streamlit Community Cloud. |

---

## 🚀 9. Quick Start Guide (Run Locally)

1. **Clone the Repository:**
   `git clone https://github.com/ramakotiabhi/FACEmeInsta.git && cd FACEmeInsta`
2. **Install Dependencies:**
   `pip install -r requirements.txt`
3. **Configure Your Baseten API Key:**
   Create `.streamlit/secrets.toml` and add: `BASETEN_API_KEY = "your_baseten_api_key_here"`
4. **Launch the Firewall:**
   `streamlit run app.py`

---
## 🏆 9. Hackathon Tracks & Ecosystem Alignment
1. **Primary Track — Autonomous Trust, Safety & Social Platform Defense:** End-to-end multimodal firewall protecting creators and everyday users on Instagram and cross-platform social networks.
2. **Meta Model Innovation Track:** Production integration of `meta-models/muse-spark-open-1026` as the core cognitive engine for nuanced safety reasoning and interactive Guard Agent workflows.
3. **Baseten Partner Infrastructure Track:** Leveraging Baseten's high-throughput OpenAI-compatible inference endpoints to achieve real-time protection without infrastructure bottlenecks.

---

## 🌍 10. Macro Impact: How Full Implementation Transforms Trust Across Instagram
If **FACEmeInsta**'s architecture is deployed at scale across Instagram's global user base:
* **🛡️ Instant Eradication of Clone & Scam Accounts:** Because our Sovereign Gatepass Key binds every real adult user (`18+`) via their domestic trusted cloud—and `vision_hasher.py`[cite: 13] + `migration_manager.py`[cite: 13] fingerprint creator media at creation—any existing unlinked fake account or scammer attempting to clone a real user is intercepted at the perimeter (`coastal_guard.py`)[cite: 13] and eliminated.
* **🔞 Mathematically Enforceable Child Safety (<18 Protection) with Zero Privacy Loss:** Minors under 18 are protected from creating unverified adult accounts, while adult citizens' IDs remain safely inside their country's trusted cloud provider rather than on Meta's servers.
* **🎣 Death of `#strings` Bait-and-Switch Scams & Pre-Emptive Hazard Blocking:** Scammers can no longer hijack trending hashtags with unrelated videos or phishing links, and explicit/CSAM content is caught during the **6-frame Baseten/Meta pre-upload scan** and routed to the **Human Admin Panel** before a single viewer is harmed.
* **💬 Psychological Safety for Creators & Youth:** The interactive **Instagram Guard Agent** and **FACEmeInsta Copilot** act as a 24/7 personal cybersecurity officer for every user—filtering out coordinated harassment, toxic DMs, and synthetic abuse in real time.
* **🔍 Accountable, Fair Moderation (Ending Unfair Shadowbans):** By backing every safety action and human admin review with `audit_logger.py`[cite: 13] and `audit_trail.json`[cite: 13], creators gain verifiable proof of content compliance and transparent notifications, replacing platform paranoia with fair governance.
* **📈 The Compounding Trust Network Effect:** In the advanced AI era, when users know that every account is backed by a Sovereign Gatepass Key and every video matches its `#strings` caption via a 24/7 autonomous firewall, **overall platform trust skyrockets**. Authentic human engagement replaces bot anxiety, and Instagram evolves into a verifiable, high-trust digital ecosystem.

## ❓ 10. Frequently Asked Questions (FAQs)

**Q1: Does Instagram or Meta ever see my Government ID or National Identity Card?**
> **No.** Under FACEmeInsta's Sovereign Architecture, your verification ID is processed and stored strictly within your home country's designated **Trusted Cloud Company**. Instagram/Meta only receives an anonymized cryptographic **Sovereign Gatepass Key** proving you are a unique adult (`18+`).

**Q2: How does FACEmeInsta stop existing fake accounts that are already on Instagram?**
> Instagram can announce a mandatory **Gatepass Key Link Window** for all accounts. Real users link their sovereign Gatepass Key in seconds. Any account that remains unlinked is automatically flagged as a fake, clone, or bot account and removed.

**Q3: Why does the Guard Agent extract 6 frames from a video instead of just checking the thumbnail?**
> Scammers often use a clean thumbnail and safe first second, then splice malicious, explicit, or unrelated scam content into the middle or end of a Reel. Extracting **6 evenly spaced frames** across the video allows Meta's multimodal model on Baseten to inspect the full narrative arc of the video and verify it against the `#strings` caption.

**Q4: What happens if a legitimate creator uses creative or abstract captions that don't literally match the video?**
> FACEmeInsta never blindly deletes ambiguous content! If the Guard Agent detects a mismatch between the 6-frame video description and the caption/`#strings`, it routes the post (along with the JSON analysis and risk percentage) to the **Human Admin Panel**. A human reviewer verifies context, approves legitimate creative posts, and only removes genuine policy violations or scams.

**Q5: How fast is the pre-upload check?**
> By combining fast local OpenCV 6-frame extraction (`vision_hasher.py`) with high-throughput **Baseten API** inference serving `meta-models/muse-spark-open-1026`, pre-flight evaluation completes in seconds.

---


<div align="center">
  <b>Built by Abhiram Sharma Ramakoti — Securing the Future of Social Media in the AI Era</b><br>
  <a href="https://facemeinsta-g5zsuknlwywobur4rwmmtn.streamlit.app">🌐 Live Streamlit App</a> •
  <a href="https://youtu.be/2YXOH9TS9Hk">🎥 3-Min YouTube Demo</a> •
  <a href="https://github.com/ramakotiabhi/FACEmeInsta">📂 GitHub Repository</a>
</div>
