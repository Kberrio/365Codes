import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from jira import JIRA

# Initialize the Slack app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Initialize the JIRA client
jira = JIRA(
    server="https://your-domain.atlassian.net",
    basic_auth=(os.environ.get("JIRA_EMAIL"), os.environ.get("JIRA_API_TOKEN"))
)

@app.command("/create-ticket")
def create_ticket(ack, command, say):
    ack()
    # Parse the command text for ticket details
    # Assuming format: "summary|description|issue_type"
    parts = command['text'].split('|')
    if len(parts) != 3:
        say("Invalid format. Please use: summary|description|issue_type")
        return

    summary, description, issue_type = parts

    # Create the ticket
    new_issue = jira.create_issue(
        project='YOUR_PROJECT_KEY',
        summary=summary,
        description=description,
        issuetype={'name': issue_type}
    )

    say(f"Ticket created: {new_issue.key}")

@app.command("/close-ticket")
def close_ticket(ack, command, say):
    ack()
    ticket_key = command['text']

    # Transition the ticket to 'Closed' status
    # Note: You need to know the transition ID for 'Closed' status in your JIRA workflow
    jira.transition_issue(ticket_key, '31')  # '31' is often the ID for 'Closed' status

    say(f"Ticket {ticket_key} has been closed.")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()