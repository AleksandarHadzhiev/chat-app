# chat-app

The application is a real-time chatting, which allows the users to join and create different groups. The real-time chatting aspect of the application is possible due to the integration of websockets. A websocket server in the backend. And a websocket in the frontend which connets to the server. As for the groups and user flows, it is implemented via a REST API backend.

## Description

The application is build on 3 main foundations. The first is a frontend running on Next.js - TypeScript. It aims to separate the code into components and take the API calls out of the components as much as possible - building classes where the `axios` calls are made. Together with that it is utilizing the WebSocket API to build a socket, which will connect to the second foundation of the app, the WebSocket server.

The WebSocket server is running in together with the third foundation - the backend, which runs on FastAPI (Python). Both run together at the same host. The server has its own "ednpoint" which saves the socket - accepts and closses it when needed. Each socket is connected to a client which in the backend is represented with the id of the user which is using the frontend.

The backend has three main flows - users, groups and messages. Each of them has its own endpoints and tables in a database. The database is in PostgreSQL - via a docker image of it for all the environments - dev, test and docker. There is a `Dockerfile` for the database which integrates a custom `init.sql` file - creates the tables and adds some basic data to it - main user (admin - the developer = "me"), the first group and some test data - used during tests.

The users endpoints are - register, login, forgot_password, reset_password, me and authorize. The registration and forgot_password integrate a SMTP functionality to send an email containing code (used to verify the user - updates the verified field for the user in the DB)- registration, link (leads to rest_password page in the frontend) - forgot_password. The authorize is part of the reset_password. As it works as an additional check if the user trying to reset the password in the frontend is allowed to do that action.

For the login flow, the user receives an access_token - a JWT generated with the `PyJWT` and `cryptography`. `cryptography` is a library which allows the creation of a secret and the decryption of the secret. In the case of the application the secret is a private+public key pair - RSA - an asymmetric key cryptography. The choice was made due to the higher security that an asymmetric key cryptography provides compared a symmetric one. 

The access_token is then used - provided and checked for - in eveyr other endpoint - /me included.

The groups and messages endpoints are the standard CRUD operations. The only difference is the creation of message, which is not an endpoint. It is part of the WebSocket server, where the server starts by a user - client - connects to it. Once connected the server listens for any messages by a socket. When a message is received the server sends the message to the socket - client in the frontend, but also stores it in the database.


## Backend

To fully run the backend for developemnt and to play around first run the docker compose file command: `docker compose --profile dev up` add `-d` if you want to keep it running in the background and still use the same terminal. Then run `pipenv run start <password>` to start the local backend. The password field can be anything you like, or leave it empty as there is a default value to it in the backend, it serves as a password for the `rsa` secret generator in the backend.

To run the tests simply run, if you have not started the database containers first run `docker compose --profile test up -d` and then
`pipenv run test-no-workers`. 

To run the backend completely in docker - no need for `pipenv run start` - run: `docker compose --profile app up -d`.

To run both the backend and frontend inside docker - no need for either `pipenv run start` or `npm run dev` - run `docker compose --profile full up -d`. 

## Frontend

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