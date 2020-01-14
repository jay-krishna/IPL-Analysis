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

def generate_matchwise():
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
						
						runs+=scorecard.calculate(src)

				pointer=open(des,'w')
				pointer.write("Runs:"+str(runs))

generate_matchwise()