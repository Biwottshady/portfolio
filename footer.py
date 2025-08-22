# footer.py
import streamlit as st

def render_footer():
    st.markdown("""
    <style>
        .custom-footer {
            background: linear-gradient(to right, #2c3e50, #4ca1af);
            padding: 20px;
            color: white;
            text-align: center;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            margin-top: 3em;
        }
        .custom-footer a {
            color: #f1f1f1;
            text-decoration: none;
            margin: 0 10px;
        }
        .custom-footer a:hover {
            color: #ffd700;
        }
    </style>
    <div class="custom-footer">
        <strong>© 2025 Shadrack Kiprop</strong> — Data Analyst & Python Developer<br>
        <strong> Phone: 📞+254 706 501 644<strong>
        |
        <a href="mailto:biwottshadrack254@gmail.com">📧 biwottshadrack254@gmail.com</a>
        |
        <a href="https://www.linkedin.com/in/shadrackkiprop" target="_blank">🔗 LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)
