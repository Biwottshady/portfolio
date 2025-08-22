# header.py
import streamlit as st

def render_header(title="Shadrack Kiprop | Data Analyst & Developer"):
    st.markdown(f"""
    <style>
        .custom-header {{
            background: linear-gradient(to right, #4ca1af, #2c3e50);
            padding: 1.5rem;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            text-align: center;
            color: white;
        }}
        .custom-header h1 {{
            margin: 0;
            font-size: 2.2rem;
            font-weight: 800;
        }}
        .custom-header p {{
            margin: 0.2rem;
            font-size: 1.1rem;
            font-weight: 300;
        }}
    </style>
    <div class="custom-header">
        <h1>{title}</h1>
        <p>Transforming data into decisions with Python, Power BI, Excel, and Automation</p>
    </div>
    """, unsafe_allow_html=True)
