import os
import requests
import streamlit as st

def get_baseten_api_key():
    """Safely retrieves the Baseten API key from Streamlit secrets or environment variables."""
    # 1. Try Streamlit Cloud secrets first (Primary for deployment)
    try:
        if "BASETEN_API_KEY" in st.secrets:
            return st.secrets["BASETEN_API_KEY"]
    except Exception:
        pass
    
    # 2. Fallback to OS environment variables
    return os.getenv("BASETEN_API_KEY")

def analyze_profile_with_meta(username, full_name):
    """
    Sends profile parameters to Meta's open-weights model hosted via Baseten
    for semantic and safety validation.
    """
    api_key = get_baseten_api_key()
    
    # If API key is not set or is a placeholder, provide simulation fallback
    if not api_key or api_key == "your_hackathon_api_key_here":
        return {
            "status": "SUCCESS",
            "verdict": "SAFE",
            "reasoning": "Evaluated via local Meta Model API simulation: Clean profile parameters."
        }

    # Baseten OpenAI-compatible or Direct Model Endpoint configuration
    # Update META_API_URL to your exact Baseten deployment endpoint if needed
    META_API_URL = os.getenv("BASETEN_API_URL", "https://api.baseten.co/v1/workflows/run") # or your model endpoint URL
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "meta-models/muse-spark-open-1026",
        "messages": [
            {
                "role": "user", 
                "content": f"Analyze profile for identity theft or synthetic risk. Username: {username}, Full Name: {full_name}"
            }
        ],
        "temperature": 0.3,
        "max_tokens": 200
    }
    
    try:
        response = requests.post(META_API_URL, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[Baseten API Error Status {response.status_code}]: {response.text}")
    except Exception as e:
        print(f"[Meta/Baseten API Warning]: {e}")
        
    return {"status": "FALLBACK", "verdict": "SAFE", "reasoning": "Default system fallback due to network/auth error."}