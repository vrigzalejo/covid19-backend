import graphene
import pandas as pd
from pathlib import Path

covid19_path = '../../../COVID-19'
ccse_confirmed_global_path = covid19_path + '/csse_covid_19_data/csse_covid_19_time_series'


def extract_ccse_covid19_confirmed_global():
    csv = ccse_confirmed_global_path + '/time_series_covid19_confirmed_global.csv'
    df = pd.read_csv(csv)  
    # print(df.columns)
    # print(df['Province/State'])
    # print(df.head(6))
    # for index, row in df.iterrows():
        # print(index, row)
    # print(df.to_numpy())
    # print(df.to_json(r'test.json', orient = "records"))
    # return df["Province/State"].to_list())
    return df


# class ConfirmedCases(graphene.ObjectType):
    

class Query(graphene.ObjectType):
    province_state = graphene.List(graphene.String)

    def resolve_province_state(self, info):
        return extract_ccse_covid19_confirmed_global()["Province/State"].to_list()



if __name__ == "__main__":
    # csvPath('test')
    extract_ccse_covid19_confirmed_global()
