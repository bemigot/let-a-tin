#!/usr/bin/env python3

import sys
import logging

from utils import job

LOGGER = logging.getLogger('acmet')
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)

TODO_FILE="domains.txt"
ACME_ACCT_KEY_FILE="acme-account/account_key.pem"

def main():
    load_env()
    todo = read_todo(TODO_FILE)
    print(todo)

def read_todo(todo_file, log=LOGGER):
    try:
        with open(todo_file, 'r') as domain_txt:
            return job.queue_jobs(domain_txt)
    except FileNotFoundError:
        log.error("%s not found.", todo_file)

def load_env(log=LOGGER):
    from dotenv import load_dotenv
    if not load_dotenv():
        log.error("No environment variable loaded from .env file")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        LOGGER.warning("no arguments will have effect in command:\n  '%s'", " ".join(sys.argv))
    main()
