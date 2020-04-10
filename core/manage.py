from flask_script import Manager, Command
from flask_app import app
from flask_migrate import MigrateCommand
from flask_app.database.base import db
from flask_app.models.country_regions import CountryRegion
import pandas as pd

engine = db.get_engine()
manager = Manager(app)

class Seeder(Command):
    covid19_path = '../COVID-19/'
    ccse_confirmed_global_path = covid19_path + 'csse_covid_19_data/csse_covid_19_time_series/'

    confirm_global_csv = ccse_confirmed_global_path + 'time_series_covid19_confirmed_global.csv'

    def seed_country_regions(self):
        csv = self.confirm_global_csv
        df = pd.read_csv(csv)

        df_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']
        filtered_df = df[df_cols].reset_index(drop=True)
        filtered_df.rename(
            columns={
                'Province/State': 'province_state',
                'Country/Region': 'country_region',
                'Lat': 'latitude',
                'Long': 'longitude'
            },
            inplace=True
        )

        filtered_df['id'] = range(1, len(filtered_df) + 1)
        df_dict = filtered_df.to_dict(orient='records')
        db.engine.execute(CountryRegion.__table__.delete())
        db.engine.execute(CountryRegion.__table__.insert(), df_dict)


    def seed_confirmed_global(self):
        csv = self.confirm_global_csv
        df = pd.read_csv(csv)
        filtered_df = (
            df[['Province/State', 'Lat', 'Long']]
            .drop_duplicates(subset='Province/State')
            .reset_index()
        )

        print(filtered_df)


    def run(self):
        self.seed_country_regions()
        # self.seed_provinces()


if __name__ == "__main__":
    manager.add_command('seed', Seeder())
    manager.run()
