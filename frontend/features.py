"""
Feature Flag Management System
Advanced feature toggle system for controlled feature rollout and A/B testing
"""
from typing import Dict, Any, Optional
from backend.config import config, feature_flags
import streamlit as st

class FeatureManager:
    """Advanced feature management system with user targeting and rollout control"""

    @staticmethod
    def is_enabled(feature_name: str, user_context: Optional[Dict[str, Any]] = None) -> bool:
        """
        Check if a feature is enabled for the current user/context

        Args:
            feature_name: Name of the feature to check
            user_context: Optional user context for advanced targeting

        Returns:
            bool: Whether the feature is enabled
        """
        # Check global feature flag
        if not feature_flags.is_feature_enabled(feature_name):
            return False

        # Advanced targeting logic can be added here
        # For now, just return the global flag
        return True

    @staticmethod
    def get_enabled_features(user_context: Optional[Dict[str, Any]] = None) -> list:
        """Get list of all enabled features for the current user/context"""
        enabled_features = []
        all_features = feature_flags.get_enabled_features()

        for feature in all_features:
            if FeatureManager.is_enabled(feature, user_context):
                enabled_features.append(feature)

        return enabled_features

    @staticmethod
    def conditional_render(feature_name: str, render_func, fallback_func=None, user_context: Optional[Dict[str, Any]] = None):
        """
        Conditionally render UI elements based on feature flags

        Args:
            feature_name: Feature to check
            render_func: Function to call if feature is enabled
            fallback_func: Optional function to call if feature is disabled
            user_context: Optional user context
        """
        if FeatureManager.is_enabled(feature_name, user_context):
            return render_func()
        elif fallback_func:
            return fallback_func()
        return None

class UIFeatureManager:
    """UI-specific feature management for Streamlit components"""

    @staticmethod
    def render_voice_interview_button():
        """Render voice interview button if feature is enabled"""
        def render_button():
            if st.button("🎤 Start Voice Interview", key="voice_interview"):
                st.info("Voice interview feature coming soon!")

        FeatureManager.conditional_render("voice_interviews", render_button)

    @staticmethod
    def render_advanced_analytics():
        """Render advanced analytics dashboard if feature is enabled"""
        def render_analytics():
            with st.expander("Advanced Analytics", expanded=False):
                st.write("Advanced analytics features:")
                st.write("- Candidate scoring trends")
                st.write("- Interview performance metrics")
                st.write("- Hiring funnel analysis")

        FeatureManager.conditional_render("advanced_analytics", render_analytics)

    @staticmethod
    def render_sentiment_analysis():
        """Render sentiment analysis if feature is enabled"""
        def render_sentiment():
            st.caption("💭 Sentiment Analysis: Positive")

        FeatureManager.conditional_render("sentiment_analysis", render_sentiment)

    @staticmethod
    def render_multi_language_selector():
        """Render language selector if multi-language feature is enabled"""
        def render_selector():
            languages = ["English", "Spanish", "French", "German", "Chinese"]
            selected_lang = st.selectbox("🌐 Language", languages, key="language_selector")
            if selected_lang != "English":
                st.info(f"Multi-language support for {selected_lang} coming soon!")

        FeatureManager.conditional_render("multi_language", render_selector)

class APIFeatureManager:
    """API-specific feature management"""

    @staticmethod
    def enable_rate_limiting():
        """Check if API rate limiting should be enabled"""
        return FeatureManager.is_enabled("api_rate_limiting")

    @staticmethod
    def enable_audit_logging():
        """Check if audit logging should be enabled"""
        return FeatureManager.is_enabled("audit_logging")

    @staticmethod
    def enable_multi_tenant():
        """Check if multi-tenant features should be enabled"""
        return FeatureManager.is_enabled("multi_tenant")

# Global instances
feature_manager = FeatureManager()
ui_feature_manager = UIFeatureManager()
api_feature_manager = APIFeatureManager()

def initialize_feature_flags():
    """Initialize feature flags in Streamlit session state"""
    if 'feature_flags_initialized' not in st.session_state:
        st.session_state.feature_flags_initialized = True
        st.session_state.enabled_features = feature_flags.get_enabled_features()

        # Log enabled features for debugging
        if config.DEBUG:
            print(f"Enabled features: {st.session_state.enabled_features}")

# Initialize on import
if __name__ != "__main__":
    try:
        initialize_feature_flags()
    except:
        pass  # Streamlit context not available during import

