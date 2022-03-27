import pandas as pd

maintanance_jobs_df = pd.read_csv("data/maintanance_jobs_df.csv", low_memory=False)

maintanance_jobs_df_selected = maintanance_jobs_df.loc[maintanance_jobs_df['year']==2026]
maintanance_jobs_df_selected.to_csv('data/maintanance_jobs_df_selected.csv')
print(maintanance_jobs_df.info())