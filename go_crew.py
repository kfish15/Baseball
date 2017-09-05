from datetime import datetime, timedelta
import requests
import json



# link: https://github.com/fspinillo/python-baseball/blob/master/baseball.py





#function to determine the status of a game, if no team selected
#based on the progress, different data is returned


def team_score():
    if game['status']['status'] == "In Progress":
        return \
        '-------------------------------\n' \
        '%s (%s) vs. %s (%s) @ %s\n' \
        '%s: %s of the %s\n' \
        'Pitching: %s, %s || Batting: %s, %s || S: %s B: %s O: %s\n' \
        '-------------------------------' % (
				game['away_team_name'],
				game['linescore']['r']['away'],
				game['home_team_name'],
				game['linescore']['r']['home'],
				game['venue'],
				game['status']['status'],
				game['status']['inning_state'],
				game['status']['inning'],
				game['pitcher']['last'],
				game['pitcher']['first'][:1],
				game['batter']['last'],
				game['batter']['first'][:1],
                game['status']['s'],
                game['status']['b'],
                game['status']['o']
            )
    elif (game['status']['status'] == "Final" or game['status']['status'] == "Game Over"):
        return \
        '-------------------------------\n' \
        '%s (%s) vs. %s (%s) %s\n' \
        'W: %s, %s || L: %s, %s || SV: %s %s\n' \
        '-------------------------------' % (
				game['away_team_name'],
				game['linescore']['r']['away'],
				game['home_team_name'],
				game['linescore']['r']['home'],
				game['status']['status'].upper(),
				game['winning_pitcher']['last'],
				game['winning_pitcher']['first'][:1],
				game['losing_pitcher']['last'],
				game['losing_pitcher']['first'][:1],
				game['save_pitcher']['last'],
				game['save_pitcher']['first'][:1]
            )
    elif (game['status']['status'] == "Pre-Game" or game['status']['status'] == "Preview"):
        return \
        '-------------------------------\n' \
        '%s vs %s @ %s %s%s\n' \
        'P: %s || P: %s\n' \
        '-------------------------------' % (
                game['away_team_name'],
                game['home_team_name'],
                game['venue'],
                game['home_time'],
                game['hm_lg_ampm'],
                game['away_probable_pitcher']['name_display_roster'],
                game['home_probable_pitcher']['name_display_roster']
               )

#function to determine which feed to grab based on user input

def date_url(date):
    if date == "yesterday" or date == "y":
        baseball_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/master_scoreboard.json" \
        % (now.year, now.strftime("%m"), yesterday.strftime("%d"))
    else:
        baseball_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/master_scoreboard.json" \
                % (now.year, now.strftime("%m"), now.strftime("%d"))
    return baseball_url



#process to set date, and convert if need be.

now = datetime.now()
yesterday = datetime.now() - timedelta(days=1)
#date = raw_input('Today or yesterday? ').lower()

date = "today" 

#builds the data structure from the feed

baseball_data = requests.get(date_url(date))
game_data = baseball_data.json()
game_array = game_data['data']['games']['game']
#team = raw_input('What team do you want? ex. SF or NYY ').upper()

teams = ["MIL","COL","STL","CHC","ARI"]

for game in game_array:
	if game['home_name_abbrev'] not in teams or game['away_name_abbrev'] not in teams:
		disp = team_score()
		print disp




