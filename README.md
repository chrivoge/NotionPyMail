# Python - Notion E-Mail Database Update 
A Python implementation of the Notion database email update notifier [[1]](https://github.com/makenotion/notion-sdk-js/tree/main/examples/database-email-update).

Uses Notion and SendGrid APIs to continuously check the value for a given select property in a Notion database and sends an E-Mail to inform the user if the value of that property has been changed.

## Installation 

1. Clone repository `git clone https://github.com/chrivoge/NotionPyMail.git`
2. Switch into project `cd NotionPyMail`
3. Install dependencies  `pip install -r requirements.txt`
4. Create a Notion [API key](https://www.notion.com/my-integrations) and paste the integration token to config.py
5. Create free [SendGrid account](https://signup.sendgrid.com/), set up a single sender API and paste the API key to config.py
6. Duplicate [this](https://www.notion.com/5b593126d3eb401db62c83cbe362d2d5?v=a44397b3675545f389a6f28282c402ae) Notion database for testing purposes or use your own. If you use your own, make sure that it contains a select property.
7. Connect the database to your Notion integration and paste the database id to config.py (See also Notion [documentation](https://developers.notion.com/docs/getting-started#share-a-database-with-your-integration) for further guidance)
8. Add sender email used in SendGrid as well as the desired recipient email to config.py

## Usage

1. Run `run.py` 
2. If the value of the given property is changed, an email is sent to the recipient 
