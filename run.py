#!/usr/bin/env python3

import config
from notion_client import Client
from time import sleep
from utilities import *

notion = Client(auth=config.NOTION_KEY)
previous_tasks = get_tasks(notion)

while True:
    sleep(config.POLLING_INTERVAL)
    updated_tasks, previous_tasks = find_updates(notion, previous_tasks)
    for task in updated_tasks:
        send_mail_update(task)
