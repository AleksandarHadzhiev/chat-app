"""Starting point of the application"""

import logging
import uvicorn
from src.main import create_app
import sys
from src.utils.rsa_generator import RSAGenerator


n = len(sys.argv)
environments = ["docker", "dev", "test"]
if n != 3:
    logging.error(f"Unsupported arguments: {n}")
else:
    env = sys.argv[1]
    password = sys.argv[2]
    if env in environments:
        rsa_gen = RSAGenerator(password=password)
        private_key = rsa_gen.get_private_key()
        public_key = rsa_gen.get_public_key()
        response = create_app(server=env, secret=private_key, public_key=public_key)
        app = response["app"]
        config = response["config"]
        uvicorn.run(app=app, host=config.BASE_URL)
    else:
        logging.error(f"Unsupported environment: {env}")
