import streamlit as st


# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="Email Anarchy", page_icon="📨", layout="wide", initial_sidebar_state="collapsed")

# ---- MAIN BODY ----
with st.container():
    st.markdown("[About Us](#about-us)", unsafe_allow_html=True)
    st.markdown("[Open Source Projects](#open-source-projects)", unsafe_allow_html=True)

    with st.container():
        st.header("Pricing", divider=True)
        st.html("""
            <center>Choose what works best for you.</center>
            """)
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

        entry, mid, annual = st.columns(3)
        with entry:
            with st.container(horizontal=False, border=False):
                st.markdown('<div class="custom-container"><center>5 Day Access'
                            '<h2>$10</h2>'
                            'Unsubscribe, Block, Mass Delete</center></div>', unsafe_allow_html=True)

        with mid:
            with st.container(horizontal=False, border=False):
                st.markdown('<div class="custom-container"><center>1 Month Access'
                            '<h2>$20</h2>'
                            'Unsubscribe, Block, Mass Delete</center></div>', unsafe_allow_html=True)
        with annual:
            with st.container(horizontal=False, border=False):
                st.markdown('<div class="custom-container"><center>1 Year Access'
                            '<h2>$100</h2>'
                            'Unsubscribe, Block, Mass Delete</center></div>', unsafe_allow_html=True)
    with st.container():
        st.header("SystemsPro.Tech", divider=True)
        st.subheader("About Us")
        st.markdown("""
            EmailAnarchy was developed out of necessity establishing email 
            management features not already available to the consumer. 
            """)
        st.markdown("""
            SystemsPro aims to provide services and tools that serve you, 
            making life and work just a little bit easier.
            """)
        st.subheader("More About Us")
        st.markdown("""
            Just check us out at [SystemsPro.Tech](https://systemspro.tech/) 
            to see what else we have to offer.
            """)
    with st.container():
        st.header("Open Source Projects", divider=True)
        st.write("""
            This project is open source so to encourage a community to build around it.
            We hope to receive community input and more feature ideas!
            """)

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
        <center>Check out what else we're working on:</center>
        <center><a href=\"https://systemspro.tech\" style=\"color: white\";>SystemsPro.tech</a></center>
        """)