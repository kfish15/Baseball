import mlbgame
import datetime

t = datetime.date
print t


year_source = int(raw_input("Year: "))
month_source = int(raw_input("Month: "))
day_source = int(raw_input("Day: "))
team_source = raw_input("Team: ")

#games = mlbgame.day(year, month, day)

print
print "--------------------------"

def day(year, month, away,team):
	return mlbgame.day(year,month,day,home=team)


#if __name__=="__main__":
#	print day(year_source,month_source,day_source,home=team_source)



print "--------------------------"
print


