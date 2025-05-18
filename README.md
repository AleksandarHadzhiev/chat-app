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

The websocket server will be running in the backend as well. The websocket server will communicate directly with both the client and utillize backend functionalities - store the message (backend), send the message (to the frontend).

## Frontend

The frontend will utilzie  `axios` for the calls to the backend and the built-int websocket, to connect to the websocket. It will be split in different components for better separation of concerns.
<!-- 
TO BE ADDED 
## Bootup
## Exampl
-->
