import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from simple_salesforce import Salesforce

# Salesforce credentials
SF_USERNAME = 'your_salesforce_username'
SF_PASSWORD = 'your_salesforce_password'
SF_SECURITY_TOKEN = 'your_salesforce_security_token'

# Slack credentials
SLACK_BOT_TOKEN = 'your_slack_bot_token'
SLACK_CHANNEL_ID = 'your_slack_channel_id'

# Connect to Salesforce
sf = Salesforce(username=SF_USERNAME, password=SF_PASSWORD, security_token=SF_SECURITY_TOKEN)

# Initialize Slack client
slack_client = WebClient(token=SLACK_BOT_TOKEN)

def get_latest_slack_message():
    try:
        result = slack_client.conversations_history(channel=SLACK_CHANNEL_ID, limit=1)
        return result['messages'][0]['text']
    except SlackApiError as e:
        print(f"Error fetching Slack message: {e}")
        return None

def add_comment_to_salesforce_ticket(ticket_id, comment):
    try:
        sf.Case.update(ticket_id, {'Comments': comment})
        print(f"Comment added to Salesforce ticket {ticket_id}")
    except Exception as e:
        print(f"Error adding comment to Salesforce ticket: {e}")

def main():
    # Get the latest message from Slack
    slack_message = get_latest_slack_message()
    if not slack_message:
        return

    # Assuming the Slack message format is: "SF-12345: This is the comment"
    ticket_id, comment = slack_message.split(': ', 1)

    # Add the comment to the Salesforce ticket
    add_comment_to_salesforce_ticket(ticket_id, comment)

if __name__ == "__main__":
    main()