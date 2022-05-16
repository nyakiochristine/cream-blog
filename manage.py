from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Post



app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db')


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Post = Post)


if __name__ == '__main__':
    manager.run()
    db.create_all()