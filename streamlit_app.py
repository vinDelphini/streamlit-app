import streamlit as st

# --- PAGE SETUP ---

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    # icon=":material/account_circle:",
    icon="⭕",
    default=True
)
project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    # icon=":material/bar_chart:",
    icon="📊"
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    # icon=":material/smart_toy:",
    icon="🤖"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
# --- RUN NAVIGATION ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)

st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made with ❤️ by Vin")
pg.run()
