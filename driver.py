import os
import scorecard
import pandas as pd

def generate_scorecard():

	directory_path=os.path.join(os.getcwd(),'ipl')

	for r,d,f in os.walk(directory_path):

		for file in f:
			if ".yaml" in file:
				src=os.path.join(r,file)
				des=os.path.join(os.getcwd(),"ipl_scorecard/"+file.split(".")[0])
				try:
					os.mkdir(des)
				except:
					continue
				scorecard.generate(src,des)

def generate_matchwise_runs():
	directory_path=os.path.join(os.getcwd(),'ipl_scorecard')

	for r,d,f in os.walk(directory_path):
		for directory in d:
			directory_full=os.path.join(r,directory)

			for r2,d2,f2 in os.walk(directory_full):
				des=os.path.join(r2,"metadata.txt")
				runs=0

				for file in f2:
					if "bowling" in file:
						src=os.path.join(r2,file)
						
						runs+=scorecard.calculate_runs(src)

				pointer=open(des,'w')
				pointer.write("Runs:"+str(runs)+'\n')

def generate_matchwise_wickets():
	directory_path=os.path.join(os.getcwd(),'ipl_scorecard')

	for r,d,f in os.walk(directory_path):
		for directory in d:
			directory_full=os.path.join(r,directory)

			for r2,d2,f2 in os.walk(directory_full):
				des=os.path.join(r2,"metadata.txt")
				wickets=0

				for file in f2:
					if "batting" in file:
						src=os.path.join(r2,file)
						
						wickets+=scorecard.calculate_wickets(src)

				pointer=open(des,'a')
				pointer.write("Wickets:"+str(wickets)+'\n')

def generate_slots_runs():
	directory_path=os.path.join(os.getcwd(),'ipl')

	for r,d,f in os.walk(directory_path):
		for file in f:
			if ".yaml" in file:
				src=os.path.join(r,file)
				des=os.path.join(os.getcwd(),"ipl_scorecard/"+file.split(".")[0]+"/metadata.txt")

				x=scorecard.generate_slots_runs(src)
				data="Slots_Runs:"
				for _ in x:
					data+=str(str(_)+" ")

				data=data.rstrip()
				data+="\n"

				file=open(des,"a")
				file.write(data)
				file.close()

def generate_slots_wickets():
	directory_path=os.path.join(os.getcwd(),'ipl')

	for r,d,f in os.walk(directory_path):
		for file in f:
			if ".yaml" in file:
				src=os.path.join(r,file)
				des=os.path.join(os.getcwd(),"ipl_scorecard/"+file.split(".")[0]+"/metadata.txt")

				x=scorecard.generate_slots_wickets(src)
				data="Slots_Wickets:"
				for _ in x:
					data+=str(str(_)+" ")

				data=data.rstrip()
				data+="\n"

				file=open(des,"a")
				file.write(data)
				file.close()

def generate_over():
	directory_path=os.path.join(os.getcwd(),'ipl')

	for r,d,f in os.walk(directory_path):
		for file in f:
			if ".yaml" in file:
				src=os.path.join(r,file)
				des=os.path.join(os.getcwd(),"ipl_scorecard/"+file.split(".")[0])

				scorecard.generate_over(src,des)

generate_over()