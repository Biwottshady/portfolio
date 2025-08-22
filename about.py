import streamlit as st
from PIL import Image

# Set page config first
st.set_page_config(page_title="Shadrack Kiprop – Data Solutions with Impact", layout="wide")

# Import reusable header and footer
from header import render_header
from footer import render_footer

render_header()

# Load image
image = Image.open("unnamed.jpg")  # Replace with your actual image path

# Custom CSS
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom right, #edf1f9, #d2e3f5);
            padding: 2rem;
            border-radius: 15px;
        }
        .main-title {
            font-size: 42px;
            font-weight: 800;
            color: #1c1c1c;
            margin-bottom: 0.3rem;
        }
        .main-subtitle {
            font-size: 20px;
            color: #444;
            margin-bottom: 2rem;
        }
        .section-title {
            font-size: 28px;
            font-weight: 700;
            color: #1c1c1c;
            margin-top: 2rem;
        }
        .subtitle {
            font-size: 18px;
            color: #333;
        }
        .skill-box {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 1rem;
            margin: 1rem 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        }
    </style>
""", unsafe_allow_html=True)

# Page Layout
st.markdown('<div class="main">', unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image(image, caption="Shadrack Kiprop", use_column_width=True)
with col2:
    st.markdown('<div class="main-title">Shadrack Kiprop – Data Solutions with Impact</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Transforming data into decisions using Python, Power BI, Excel, and cloud tools.</div>', unsafe_allow_html=True)

# About Me
st.markdown('<div class="section-title">👋 About Me</div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Hi, I\'m <strong>Shadrack Kiprop</strong> – a <strong>Data Analyst & Developer</strong> helping businesses turn raw data into clear insights. I specialize in <strong>Python, Excel, Power BI, and automation tools</strong>.</p>', unsafe_allow_html=True)

# Career Highlights
st.markdown('<div class="section-title">🏆 Career Highlights</div>', unsafe_allow_html=True)
st.markdown("""
<ul class="subtitle">
  <li>📈 Increased revenue visibility through real-time dashboards for local government.</li>
  <li>📊 Created over 30+ interactive dashboards using Excel & Power BI.</li>
  <li>🤖 Built automated reporting tools that saved 80% manual work hours.</li>
</ul>
""", unsafe_allow_html=True)

# Industries Worked With
st.markdown('<div class="section-title">🌍 Industries I’ve Worked With</div>', unsafe_allow_html=True)
st.markdown("""
<ul class="subtitle">
  <li>🏛️ Government & Education</li>
  <li>🌱 Environmental & Carbon Projects</li>
  <li>📦 Logistics & Inventory</li>
  <li>📲 Fintech & Mobile Apps</li>
</ul>
""", unsafe_allow_html=True)

# Tools
st.markdown('<div class="section-title">🛠️ Tools I Use Daily</div>', unsafe_allow_html=True)
st.markdown("""
<ul class="subtitle">
  <li>📌 Excel, Power BI, Google Sheets</li>
  <li>🐍 Python (Pandas, Streamlit, Selenium)</li>
  <li>☁️ Snowflake, Firebase, BigQuery</li>
  <li>💻 GitHub, Jupyter, VS Code</li>
</ul>
""", unsafe_allow_html=True)

# Services (optional – you can move this if needed)
st.markdown('<div class="section-title">🚀 What I Do</div>', unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown('<div class="skill-box">🧹 <strong>Data Cleaning & Analysis</strong><br>Turn messy data into reliable insights.</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">📄 <strong>Google Sheets + Apps Script</strong><br>Automate reports and workflows using cloud tools.</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="skill-box">📊 <strong>Dashboard Design</strong><br>Create insightful dashboards using Excel & Power BI.</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">❄️ <strong>Snowflake & Streamlit Apps</strong><br>Build interactive data apps with cloud queries.</div>', unsafe_allow_html=True)

st.markdown('<div class="skill-box">🔍 <strong>Web Scraping & Automation</strong><br>Extract and structure data using Python & Selenium.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

render_footer()
