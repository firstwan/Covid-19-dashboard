import pandas

covid_df = pandas.read_csv('./dashboard/data/owid-covid-data.csv')
covid_df_excluded_owid = covid_df[(~covid_df['iso_code'].str.contains('OWID', regex=False))] # remove OWID generated custom row

def location_list():
    return covid_df_excluded_owid['location'].unique()