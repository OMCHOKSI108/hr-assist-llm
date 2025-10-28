"""
TalentScout AI - Professional Hiring Assistant
Clean, modular Streamlit application for HR recruitment interviews
"""

import streamlit as st
import os
import json
from components.theme_manager import ThemeManager
from components.chat_interface import ChatInterface
from components.api_service import APIService

# App Configuration
st.set_page_config(
    page_title="TalentScout AI - Professional Hiring Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize components
theme_manager = ThemeManager()
api_service = APIService()
chat_interface = ChatInterface(api_service, theme_manager)

def main():
    """Main application entry point"""
    
    # Apply current theme
    theme_manager.apply_theme()
    
    # Hide Streamlit default elements
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar with controls
    with st.sidebar:
        st.markdown("### 🎯 TalentScout AI")
        st.markdown("Professional Hiring Assistant")
        
        # Theme toggle
        if st.button(
            f"🌓 Switch to {'Dark' if theme_manager.is_light_mode() else 'Light'} Mode",
            help="Toggle between light and dark themes"
        ):
            theme_manager.toggle_theme()
            st.rerun()
        
        st.markdown("---")
        
        # Session info
        if "session_id" in st.session_state:
            st.markdown(f"**Session:** `{st.session_state.session_id[:8]}...`")
        
        # Progress indicators
        st.markdown("### 📊 Interview Progress")
        progress_data = st.session_state.get("progress", {})
        
        stages = [
            ("👋", "Introduction", "intro"),
            ("💼", "Experience", "experience"),
            ("🎯", "Skills", "skills"),
            ("📈", "Goals", "goals")
        ]
        
        for icon, label, key in stages:
            completed = progress_data.get(key, False)
            status = "✅" if completed else "⏳"
            st.markdown(f"{icon} {status} {label}")
    
    # Main content area
    st.markdown("## 💬 Professional Interview Chat")
    
    # Render chat interface
    chat_interface.render()

if __name__ == "__main__":
    main()