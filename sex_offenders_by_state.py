# Group by state and count the number of sex offenders
from project import combined_df


sex_offenders_by_state = combined_df.groupby('State')['sex_offender'].sum().reset_index()