import yaml
import math
import pandas as pd
import numpy as np

def generate(file,des):

	with open(file) as f:
	    
	    data = yaml.load(f)

	    df_batting=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","out","out_type","bowler"])
	    df_batting=df_batting.set_index(["Name"])

	    df_bowling=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","Extras","Wicket"])
	    df_bowling=df_bowling.set_index(["Name"])

	    for ball in data["innings"][0]["1st innings"]["deliveries"]:
	    	ball_data=list(ball.values())

	    	if(ball_data[0]["batsman"] not in list(df_batting.index)):
	    		x=pd.DataFrame({"Name":ball_data[0]["batsman"],"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"out":[False],"out_type":[""],"bowler":[""]})
	    		x=x.set_index(["Name"])
	    		df_batting=df_batting.append(x)

	    		# print(df_batting)

	    	df_batting.loc[ball_data[0]["batsman"]]["Balls"]+=1
	    	df_batting.loc[ball_data[0]["batsman"]]["Runs"]+=ball_data[0]["runs"]["batsman"]

	    	if(ball_data[0]["runs"]["batsman"]==0):
	    		df_batting.loc[ball_data[0]["batsman"]]["Dot"]+=1
	    	elif(ball_data[0]["runs"]["batsman"]==4):
	    		df_batting.loc[ball_data[0]["batsman"]]["4"]+=4
	    	elif(ball_data[0]["runs"]["batsman"]==6):
	    		df_batting.loc[ball_data[0]["batsman"]]["6"]+=6
	    	else:
	    		df_batting.loc[ball_data[0]["batsman"]]["Other"]+=ball_data[0]["runs"]["batsman"]

	    	if(ball_data[0]["bowler"] not in list(df_bowling.index)):
	    		y=pd.DataFrame({"Name":ball_data[0]["bowler"],"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"Extras":[0],"Wicket":[0]})
	    		y=y.set_index(["Name"])
	    		df_bowling=df_bowling.append(y)

	    	df_bowling.loc[ball_data[0]["bowler"]]["Balls"]+=1
	    	df_bowling.loc[ball_data[0]["bowler"]]["Runs"]+=ball_data[0]["runs"]["batsman"]
	    	df_bowling.loc[ball_data[0]["bowler"]]["Extras"]+=ball_data[0]["runs"]["extras"]

	    	if(ball_data[0]["runs"]["batsman"]==0):
	    		df_bowling.loc[ball_data[0]["bowler"]]["Dot"]+=1
	    	elif(ball_data[0]["runs"]["batsman"]==4):
	    		df_bowling.loc[ball_data[0]["bowler"]]["4"]+=4
	    	elif(ball_data[0]["runs"]["batsman"]==6):
	    		df_bowling.loc[ball_data[0]["bowler"]]["6"]+=6
	    	else:
	    		df_bowling.loc[ball_data[0]["bowler"]]["Other"]+=ball_data[0]["runs"]["batsman"]

	    	try:
	    		t=ball_data[0]["extras"]
	    		df_bowling.loc[ball_data[0]["bowler"]]["Balls"]-=1
	    		df_batting.loc[ball_data[0]["batsman"]]["Balls"]-=1
	    	except:
	    		pass

	    	try:
	    		t=ball_data[0]["wicket"]
	    		if(ball_data[0]["wicket"]["kind"]!="run out"):
	    			df_bowling.loc[ball_data[0]["bowler"]]["Wicket"]+=1
	    			df_batting.loc[ball_data[0]["wicket"]["player_out"]]["bowler"]=ball_data[0]["bowler"]

	    		df_batting.loc[ball_data[0]["wicket"]["player_out"]]["out"]=True
	    		df_batting.loc[ball_data[0]["wicket"]["player_out"]]["out_type"]=ball_data[0]["wicket"]["kind"]
	    	except:
	    		pass

	    df_bowling["Balls"]=np.ceil(df_bowling["Balls"]/6)

	    df_batting.to_csv(des+"/batting_first.csv")
	    df_bowling.to_csv(des+"/bowling_first.csv")



	    df_batting=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","out","out_type","bowler"])
	    df_batting=df_batting.set_index(["Name"])

	    df_bowling=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","Extras","Wicket"])
	    df_bowling=df_bowling.set_index(["Name"])

	    for ball in data["innings"][1]["2nd innings"]["deliveries"]:
	    	ball_data=list(ball.values())

	    	if(ball_data[0]["batsman"] not in list(df_batting.index)):
	    		x=pd.DataFrame({"Name":ball_data[0]["batsman"],"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"out":[False],"out_type":[""],"bowler":[""]})
	    		x=x.set_index(["Name"])
	    		df_batting=df_batting.append(x)

	    	df_batting.loc[ball_data[0]["batsman"]]["Balls"]+=1
	    	df_batting.loc[ball_data[0]["batsman"]]["Runs"]+=ball_data[0]["runs"]["batsman"]

	    	if(ball_data[0]["runs"]["batsman"]==0):
	    		df_batting.loc[ball_data[0]["batsman"]]["Dot"]+=1
	    	elif(ball_data[0]["runs"]["batsman"]==4):
	    		df_batting.loc[ball_data[0]["batsman"]]["4"]+=4
	    	elif(ball_data[0]["runs"]["batsman"]==6):
	    		df_batting.loc[ball_data[0]["batsman"]]["6"]+=6
	    	else:
	    		df_batting.loc[ball_data[0]["batsman"]]["Other"]+=ball_data[0]["runs"]["batsman"]

	    	if(ball_data[0]["bowler"] not in list(df_bowling.index)):
	    		y=pd.DataFrame({"Name":ball_data[0]["bowler"],"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"Extras":[0],"Wicket":[0]})
	    		y=y.set_index(["Name"])
	    		df_bowling=df_bowling.append(y)

	    	df_bowling.loc[ball_data[0]["bowler"]]["Balls"]+=1
	    	df_bowling.loc[ball_data[0]["bowler"]]["Runs"]+=ball_data[0]["runs"]["batsman"]
	    	df_bowling.loc[ball_data[0]["bowler"]]["Extras"]+=ball_data[0]["runs"]["extras"]

	    	if(ball_data[0]["runs"]["batsman"]==0):
	    		df_bowling.loc[ball_data[0]["bowler"]]["Dot"]+=1
	    	elif(ball_data[0]["runs"]["batsman"]==4):
	    		df_bowling.loc[ball_data[0]["bowler"]]["4"]+=4
	    	elif(ball_data[0]["runs"]["batsman"]==6):
	    		df_bowling.loc[ball_data[0]["bowler"]]["6"]+=6
	    	else:
	    		df_bowling.loc[ball_data[0]["bowler"]]["Other"]+=ball_data[0]["runs"]["batsman"]

	    	try:
	    		t=ball_data[0]["extras"]
	    		df_bowling.loc[ball_data[0]["bowler"]]["Balls"]-=1
	    		df_batting.loc[ball_data[0]["batsman"]]["Balls"]-=1
	    	except:
	    		pass

	    	try:
	    		t=ball_data[0]["wicket"]
	    		if(ball_data[0]["wicket"]["kind"]!="run out"):
	    			df_bowling.loc[ball_data[0]["bowler"]]["Wicket"]+=1
	    			df_batting.loc[ball_data[0]["wicket"]["player_out"]]["bowler"]=ball_data[0]["bowler"]

	    		df_batting.loc[ball_data[0]["wicket"]["player_out"]]["out"]=True
	    		df_batting.loc[ball_data[0]["wicket"]["player_out"]]["out_type"]=ball_data[0]["wicket"]["kind"]
	    	except:
	    		pass

	    df_bowling["Balls"]=np.ceil(df_bowling["Balls"]/6)

	    df_batting.to_csv(des+"/batting_second.csv")
	    df_bowling.to_csv(des+"/bowling_second.csv")

