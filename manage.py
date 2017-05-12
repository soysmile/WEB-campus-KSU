from app import app, db
from app.models import User, Post, Person, Temperature, Block, Hostel, Room
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_alchemydumps import AlchemyDumps, AlchemyDumpsCommand

alchemydumps = AlchemyDumps(app, db)
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Post=Post, User=User, Person=Person, Temperature=Temperature,
                Block=Block, Hostel=Hostel, Room=Room)


manager.add_command('alchemydumps', AlchemyDumpsCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
