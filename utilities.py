import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from notion_client import Client
from typing import List, Dict, Tuple
from datetime import datetime


def get_tasks(notion: Client) -> Dict[Tuple, Tuple]:
    """
    Queries the given Notion database, retrieves all entries and stores a mapping between the id of each entry and the
    value of the specified select property
    """

    task_map = {}
    try:
        results = notion.databases.query(
            **{
                "database_id": config.NOTION_DATABASE_ID,
            }
        ).get("results")

        for item in results:
            task_map[(item['id'], item['properties']['Name']['title'][0]['plain_text'])] = (item['properties'][config.PROPERTY_NAME]['select']['id'], item['properties'][config.PROPERTY_NAME]['select']['name']) if item['properties'][config.PROPERTY_NAME]['select'] else ('', 'No Status')
        print(f'{datetime.now()}: Successfully queried task database')

    except Exception as e:
        print(f'{datetime.now()}: ' + str(e))

    return task_map


def find_updates(notion: Client, previous_tasks: Dict[Tuple, Tuple]) -> [List[Tuple], Dict[Tuple, Tuple]]:
    """
    Queries the given Notion database, compares the obtained tasks with previous tasks and returns those tasks where
    the value of the given property has changed
    """

    current_tasks = get_tasks(notion)
    updated_tasks = list(set(current_tasks.items()) - set(previous_tasks.items()))
    print(f'{datetime.now()}: {len(updated_tasks)} updated tasks were found') if updated_tasks else None

    return updated_tasks, current_tasks


def send_mail_update(task: Tuple) -> None:
    """
    Sends E-Mail to inform recipient about a property change for the given task
    """

    message = Mail(
        from_email=config.EMAIL_FROM_FIELD,
        to_emails=config.EMAIL_TO_FIELD,
        subject='Updated task in Notion database',
        plain_text_content=f'''Dear user,\n \n the property {config.PROPERTY_NAME} of task {task[0][1]} in your Notion database has been updated to {task[1][1]} 
                            ''')
    try:
        sg = SendGridAPIClient(config.SENDGRID_KEY)
        response = sg.send(message)
        print(f'{datetime.now()}: Successfully sent email for updated task')
    except Exception as e:
        print(e)
