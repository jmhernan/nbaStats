import sys
import numpy as np
import pandas as pd

# nba_api
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

player_name = "Lebron James"

player_dict = [player for player in nba_players if player['full_name'] == player_name][0]

career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])

career_df = career.get_data_frames()[0]

# team id during the season

team_id = career_df[career_df['SEASON_ID'] == season_id]['TEAM_ID']

# shotchartdetail endpoints

shotchartlist = shotchartdetail.ShotChartDetail(team_id=int(team_id),
                                                    player_id=int(player_dict['id']),
                                                    season_type_all_star='Regular Season',
                                                    season_nullable=season_id,
                                                    context_measure_simple="FGA").get_data_frames()
