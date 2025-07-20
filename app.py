#!/usr/bin/env python
import streamlit as st
import warnings
from datetime import datetime
from fundamental_analyst.crew import FundamentalAnalyst
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Page configuration with custom styling
st.set_page_config(
    page_title="Company Fundamental Analyst", 
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 10px;
    }
    
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        border: none;
    }
    
    .info-box h3 {
        color: white !important;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .info-box p {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(116, 185, 255, 0.3);
        margin: 0.5rem 0;
        border: none;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(116, 185, 255, 0.4);
    }
    
    .feature-card h4 {
        color: white !important;
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    .feature-card p {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1rem;
        margin: 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .analysis-header {
        background: linear-gradient(135deg, #74b9ff, #0984e3);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


def run_crew(company_name: str):
    """Kick off the CrewAI process"""
    inputs = {
        'company_name': company_name,
        'current_year': str(datetime.now().year)
    }

    with st.spinner(f"🔍 Analyzing {company_name}... This may take a few minutes."):
        try:
            FundamentalAnalyst().crew().kickoff(inputs=inputs)
            return "report.md"
        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")
            st.info("💡 **Troubleshooting Tips:**\n- Check if the company name is spelled correctly\n- Ensure you have internet connection\n- Try again in a few minutes")
            return None


# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Fundamental Company Analysis</h1>
    <p style="font-size: 1.1rem; margin-top: 10px;">AI-Powered Financial Analysis using CrewAI</p>
</div>
""", unsafe_allow_html=True)

# Info section
st.markdown("""
<div class="info-box">
    <h3>🎯 What does this tool do?</h3>
    <p>This application performs comprehensive fundamental analysis of public companies using AI agents. 
    Get detailed insights into financial health, market position, and investment potential.</p>
</div>
""", unsafe_allow_html=True)

# Features section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>📈 Financial Metrics</h4>
        <p>Revenue, profitability, and growth analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🔍 Market Analysis</h4>
        <p>Industry position and competitive landscape</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>📊 Investment Insights</h4>
        <p>Risk assessment and recommendations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# API Configuration Section
st.markdown("### 🔧 API Configuration")
st.markdown("Configure your API keys for the analysis to work properly.")

col1, col2 = st.columns(2)

with col1:
    # Gemini API Key
    gemini_key = st.text_input(
        "🤖 Gemini API Key",
        type="password",
        value=st.session_state.get("GEMINI_API_KEY", ""),
        placeholder="Enter your Gemini API key",
        help="Enter your Google Gemini API key for AI analysis"
    )

with col2:
    # Serper API Key
    serper_key = st.text_input(
        "🔍 Serper API Key",
        type="password",
        value=st.session_state.get("SERPER_API_KEY", ""),
        placeholder="Enter your Serper API key",
        help="Enter your Serper API key for web search capabilities"
    )

# Save Settings Button
if st.button("💾 Save API Settings", key="save_settings"):
    updated = False
    
    if gemini_key:
        st.session_state["GEMINI_API_KEY"] = gemini_key
        os.environ["GEMINI_API_KEY"] = gemini_key
        os.environ["MODEL"] = "gemini/gemini-2.5-flash-preview-05-20"
        updated = True
    
    if serper_key:
        st.session_state["SERPER_API_KEY"] = serper_key
        os.environ["SERPER_API_KEY"] = serper_key
        updated = True
    
    if updated:
        st.success("✅ API settings saved successfully!")
    else:
        st.warning("⚠️ Please enter at least one API key to save.")

st.markdown("---")

# Input section
st.markdown("### 🏢 Enter Company Details")
st.markdown("Enter the full company name for the most accurate analysis.")

# Company input with better styling
company_name = st.text_input(
    "Company Name:",
    value="Tata Consultancy Services",
    placeholder="e.g., Apple Inc., Microsoft Corporation, Tesla Inc.",
    help="Enter the official company name. For best results, include 'Inc.', 'Ltd.', or 'Corp.' if applicable."
)

# Add example companies
st.markdown("**💡 Popular examples:** Apple Inc., Microsoft Corporation, Google (Alphabet), Amazon, Tesla Inc.")

st.markdown("---")

# Analysis section
if st.button("🚀 Start Fundamental Analysis", type="primary"):
    if company_name.strip():
        # Display analysis info
        st.markdown(f"""
        <div class="analysis-header">
            <h3>🔍 Analyzing: {company_name}</h3>
            <p>Our AI agents are gathering and analyzing data...</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress information
        with st.expander("📋 What's happening during analysis?", expanded=False):
            st.markdown("""
            - **🌐 Data Collection:** Gathering financial statements and market data
            - **📊 Financial Analysis:** Calculating key ratios and metrics
            - **🏭 Industry Research:** Analyzing sector trends and competition
            - **📈 Valuation Models:** Running DCF and comparable analysis
            - **📝 Report Generation:** Compiling comprehensive analysis report
            """)
        
        report_path = run_crew(company_name)

        if report_path and os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                report_md = f.read()

            st.success("✅ Analysis completed successfully!")
            
            # Report section with better styling
            st.markdown("""
            <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h3 style="color: #2d5a2d;">📋 Fundamental Analysis Report</h3>
                <p style="color: #4a7c4a;">Your comprehensive company analysis is ready below.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add download option
            st.download_button(
                label="📥 Download Report",
                data=report_md,
                file_name=f"{company_name}_fundamental_analysis.md",
                mime="text/markdown",
                help="Download the complete analysis report"
            )
            
            st.markdown("---")
            st.markdown(report_md, unsafe_allow_html=True)
            
        elif report_path:
            st.warning("⚠️ Report file not found. Please check if the analysis completed correctly.")
            st.info("🔄 Try running the analysis again or contact support if the issue persists.")
    else:
        st.error("❌ Please enter a company name to proceed.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🤖 Powered by CrewAI • Built with Streamlit</p>
    <p style="font-size: 0.8rem;">For educational and informational purposes only. Not investment advice.</p>
</div>
""", unsafe_allow_html=True)