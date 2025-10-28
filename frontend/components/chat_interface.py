"""
Chat Interface Component
Renders the chat UI using HTML/CSS/JS within a Streamlit iframe
"""

import streamlit as st
import streamlit.components.v1 as components
import base64
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api_service import APIService
    from .theme_manager import ThemeManager

class ChatInterface:
    """Chat interface component with theme support and API integration"""
    
    def __init__(self, api_service: 'APIService', theme_manager: 'ThemeManager'):
        """
        Initialize chat interface
        
        Args:
            api_service: API service instance for backend communication
            theme_manager: Theme manager instance for theme switching
        """
        self.api_service = api_service
        self.theme_manager = theme_manager
        self._ensure_chat_state()
    
    def _ensure_chat_state(self):
        """Initialize chat-related session state"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "progress" not in st.session_state:
            st.session_state.progress = {
                "intro": False,
                "experience": False,
                "skills": False,
                "goals": False
            }
    
    def render(self):
        """Render the chat interface"""
        # Check API health
        if not self.api_service.health_check():
            st.error("🔴 Backend service is not available. Please check the connection.")
            return
        
        # Load and render chat HTML
        try:
            html_content = self._load_chat_html()
            self._render_chat_iframe(html_content)
        except Exception as e:
            st.error(f"❌ Failed to load chat interface: {e}")
            self._render_fallback_chat()
    
    def _load_chat_html(self) -> str:
        """Load the chat HTML template"""
        html_path = "assets/chat_ui.html"
        
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            # Return embedded HTML if file doesn't exist
            return self._get_embedded_chat_html()
    
    def _render_chat_iframe(self, html_content: str):
        """Render chat interface in an iframe with proper theme communication"""
        
        # Inject API base and session info
        api_script = f"""
        <script>
            window.API_BASE = '{self.api_service.api_base}';
            window.SESSION_ID = '{st.session_state.session_id}';
        </script>
        """
        
        # Inject the API script at the beginning of the HTML
        html_content = html_content.replace('<head>', f'<head>{api_script}')
        
        # Encode HTML for iframe
        encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
        
        # Create iframe with theme communication
        iframe_html = f"""
        <div id="chat-container" style="width: 100%; height: 600px;">
            <div id="iframe-container"></div>
        </div>
        
        <script>
        (function() {{
            const container = document.getElementById('iframe-container');
            const iframe = document.createElement('iframe');
            
            iframe.id = 'chat-iframe';
            iframe.src = 'data:text/html;base64,{encoded_html}';
            iframe.sandbox.add('allow-scripts', 'allow-same-origin', 'allow-forms');
            iframe.style.cssText = 'width:100%; height:600px; border:0; border-radius:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);';
            
            container.appendChild(iframe);
            
            // Send theme to iframe when ready
            iframe.onload = function() {{
                setTimeout(() => {{
                    iframe.contentWindow.postMessage({{
                        type: 'set-theme',
                        theme: '{self.theme_manager.get_current_theme()}'
                    }}, '*');
                }}, 100);
            }};
            
            // Handle messages from iframe
            window.addEventListener('message', function(event) {{
                if (event.data && event.data.type === 'chat-request') {{
                    // Forward to parent for API handling
                    console.log('Chat request received:', event.data);
                }}
            }});
        }})();
        </script>
        """
        
        # Render iframe
        components.html(iframe_html, height=650)
    
    def _render_fallback_chat(self):
        """Render a simple fallback chat interface using Streamlit components"""
        st.markdown("### 💬 Simple Chat Interface")
        st.info("Using fallback interface. For the full experience, ensure chat_ui.html is available.")
        
        # Display messages
        for message in st.session_state.messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            
            if role == "user":
                st.markdown(f"**You:** {content}")
            else:
                st.markdown(f"**Assistant:** {content}")
        
        # Input field
        user_input = st.text_input("Type your message:", key="fallback_input")
        
        if st.button("Send", key="fallback_send") and user_input.strip():
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Send to API
            with st.spinner("Thinking..."):
                response = self.api_service.send_message(user_input)
            
            if response["success"]:
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response["response"]
                })
            else:
                st.error(f"Error: {response['error']}")
            
            st.rerun()
    
    def _get_embedded_chat_html(self) -> str:
        """Get embedded chat HTML as fallback"""
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TalentScout AI Chat</title>
            <style>
                :root {
                    --primary-color: #2563eb;
                    --bg-primary: #ffffff;
                    --bg-secondary: #f8fafc;
                    --text-primary: #1e293b;
                    --text-secondary: #64748b;
                    --border-color: #e2e8f0;
                }
                
                [data-theme='dark'] {
                    --bg-primary: #0f172a;
                    --bg-secondary: #1e293b;
                    --text-primary: #f8fafc;
                    --text-secondary: #cbd5e1;
                    --border-color: #475569;
                }
                
                * { margin: 0; padding: 0; box-sizing: border-box; }
                
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                    background: var(--bg-primary);
                    color: var(--text-primary);
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                }
                
                .chat-header {
                    background: var(--bg-secondary);
                    padding: 1rem;
                    border-bottom: 1px solid var(--border-color);
                    text-align: center;
                }
                
                .chat-messages {
                    flex: 1;
                    padding: 1rem;
                    overflow-y: auto;
                }
                
                .message {
                    margin-bottom: 1rem;
                    padding: 0.75rem;
                    border-radius: 8px;
                    max-width: 80%;
                }
                
                .message.user {
                    background: var(--primary-color);
                    color: white;
                    margin-left: auto;
                }
                
                .message.assistant {
                    background: var(--bg-secondary);
                    border: 1px solid var(--border-color);
                }
                
                .chat-input {
                    padding: 1rem;
                    border-top: 1px solid var(--border-color);
                    display: flex;
                    gap: 0.5rem;
                }
                
                input {
                    flex: 1;
                    padding: 0.75rem;
                    border: 1px solid var(--border-color);
                    border-radius: 6px;
                    background: var(--bg-primary);
                    color: var(--text-primary);
                    outline: none;
                }
                
                button {
                    padding: 0.75rem 1.5rem;
                    background: var(--primary-color);
                    color: white;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                }
                
                button:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                }
            </style>
        </head>
        <body data-theme="light">
            <div class="chat-header">
                <h2>🎯 TalentScout AI</h2>
                <p>Professional Hiring Assistant</p>
            </div>
            
            <div class="chat-messages" id="messages">
                <div class="message assistant">
                    <strong>TalentScout AI:</strong> Hello! I'm here to help with your professional interview. What's your name?
                </div>
            </div>
            
            <div class="chat-input">
                <input type="text" id="messageInput" placeholder="Type your message..." />
                <button id="sendButton" onclick="sendMessage()">Send</button>
            </div>
            
            <script>
                // Theme listener
                window.addEventListener('message', function(event) {
                    if (event.data && event.data.type === 'set-theme') {
                        document.body.setAttribute('data-theme', event.data.theme);
                    }
                });
                
                // Send message function
                function sendMessage() {
                    const input = document.getElementById('messageInput');
                    const message = input.value.trim();
                    
                    if (!message) return;
                    
                    // Add user message to UI
                    addMessage('user', message);
                    input.value = '';
                    
                    // Send to parent (Streamlit will handle API call)
                    window.parent.postMessage({
                        type: 'chat-request',
                        message: message
                    }, '*');
                }
                
                function addMessage(role, content) {
                    const messagesDiv = document.getElementById('messages');
                    const messageDiv = document.createElement('div');
                    messageDiv.className = `message ${role}`;
                    messageDiv.innerHTML = `<strong>${role === 'user' ? 'You' : 'TalentScout AI'}:</strong> ${content}`;
                    messagesDiv.appendChild(messageDiv);
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                }
                
                // Enter key support
                document.getElementById('messageInput').addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
            </script>
        </body>
        </html>
        '''