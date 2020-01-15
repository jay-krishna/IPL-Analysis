import os
import pandas as pd

def get_value(src,key):
	file=open(src,"r")

	for _ in file:
		one=_.split(":")[0]
		two=_.split(":")[1]

		if(one==key):
			return two

def calculate_averages_batting():
	matches=os.path.join(os.getcwd(),'ipl/matches.txt')
	matches_file=open(matches,"r")

	df_batting=pd.DataFrame(columns=["Year","Total","Matches"])

	for _ in matches_file:
		line=_.rstrip()
		year=line.split(":")[0].split("-")[0]
		match_id=line.split(":")[1]
		src=os.path.join(os.getcwd(),str("ipl_scorecard/"+match_id+"/metadata.txt"))

		if(year not in list(pd.unique(df_batting["Year"]))):
			x=pd.DataFrame({"Year":year,"Total":[0],"Matches":[0]})
			df_batting=df_batting.append(x)

		df_batting.loc[df_batting.Year==year,'Matches']+=1
		df_batting.loc[df_batting.Year==year,'Total']+=int(get_value(src,"Runs"))

	df_batting["Average"]=(df_batting["Total"]/df_batting["Matches"])/2
	df_batting=df_batting.set_index(["Year"])

	des=os.path.join(os.getcwd(),"data")
	df_batting.to_csv(des+"/combined_batting.csv")

def calculate_averages_bowling():
	matches=os.path.join(os.getcwd(),'ipl/matches.txt')
	matches_file=open(matches,"r")

	df_bowling=pd.DataFrame(columns=["Year","Total","Matches"])

	for _ in matches_file:
		line=_.rstrip()
		year=line.split(":")[0].split("-")[0]
		match_id=line.split(":")[1]
		src=os.path.join(os.getcwd(),str("ipl_scorecard/"+match_id+"/metadata.txt"))

		if(year not in list(pd.unique(df_bowling["Year"]))):
			x=pd.DataFrame({"Year":year,"Total":[0],"Matches":[0]})
			df_bowling=df_bowling.append(x)

		df_bowling.loc[df_bowling.Year==year,'Matches']+=1
		df_bowling.loc[df_bowling.Year==year,'Total']+=int(get_value(src,"Wickets"))

	df_bowling["Average"]=(df_bowling["Total"]/df_bowling["Matches"])/2
	df_bowling=df_bowling.set_index(["Year"])

	des=os.path.join(os.getcwd(),"data")
	df_bowling.to_csv(des+"/combined_bowling.csv")

def calculate_averages_slot_batting():
	matches=os.path.join(os.getcwd(),'ipl/matches.txt')
	matches_file=open(matches,"r")

	df_batting=pd.DataFrame(columns=["Year","0-6","6-12","12-16","16-20","Avg.0-6","Avg.6-12","Avg.12-16","Avg.16-20","Str.0-6","Str.6-12","Str.12-16","Str.16-20","Matches"])

	for _ in matches_file:
		line=_.rstrip()
		year=line.split(":")[0].split("-")[0]
		match_id=line.split(":")[1]
		src=os.path.join(os.getcwd(),str("ipl_scorecard/"+match_id+"/metadata.txt"))

		if(year not in list(pd.unique(df_batting["Year"]))):
			x=pd.DataFrame({"Year":year,"0-6":[0],"6-12":[0],"12-16":[0],"16-20":[0],"Avg.0-6":[{0.0}],"Avg.6-12":[{0.0}],"Avg.12-16":[{0.0}],"Avg.16-20":[{0.0}],"Str.0-6":[{0.0}],"Str.6-12":[{0.0}],"Str.12-16":[{0.0}],"Str.16-20":[{0.0}],"Matches":[0]})
			df_batting=df_batting.append(x)

		df_batting.loc[df_batting.Year==year,'Matches']+=1
		runs=get_value(src,"Slots_Runs")
		df_batting.loc[df_batting.Year==year,'0-6']+=int(runs.split(" ")[0])
		df_batting.loc[df_batting.Year==year,'6-12']+=int(runs.split(" ")[1])
		df_batting.loc[df_batting.Year==year,'12-16']+=int(runs.split(" ")[2])
		df_batting.loc[df_batting.Year==year,'16-20']+=int(runs.split(" ")[3])

	df_batting["Avg.0-6"]=(df_batting["0-6"]/df_batting["Matches"])/2
	df_batting["Avg.6-12"]=(df_batting["6-12"]/df_batting["Matches"])/2
	df_batting["Avg.12-16"]=(df_batting["12-16"]/df_batting["Matches"])/2
	df_batting["Avg.16-20"]=(df_batting["16-20"]/df_batting["Matches"])/2

	df_batting["Str.0-6"]=(df_batting["Avg.0-6"]/72)*100
	df_batting["Str.6-12"]=(df_batting["Avg.6-12"]/72)*100
	df_batting["Str.12-16"]=(df_batting["Avg.12-16"]/56)*100
	df_batting["Str.16-20"]=(df_batting["Avg.16-20"]/56)*100

	df_batting=df_batting.set_index(["Year"])

	print(df_batting)
	# des=os.path.join(os.getcwd(),"data")
	# df_batting.to_csv(des+"/combined_slot_batting.csv")

