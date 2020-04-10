from flask_script import Manager, Command
from flask_app import app
from flask_migrate import MigrateCommand
from flask_app.database.base import db
from flask_app.models.country_regions import CountryRegion
from flask_app.models.confirmed_global import ConfirmedGlobal
from datetime import datetime
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
        print(df_dict)

    def seed_confirmed_global(self):
        csv = self.confirm_global_csv
        df = pd.read_csv(csv, parse_dates=True)
        df['country_region_id'] = df.index + 1
        df_date_as_rows = pd.melt(
            df,
            id_vars=['Province/State', 'Country/Region', 'Lat', 'Long', 'country_region_id'],
            var_name="date",
            value_name="numbers"
        )

        df_cols = ['date', 'numbers', 'country_region_id']
        filtered_df = df_date_as_rows[df_cols].reset_index(drop=True)
        filtered_df['id'] = filtered_df.index + 1
        filtered_df['date'] = pd.to_datetime(filtered_df['date'])
        df_dict = filtered_df.to_dict('records')
        db.engine.execute(ConfirmedGlobal.__table__.delete())
        db.engine.execute(ConfirmedGlobal.__table__.insert(), df_dict)
        print(df_dict)

    def run(self):
        self.seed_country_regions()
        self.seed_confirmed_global()


if __name__ == "__main__":
    manager.add_command('seed', Seeder())
    manager.run()
