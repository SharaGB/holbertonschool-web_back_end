#!/usr/bin/env python3
""" Create user, Find user, Update user """
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


class DB:
    """class"""

    def __init__(self):
        """constructor"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """takes in email and hashed_password string arguments and returns a
        User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments and returns the first row
        found in the users table as filtered by the method’s input arguments"""
        if kwargs is None:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """takes as input a required user_id integer argument and an arbitrary
        number of keyword arguments, and returns None"""
        _id = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(_id, key):
                raise ValueError
            setattr(_id, key, value)
        self._session.commit()