def calculate_averages_slot_bowling():
	matches=os.path.join(os.getcwd(),'ipl/matches.txt')
	matches_file=open(matches,"r")

	df_bowling=pd.DataFrame(columns=["Year","0-6","6-12","12-16","16-20","Avg.0-6","Avg.6-12","Avg.12-16","Avg.16-20","Str.0-6","Str.6-12","Str.12-16","Str.16-20","Matches"])

	for _ in matches_file:
		line=_.rstrip()
		year=line.split(":")[0].split("-")[0]
		match_id=line.split(":")[1]
		src=os.path.join(os.getcwd(),str("ipl_scorecard/"+match_id+"/metadata.txt"))

		if(year not in list(pd.unique(df_bowling["Year"]))):
			x=pd.DataFrame({"Year":year,"0-6":[0],"6-12":[0],"12-16":[0],"16-20":[0],"Avg.0-6":[{0.0}],"Avg.6-12":[{0.0}],"Avg.12-16":[{0.0}],"Avg.16-20":[{0.0}],"Str.0-6":[{0.0}],"Str.6-12":[{0.0}],"Str.12-16":[{0.0}],"Str.16-20":[{0.0}],"Matches":[0]})
			df_bowling=df_bowling.append(x)

		df_bowling.loc[df_bowling.Year==year,'Matches']+=1
		wickets=get_value(src,"Slots_Wickets")
		df_bowling.loc[df_bowling.Year==year,'0-6']+=int(wickets.split(" ")[0])
		df_bowling.loc[df_bowling.Year==year,'6-12']+=int(wickets.split(" ")[1])
		df_bowling.loc[df_bowling.Year==year,'12-16']+=int(wickets.split(" ")[2])
		df_bowling.loc[df_bowling.Year==year,'16-20']+=int(wickets.split(" ")[3])

	df_bowling["Avg.0-6"]=(df_bowling["0-6"]/df_bowling["Matches"])/2
	df_bowling["Avg.6-12"]=(df_bowling["6-12"]/df_bowling["Matches"])/2
	df_bowling["Avg.12-16"]=(df_bowling["12-16"]/df_bowling["Matches"])/2
	df_bowling["Avg.16-20"]=(df_bowling["16-20"]/df_bowling["Matches"])/2

	df_bowling["Str.0-6"]=(72/df_bowling["Avg.0-6"])
	df_bowling["Str.6-12"]=(72/df_bowling["Avg.6-12"])
	df_bowling["Str.12-16"]=(56/df_bowling["Avg.12-16"])
	df_bowling["Str.16-20"]=(56/df_bowling["Avg.16-20"])

	df_bowling=df_bowling.set_index(["Year"])
	print(df_bowling)
	# des=os.path.join(os.getcwd(),"data")
	# df_bowling.to_csv(des+"/combined_slot_bowling.csv")

calculate_averages_slot_batting()
calculate_averages_slot_bowling()