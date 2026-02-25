from datetime import datetime
import pandas as pd
import streamlit as st
import utils.tasks as tasks

st.title("Email Anarchy")

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            padding-top: 2rem; /* Add some space above the logo */
        }
        [data-testid="stSidebar"] [data-testid="stImage"] {
            display: flex;
            justify-content: center;
            padding: 20px;
            background-color: #FF8038;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.image("src/resources/bw_emailanarchy.png", width=200) # Adjust width as needed for your 320x320 file

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    oauth2 = tasks.oauth_instance()
    st.write("Login with Gmail")
    result = oauth2.authorize_button(
        name="Login",
        redirect_uri=st.session_state.REDIRECT_URI,
        icon="https://www.google.com.tw/favicon.ico",
        scope=st.session_state.SCOPE,
        height=400,
        width=300,
        key="google",
        extras_params={"prompt": "consent", "access_type": "offline"},
        use_container_width=False,
        pkce='S256',
    )

    if result and 'token' not in st.session_state:
        st.session_state["token"] = result.get("token")
        st.session_state.logged_in = True
        st.session_state.cart = False

        # Get User Data
        user_info = tasks.get_user_info(token=st.session_state["token"])
        if 'user_name' not in st.session_state:
            st.session_state.user_name = user_info['given_name']
        if 'user_email' not in st.session_state:
            st.session_state.user_email = user_info['email']

        # Get Total inbox size (int)
        st.session_state.inbox_size = tasks.get_messages_total(token=st.session_state["token"])

        # Log it
        # ---- FETCH GSHEET DATA ----
        user_login = st.session_state.sheet_con.read(worksheet="Login", usecols=list(range(4)), ttl=5)
        user_login = user_login.dropna(how="all")
        # Get the current date and time
        now = datetime.now()
        # Extract the date part
        date = now.date()
        # Extract only the time part from the datetime object
        current_time = now.time()
        # format the time as a string
        time = now.strftime("%H:%M:%S")
        new_login = pd.DataFrame(
            [
                {
                    "email": st.session_state.user_email,
                    "date": date,
                    "time": time,
                    "total_emails": st.session_state.inbox_size,
                }
            ]
        )
        # join existing data with new login info
        user_login = pd.concat([user_login, new_login], ignore_index=True)

        # Update Google Sheets with the new data
        st.session_state.sheet_con.update(worksheet="Login", data=user_login)
        st.rerun()

def logout():
    if st.button("Log out"):
        # remove all keys from session_state
        keys = list(st.session_state.keys())
        for key in keys:
            st.session_state.pop(key)
        st.rerun()

about = st.Page("pages/about.py", title="About", icon="ℹ")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
cart = st.Page("pages/cart.py", title="Pending Actions", icon="✔️")
landing_page = st.Page("pages/landing.py", title="Home", icon=":material/login:", default=True)
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


if st.session_state.logged_in and st.session_state.cart:
    pg = st.navigation(
        {
            "Account": [logout],
            "Navigation": [cart, dashboard, landing_page, about],
        }
    )
elif st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout],
            "Navigation": [dashboard, landing_page, about],
        }
    )
else:
    pg = st.navigation(
        {
            "Account": [login],
            "Navigation": [landing_page, about],
        })

pg.run()