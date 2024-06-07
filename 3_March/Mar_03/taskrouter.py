from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Create a workspace (if not already created)
workspace = client.taskrouter.workspaces.create(friendly_name='My Workspace')

# Create a workflow
workflow = client.taskrouter.workspaces(workspace.sid).workflows.create(
    friendly_name='My Workflow',
    assignment_callback_url='http://example.com/assignment',
    fallback_assignment_callback_url='http://example.com/fallback',
    task_reservation_timeout='30'
)

# Create a task queue
queue = client.taskrouter.workspaces(workspace.sid).task_queues.create(
    friendly_name='My Queue',
    assignment_activity_sid='your_assignment_activity_sid',
    reservation_activity_sid='your_reservation_activity_sid',
    target_workers='languages HAS "english"'
)

# Create workers
worker1 = client.taskrouter.workspaces(workspace.sid).workers.create(
    friendly_name='Worker 1',
    attributes='{"languages":["english", "spanish"]}'
)
worker2 = client.taskrouter.workspaces(workspace.sid).workers.create(
    friendly_name='Worker 2',
    attributes='{"languages":["english", "french"]}'
)

# Create a task
task = client.taskrouter.workspaces(workspace.sid).tasks.create(
    attributes='{"language":"english"}'
)

# Enqueue the task into the queue
enqueue = client.taskrouter.workspaces(workspace.sid).tasks(task.sid).enqueue(
    workflow_sid=workflow.sid
)

# Print task SID
print('Task SID:', task.sid)
