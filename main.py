import streamlit as st


# Navigation in sidebar
about_page = st.Page(page="D:/streamlit/about.py",
                    title="About Me",
                    icon="🤵"
                    )
chartbot_page = st.Page(page="D:/streamlit/chartbot.py",
                    title="ChartBot",
                    icon="🔩"
                    )
dashboard_page = st.Page(page="D:/streamlit/dashboard.py",
                    title="Dashboard",
                    icon="📊")

pg=st.navigation({"Info":[about_page],
                  "Projects":[chartbot_page,dashboard_page],})


pg.run()