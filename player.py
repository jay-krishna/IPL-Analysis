import os
import pandas as pd

def get_unique_players():
    directory_path=os.path.join(os.getcwd(),'ipl_scorecard')
    des=os.path.join(os.getcwd(),"data")

    df_bowling=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","Wicket"])
    df_bowling=df_bowling.set_index(["Name"])
    df_batting=pd.DataFrame(columns=["Name","Balls","Runs","Dot","Other","4","6","not_out"])
    df_batting=df_batting.set_index(["Name"])


    for r,d,f in os.walk(directory_path):
        for directory in d:
            directory_full=os.path.join(r,directory)

            for r2,d2,f2 in os.walk(directory_full):

                for file in f2:
                    if "batting" in file:
                        src=os.path.join(r2,file)
                        df=pd.read_csv(src)
                        df=df.set_index(["Name"])

                        for _ in list(df.index):
                            if _ not in list(df_batting.index):
                                x=pd.DataFrame({"Name":_,"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"not_out":[0]})
                                x=x.set_index(["Name"])
                                df_batting=df_batting.append(x)

                            df_batting.loc[df_batting.index==_,"Balls"]+=df.loc[_]["Balls"]
                            df_batting.loc[df_batting.index==_,"Runs"]+=df.loc[_]["Runs"]
                            df_batting.loc[df_batting.index==_,"Dot"]+=df.loc[_]["Dot"]
                            df_batting.loc[df_batting.index==_,"Other"]+=df.loc[_]["Other"]
                            df_batting.loc[df_batting.index==_,"4"]+=df.loc[_]["4"]
                            df_batting.loc[df_batting.index==_,"6"]+=df.loc[_]["6"]
                            
                            if(df.loc[_]["out"]==False):
                                df_batting.loc[df_batting.index==_,"not_out"]+=1

    df_batting.to_csv(des+"/combined_player_batting.csv")

    for r,d,f in os.walk(directory_path):
        for directory in d:
            directory_full=os.path.join(r,directory)

            for r2,d2,f2 in os.walk(directory_full):

                for file in f2:
                    if "bowling" in file:
                        src=os.path.join(r2,file)
                        df=pd.read_csv(src)
                        df=df.set_index(["Name"])

                        for _ in list(df.index):
                            if _ not in list(df_bowling.index):
                                x=pd.DataFrame({"Name":_,"Balls":[0],"Runs":[0],"Dot":[0],"Other":[0],"4":[0],"6":[0],"Wicket":[0]})
                                x=x.set_index(["Name"])
                                df_bowling=df_bowling.append(x)

                            df_bowling.loc[df_bowling.index==_,"Balls"]+=df.loc[_]["Balls"]
                            df_bowling.loc[df_bowling.index==_,"Runs"]+=df.loc[_]["Runs"]+df.loc[_]["Extras"]
                            df_bowling.loc[df_bowling.index==_,"Dot"]+=df.loc[_]["Dot"]
                            df_bowling.loc[df_bowling.index==_,"Other"]+=df.loc[_]["Other"]
                            df_bowling.loc[df_bowling.index==_,"4"]+=df.loc[_]["4"]
                            df_bowling.loc[df_bowling.index==_,"6"]+=df.loc[_]["6"]
                            df_bowling.loc[df_bowling.index==_,"Wicket"]+=df.loc[_]["Wicket"]

    df_bowling.to_csv(des+"/combined_player_bowling.csv")
    
get_unique_players()                    