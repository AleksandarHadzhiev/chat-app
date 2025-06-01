# chat-app

A chat-app utilizing websockets 

## Description

A chat application with Next.js as a frontend service and FastAPI as a backend service. Together with that there will be a websocket server running in the backend, and the frontend will serve as a client. The application will provide the option for the user to login using email + password combination. PostgreSQL as a DB service.

## Backend

The backed will be split in a few separate major endpoints - users, groups, messages. And each of them will have their own subendpoint, for example: `/login`, `groups/all`, `messages/{group_id}`.

The websocket server will be running in the backend as well. The websocker server will communicate directly with both the client and utillize backend functionalities - store the message (backend), send the message (to the frontend).

To fully run the backend for developemnt and to play around first run the docker compose file command: `docker compose --profile dev up` add `-d` if you want to keep it running in the background and still use the same terminal. Then run `pipenv run start <password>` to start the local backend. The password field can be anything you like, or leave it empty as there is a default value to it in the backend, it serves as a password for the `rs` secret generator in the backend. The generator is used to generate a secret_key and public_key for the jwt token, which is used as an access_token for the endpoints -> groups and messages. 

To run the tests simply run, if you have not started the database containers first run `docker compose --profile test up -d` and then
`pipenv run test-no-workers`. 

To run the backend completely in docker - no need for `pipenv run start` - run: `docker compose --profile app up -d`.

To run both the backend and frontend inside docker - no need for either `pipenv run start` or `npm run dev` - run `docker compose --profile full up -d. 

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