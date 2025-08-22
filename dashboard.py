import streamlit as st

# Set page config
st.set_page_config(page_title="Shadrack's Projects", layout="wide")

from header import render_header
render_header()

# Title and description
st.title("📂 My Projects")
st.markdown("Explore a selection of the data, automation, and visualization projects I've worked on.")

# Define a list of projects
projects = [
    {
        "title": "🧾 Automated Invoicing System in Google Sheets",
        "description": "Built a fully automated invoicing tool using Google Apps Script, which generates PDF invoices and saves them in Google Drive.",
        "link": "https://your-link-to-demo-or-code.com"
    },
    {
        "title": "📊 County Revenue Dashboard (ERT Machines)",
        "description": "Developed a real-time dashboard showing locations and collections from ERT revenue machines, using Excel and Power BI integration.",
        "link": "https://your-link-to-dashboard-or-sample.com"
    },
    {
        "title": "🌳 Tree Growth Predictor",
        "description": "Python-based model to predict tree growth trajectory using nursery data and visualize projected heights over time.",
        "link": "https://your-link-to-code-or-presentation.com"
    },
    {
        "title": "🧠 OCR-based Data Extraction",
        "description": "Extracted structured and unstructured data from images and PDFs using Python OCR and saved results in Excel.",
        "link": "https://your-link-to-github-or-demo.com"
    },
    {
        "title": "💬 ChatGPT-powered Assistant in Streamlit",
        "description": "Built a chatbot app that allows users to interact with a custom assistant using OpenAI GPT-3.5 inside a Streamlit UI.",
        "link": "https://your-link-if-available.com"
    },
]

# Display each project in a card style
for project in projects:
    st.markdown("---")
    st.subheader(project["title"])
    st.write(project["description"])
    if project["link"]:
        st.markdown(f"[🔗 View More]({project['link']})", unsafe_allow_html=True)

# Optionally, add a footer
st.markdown("---")
st.markdown("🌐 Contact me for collaborations or to view more detailed project breakdowns.")

from footer import render_footer
render_footer()

