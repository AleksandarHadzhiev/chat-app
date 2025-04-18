# chat-app

A chat-app utilizing websockets 

## Description

A chat application with Next.js as a frontend service and FastAPI as a backend service. Together with that there will be a websocket server running in the backend, and the frontend will serve as a client. The application will provide the option for the user to login using Google or email + password combination. PostgreSQL as a DB service and hosting the application on Google Cloud.

<!-- 
TO BE ADDED 
## Architecture
-->
## Backend

The backed will be split in a few separate major endpoints - users, groups, messages. And each of them will have their own subendpoint, for example: `users/login`, `groups/all`, `messages/{group_id}`.

The websocket server will be running in the backend as well. The websocker server will communicate directly with both the client and utillize backend functionalities - store the message (backend), send the message (to the frontend).

To fully run the backend for developemnt and to play around first run the docker compose file command: `docker compose up` add `-d` if you want to keep it running in the background and still use the same terminal. Then run `pipenv run start` to start the local backend.

To run the tests simply run `pipenv run test`

There will be options for fully dockerized application, utilizing --profiles from docker, but work is still in progress. The development setup is utlizing postgresql for DB and mailhog for sending and receiving emails require when registering. 

## Frontend

The frontend will utilzie  `axios` for the calls to the backend and the built-int websocket, to connect to the websocket. It will be split in different components for better separation of concerns.

To run the frontend there are three options. But first you have to have the backend up and running. If the backend is running you can run either of the three options:
```
// Feature in testing fron NextJs
npm run turbo

// Development server regular
npm run dev

// Production server
  // Run build
  npm run build

  // Start server
  npm run start 

```
<!-- 
TO BE ADDED 
## Bootup
## Exampl
-->
