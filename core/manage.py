from flask_script import Manager, Command
from flask_app import app
from flask_migrate import MigrateCommand
from flask_app.database.base import db
from flask_app.models.countries import Country
import pandas as pd

engine = db.get_engine()
manager = Manager(app)

class Seeder(Command):
    covid19_path = '../COVID-19/'
    ccse_confirmed_global_path = covid19_path + 'csse_covid_19_data/csse_covid_19_time_series/'

    confirm_global_csv = ccse_confirmed_global_path + 'time_series_covid19_confirmed_global.csv'

    def seed_confirm_global_csv(self):
        csv = self.confirm_global_csv
        df = pd.read_csv(csv)

        filtered_df = (
            df[['Country/Region']]
            .drop_duplicates(subset='Country/Region')
            .reset_index()
        )

        filtered_df.rename(
            columns={
                'Country/Region': 'country'
            },
            inplace=True
        )

        filtered_df['id'] = range(1, len(filtered_df) + 1)
        df_dict = filtered_df.to_dict(orient='records')
        db.engine.execute(Country.__table__.delete())
        db.engine.execute(Country.__table__.insert(), df_dict)
        print(df_dict)

    def run(self):
        self.seed_confirm_global_csv()


if __name__ == "__main__":
    manager.add_command('seed', Seeder())
    manager.run()
