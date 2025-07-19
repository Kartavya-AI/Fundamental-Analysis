#!/usr/bin/env python
import streamlit as st
import warnings
from datetime import datetime
from fundamental_analyst.crew import FundamentalAnalyst
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

st.set_page_config(page_title="Company Fundamental Analyst", layout="centered")


def run_crew(company_name: str):
    """Kick off the CrewAI process"""
    inputs = {
        'company_name': company_name,
        'current_year': str(datetime.now().year)
    }

    with st.spinner(f"Running Fundamental Analysis for {company_name}..."):
        try:
            FundamentalAnalyst().crew().kickoff(inputs=inputs)
            return "report.md"
        except Exception as e:
            st.error(f"❌ Error occurred: {e}")
            return None


# UI
st.title("📊 Fundamental Company Analysis")
st.markdown("This app performs a full fundamental analysis using CrewAI and displays the final report.")

company_name = st.text_input("Enter a Company Name:", value="Tata Consultancy Services")

if st.button("🔍 Run Analysis"):
    report_path = run_crew(company_name)

    if report_path and os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            report_md = f.read()

        st.success("✅ Analysis completed. Here's your report:")
        st.markdown(report_md, unsafe_allow_html=True)
    elif report_path:
        st.warning("Report file not found. Please check if the crew ran correctly.")
