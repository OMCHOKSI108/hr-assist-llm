"""
API Service Component
Handles communication with the FastAPI backend
"""

import requests
import json
import os
import uuid
import streamlit as st
from typing import Dict, Any, Optional

class APIService:
    """Service class for backend API communication"""
    
    def __init__(self):
        """Initialize API service with base URL"""
        self.api_base = os.environ.get('API_BASE', 'http://localhost:8000')
        self._ensure_session_id()
    
    def _ensure_session_id(self):
        """Ensure session ID exists in session state"""
        if "session_id" not in st.session_state:
            st.session_state.session_id = str(uuid.uuid4())
    
    def send_message(self, message: str) -> Dict[str, Any]:
        """
        Send a chat message to the backend API
        
        Args:
            message: User message to send
            
        Returns:
            Dictionary containing response data
        """
        try:
            payload = {
                "user_input": message,
                "session_id": st.session_state.session_id
            }
            
            response = requests.post(
                f"{self.api_base}/chat",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Update session state with response data
                if "user_details" in data:
                    st.session_state.user_details = data["user_details"]
                
                return {
                    "success": True,
                    "response": data.get("response", ""),
                    "session_id": data.get("session_id", st.session_state.session_id),
                    "user_details": data.get("user_details", {})
                }
            else:
                return {
                    "success": False,
                    "error": f"API returned status code {response.status_code}",
                    "response": "Sorry, I'm having trouble connecting to the service."
                }
                
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timeout",
                "response": "Sorry, the response is taking too long. Please try again."
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Connection error", 
                "response": "Sorry, I can't connect to the service right now. Please check your connection."
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "response": "Sorry, something went wrong. Please try again."
            }
    
    def get_session_history(self) -> Dict[str, Any]:
        """
        Get chat history for the current session
        
        Returns:
            Dictionary containing session history
        """
        try:
            response = requests.get(
                f"{self.api_base}/sessions/{st.session_state.session_id}",
                timeout=10
            )
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "history": response.json()
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to fetch history: {response.status_code}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def health_check(self) -> bool:
        """
        Check if the API backend is healthy
        
        Returns:
            True if backend is accessible, False otherwise
        """
        try:
            response = requests.get(f"{self.api_base}/", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_api_info(self) -> Dict[str, Any]:
        """
        Get API information and status
        
        Returns:
            Dictionary containing API information
        """
        try:
            response = requests.get(f"{self.api_base}/", timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "API not accessible"}
        except Exception as e:
            return {"error": str(e)}