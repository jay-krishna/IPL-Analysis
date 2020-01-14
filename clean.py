import os

source=os.path.join(os.getcwd(),"ipl/map.txt")
destination=os.path.join(os.getcwd(),"ipl/matches.txt")

file_s=open(source,"r")
file_d=open(destination,"w")

for line in file_s:
	one_line=line.replace(" - "," ")
	one_line=one_line.replace(" club IPL male "," ")
	one_line=one_line.replace(" ",":",2)
	file_d.write(one_line)