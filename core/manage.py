from flask_script import Manager, Command
from flask_app import app
from flask_migrate import MigrateCommand
from flask_app.database.base import db
import pandas as pd

engine = db.get_engine()
manager = Manager(app)

print(db.engine.table_names())

class Seeder(Command):
    covid19_path = '../COVID-19'
    ccse_confirmed_global_path = covid19_path + \
        '/csse_covid_19_data/csse_covid_19_time_series'

    def run(self):
        csv = self.ccse_confirmed_global_path + '/time_series_covid19_confirmed_global.csv'
        df = pd.read_csv(csv)
        print(df.head(3))

if __name__ == "__main__":
    manager.add_command('seed', Seeder())
    manager.run()
