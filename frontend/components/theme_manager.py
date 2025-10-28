"""
Theme Manager Component
Handles dark/light mode switching with proper CSS variables and iframe communication
"""

import streamlit as st

class ThemeManager:
    """Manages application themes and communicates with iframe components"""
    
    def __init__(self):
        """Initialize theme manager with session state"""
        if "theme_mode" not in st.session_state:
            st.session_state.theme_mode = "light"
    
    def is_light_mode(self) -> bool:
        """Check if current theme is light mode"""
        return st.session_state.theme_mode == "light"
    
    def is_dark_mode(self) -> bool:
        """Check if current theme is dark mode"""
        return st.session_state.theme_mode == "dark"
    
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        st.session_state.theme_mode = "dark" if self.is_light_mode() else "light"
    
    def get_current_theme(self) -> str:
        """Get current theme mode"""
        return st.session_state.theme_mode
    
    def apply_theme(self):
        """Apply theme styles to the Streamlit app"""
        theme = self.get_current_theme()
        
        if theme == "dark":
            self._apply_dark_theme()
        else:
            self._apply_light_theme()
    
    def _apply_light_theme(self):
        """Apply light theme styles"""
        st.markdown("""
        <style>
            :root {
                --primary-color: #2563eb;
                --primary-dark: #1d4ed8;
                --secondary-color: #64748b;
                --success-color: #10b981;
                --warning-color: #f59e0b;
                --error-color: #ef4444;
                
                --bg-primary: #ffffff;
                --bg-secondary: #f8fafc;
                --bg-tertiary: #f1f5f9;
                --text-primary: #1e293b;
                --text-secondary: #475569;
                --text-muted: #64748b;
                --border-color: #e2e8f0;
                
                --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
                --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }
            
            .stApp {
                background: var(--bg-primary);
                color: var(--text-primary);
            }
            
            .sidebar .sidebar-content {
                background: var(--bg-secondary);
                border-right: 1px solid var(--border-color);
            }
            
            .main .block-container {
                background: var(--bg-primary);
                padding: 1rem;
            }
        </style>
        """, unsafe_allow_html=True)
    
    def _apply_dark_theme(self):
        """Apply dark theme styles"""
        st.markdown("""
        <style>
            :root {
                --primary-color: #3b82f6;
                --primary-dark: #2563eb;
                --secondary-color: #94a3b8;
                --success-color: #10b981;
                --warning-color: #f59e0b;
                --error-color: #ef4444;
                
                --bg-primary: #0f172a;
                --bg-secondary: #1e293b;
                --bg-tertiary: #334155;
                --text-primary: #f8fafc;
                --text-secondary: #cbd5e1;
                --text-muted: #94a3b8;
                --border-color: #475569;
                
                --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
                --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
                --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            }
            
            .stApp {
                background: var(--bg-primary) !important;
                color: var(--text-primary) !important;
            }
            
            .sidebar .sidebar-content {
                background: var(--bg-secondary) !important;
                border-right: 1px solid var(--border-color);
                color: var(--text-primary) !important;
            }
            
            .main .block-container {
                background: var(--bg-primary) !important;
                color: var(--text-primary) !important;
                padding: 1rem;
            }
            
            /* Dark theme for Streamlit components */
            .stSelectbox > div > div {
                background-color: var(--bg-secondary) !important;
                color: var(--text-primary) !important;
            }
            
            .stButton > button {
                background-color: var(--bg-secondary) !important;
                color: var(--text-primary) !important;
                border: 1px solid var(--border-color) !important;
            }
            
            .stButton > button:hover {
                background-color: var(--bg-tertiary) !important;
                border-color: var(--primary-color) !important;
            }
        </style>
        """, unsafe_allow_html=True)
    
    def get_theme_message_data(self) -> dict:
        """Get theme data for iframe communication"""
        return {
            "type": "set-theme",
            "theme": self.get_current_theme()
        }