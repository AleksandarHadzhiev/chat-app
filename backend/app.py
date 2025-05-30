"""Starting point of the application"""

import logging
import uvicorn
from src.main import create_app
import sys


n = len(sys.argv)
environments = ["docker", "dev", "test"]
if n != 3:
    logging.error(f"Unsupported arguments: {n}")
else:
    env = sys.argv[1]
    key = sys.argv[1]
    if env in environments:
        response = create_app(server=env, secret=key)
        app = response["app"]
        config = response["config"]
        uvicorn.run(app=app, host=config.BASE_URL)
    else:
        logging.error(f"Unsupported environment: {env}")
