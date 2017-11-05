#! /usr/bin/env python

import os

from flask_script import Manager
from flask_script import Command

from app import create_app, db
from app.models.user import User

app = create_app(os.getenv('APP_CONFIG', 'default'))
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

@manager.command
def add_user():
    "adds a user"
    username = input("username: ")
    password = input("password: ")
    user = User(username=username,
                password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
