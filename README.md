# Email Anarchy
This web app allows you to hook into your gmail and perform bulk management functions such as:

- Unsubscribe from Multiple Senders
- Block Multiple Senders
- Bulk Delete All Emails from a Sender

Presently hosted SaaS at: [EmailAnarchy.com](https://emailanarchy.com)

## Docker Instructions:

`git clone git@github.com:SystemsProTech/EmailAnarchy.git`

`docker build -t systemsprotech/emailanarchy:latest -f EmailAnarchy/Dockerfile .`

`docker images -a`

`docker run -d -p 8501:8501 systemsprotech/emailanarchy`

`docker ps`

## Setting up Gmail APIs
Go to [Google Cloud APIs](https://cloud.google.com/apis/dashboard)

Once logged in, click on **Select a Project** and **New project**

Enter a **Project name** and select **Create**

Once the project is created and selected, use the Navigation Menu in the top-right hand corner of th screen.
Go to **APIs & Services**, and select **Library**

In the search feild for Apis & Services type: **Mail**

Select **GMail API** and **Enable**

## Create an OAuth Client
Next use the Navigation Menu in the top-right hand corner of th screen.
Go to **APIs & Services**, and select **OAuth consent screen**

Now click on **Get started**

Enter an **App Name** and **Email Address**, then select **Next**

For Audience select **External** and then **Next**

Once again enter an **Email Address** and select **Next**

Check **I agree** and hit **Continue**

Finally, select **Create**

Now click on **Create OAuth client**

Under **Application type** select **Web Application**

Provide a **Name**

For JavaScript origins,
**Add URI**: http://localhost:8501

For redirect URIs,
**Add URI**: http://localhost:8501/app

Click on **Create**

*Note: Be sure to take note of your **Client Secret** displayed or download the JSON file*

## Setup Data Access
Use the Navigation Menu in the top-right hand corner of th screen.
Go to **APIs & Services**, and select **OAuth consent screen**

Navigate to **Data Access** and select **Add or remove scopes**

Next to **Filter**, type and add the following: **userinfo**

Select both **email** and **profile**, then click **Update**

## Adding Test Users
Use the Navigation Menu in the top-right hand corner of th screen.
Go to **APIs & Services**, and select **OAuth consent screen**

Navigate to **Audience** and select under **Test user**, **Add users**

Add any email addresses that you would like to use the web app and select **Save**

## Adding a secrets.toml File
In **src/.streamlit/** create a **secrets.toml** file and include the following. 
Be sure to add your project info.

`[web]`

`client_id = <your client id>`

`project_id = <your project id>`

`auth_uri = "https://accounts.google.com/o/oauth2/auth"`

`token_uri = "https://oauth2.googleapis.com/token"`

`auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"`

`client_secret = <your client secret>`

`redirect_uris = ["http://127.0.0.1:8501"]`

`javascript_origins = ["http://127.0.0.1:8501"]`

## Deploying A Professional Streamlit SaaS Application
Full tutorial here: []()