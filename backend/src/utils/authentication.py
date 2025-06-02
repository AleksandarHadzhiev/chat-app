import logging
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Request
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel

from config import Config
from src.db.db import Database
from src.users.repositories.factory import RepositoryFactory


class TokenData(BaseModel):
    email: str | None = None


class User(BaseModel):
    id: int
    email: str
    username: str
    verified: bool


class Authenticator:
    def __init__(self, config: Config, db: Database):
        self.config = config
        self.rep = RepositoryFactory(db=db).get_db()

    def create_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=self.config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=self.config.SECRET_KEY,
            algorithm=self.config.ALGORITHM,
        )
        return encoded_jwt

    async def get_current_user(self, token: str):
        credentails_exception = {"fail": "unauthorized"}
        try:
            payload = jwt.decode(
                token, self.config.PUBLIC_KEY, algorithms=[self.config.ALGORITHM]
            )
            email = payload.get("sub")
            if email is None:
                raise credentails_exception
            token_data = TokenData(email=email)
        except InvalidTokenError as e:
            logging.error(e.args)
            return credentails_exception
        data = {"email": token_data.email}
        user = await self.rep.get_by_email(data=data)
        if "user" in user:
            return credentails_exception
        return User(**user)
