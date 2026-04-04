def game_analysis(activity):
    resu = activity.loc[
        activity.groupby('player_id')['event_date'].idxmin()
    ][['player_id', 'event_date']]
    resu = resu.rename(columns={"event_date": "first_login"})
    
    return resu