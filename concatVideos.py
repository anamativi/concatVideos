import sys
import os
import time

projectFile = sys.argv[1]
GOPSize = sys.argv[2]

out = time.strftime("%y_%m") + "/" + time.strftime("%d") + "/" + "concatVideos_" + projectFile
os.system("mkdir --p " + out) #creates results folder, if it insnt there already

r = open(out + ".yuv", 'wb')
p = open(projectFile + ".txt", "r")
lines = p.readlines()
p.close()

	
def copyGOP(video, startFrame):
	size = video.split("_")
	size = size[1].split("x")
	h = int(size[0])
	w = int(size[1])
	
	f = open("../../origCfP/" + video + ".yuv", 'rb')
	frame = 3 * (int(h) * int(w)) / 2 #YCrCb
	
	for frames in range(0,int(startFrame)): #reads frames before the starting frame
		f.read(frame)
	for frames in range(int(startFrame), (int(startFrame) + int(GOPSize))): #reads and saves the GOP
		YUV = f.read(frame)
		r.write(YUV)
		
	f.close()
	
for line in lines:
	line = line.split()
	print line
	copyGOP(line[0], line[1])

r.close()
