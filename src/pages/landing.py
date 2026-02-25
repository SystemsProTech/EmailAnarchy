from streamlit_gsheets import GSheetsConnection
import pandas as pd
import streamlit as st


# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="Email Anarchy", page_icon="📨", layout="centered", initial_sidebar_state="collapsed")

# ---- SITE GOAL ----
st.markdown("""
    <style>
    /* The orange bar fill */
    .stProgress > div > div > div > div {
        background-color: #FF8038;
    }
    /* Gray percentage text */
    .gray-text {
        color: #808495;
        font-size: 0.8rem;
        font-family: 'Space Grotesk', sans-serif;
    }
    /* The Cyan/Blue status text */
    .status-cyan {
        color: #76FFF3;
        font-size: 0.8rem;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Progress Bar Layout
# 1. Percentage labels
col_left, col_right = st.columns([1, 11])
with col_left:
    st.markdown('<p class="gray-text">7%</p>', unsafe_allow_html=True)
with col_right:
    st.markdown('<p class="status-cyan" style="text-align: right;">73,042</p>', unsafe_allow_html=True)

# 2. The Actual Bar
st.progress(7)

# 3. The status message below
st.markdown('<p class="status-cyan">SITE GOAL: 1,000,000 deleted emails!</p>', unsafe_allow_html=True)

# ---- MAIN BODY ----
with st.container(horizontal_alignment="center"):
    st.html("""<center>
    <h1>Quickly Cleanup Your Gmail!</h1>
    <p>Escape email anarchy!<br> 
    Quickly unsubscribe, block, and mass delete emails.</p>
    <p>No signup! Just log in directly with your Gmail account.</p>
    </center>""")

    st.markdown("""
        <style>
        .custom-container {
            background-color: #1A1C24; /* Secondary background from mockup */
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #262730; /* Optional subtle border */
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    users, deletes, unsub = st.columns(3)
    with users:
        with st.container(horizontal=False, border=False):
            st.markdown('<div class="custom-container">Unique User Logins'
                        '<h2>2,345</h2></div>', unsafe_allow_html=True)

    with deletes:
        with st.container(horizontal=False, border=False):
            st.markdown('<div class="custom-container">Total Deleted Emails'
                        '<h2>201,872,001</h2></div>', unsafe_allow_html=True)
    with unsub:
        with st.container(horizontal=False, border=False):
            st.markdown('<div class="custom-container">Senders Unsubscribed or Blocked'
                        '<h2>34,503</h2></div>', unsafe_allow_html=True)

    st.divider()

# ---- FOOTER ----

org, links, something = st.columns(3)
with org:
    with st.container(horizontal=True):
        st.html("""
                <center>This Project Is Currently Open Source:<br>
                <a href=\"https://github.com/SystemsProTech/EmailAnarchy\" style=\"color: white\";>SystemsProTech/EmailAnarchy</a><br><br>
                Developed by:<br>
                <a href=\"https://systemspro.tech\" style=\"color: white\";>SystemsPro.tech</a></center>
                """)
with links:
    with st.container(horizontal=True):
        st.html("""
        <center>
            Follow and Connect<br>
            <a href="https://medium.com/automate-everything">
                <img src="https://img.icons8.com/?size=100&id=114433&format=png&color=000000>" width="40"/>
            </a>
            <a href="https://x.com/yery_odell">
                <img src="https://img.icons8.com/?size=100&id=01GWmP9aUoPj&format=png&color=000000>" width="40"/>
            </a>
            <a href="https://www.linkedin.com/in/yery-odell-a0a58355/">
                <img src="https://img.icons8.com/?size=100&id=98960&format=png&color=000000" width="40"/>
            </a>
            <a href="mailto:yery.odell@gmail.com">
                <img src="https://img.icons8.com/?id=Y2GfpkgYNp42&format=png&color=000000" width="40"/>
            </a>
            </center>
        """)
with something:
    with st.container(horizontal=True):
        st.html("""
        <center>Like this tool?</center>
        <center>Checkout what else is brewing at:</center>
        <center><a href=\"https://systemspro.tech\" style=\"color: white\";>SystemsPro.tech</a></center>
        """)