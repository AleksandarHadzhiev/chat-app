"""Starting point of the application"""

import logging
import sys

import uvicorn

from src.main import create_app

n = len(sys.argv)
environments = ["docker", "dev", "test"]

env = sys.argv[1]
password="secret-key-placeholder"
if n == 3:
    password = sys.argv[2]
if env in environments:
    response = create_app(server=env, password=password)
    app = response["app"]
    config = response["config"]
    uvicorn.run(app=app, host=config.BASE_URL)
else:
    logging.error(f"Unsupported environment: {env}")
