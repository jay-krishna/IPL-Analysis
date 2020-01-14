import os
import scorecard

directory_path=os.path.join(os.getcwd(),'ipl')
i=0

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

			i+=1
			if(i%100==0):
				print("Done")