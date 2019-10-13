from ihome import  create_app,db

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


app = create_app("develop")

manage = Manager(app)

manage.add_command("db",MigrateCommand)

Migrate(app,db) # 数据库迁移

if __name__ == '__main__':

    manage.run()