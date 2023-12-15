from project import combined_df, count_input, z_val


import altair as alt


bar = alt.Chart(combined_df.nlargest(count_input, z_val)).mark_bar().encode(
    y=alt.Y('State', title='State', sort='-x'),
    x=alt.X(z_val, title=f'{z_val}'),
    tooltip=['State', z_val, 'Total']
).transform_window(
    rank='rank(z_val)', sort=[alt.SortField(z_val, order='descending')]
).transform_filter(
    (alt.datum.rank <= count_input)
)