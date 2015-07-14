import sys

projectFile = sys.argv[1]
GOPSize = sys.argv[2]

result = open("concatVideos" + projectFile + ".yuv", 'wb')
p = open(proj + ".txt", "r")
lines = p.readlines()
p.close()

	
def copyGOP(video, h, w, startFrame):
	f = open("../../origCfP/" + video + ".yuv", 'rb')
	frame = 3 * (int(h) * int(w)) / 2 #YCrCb
	
	for frames in range(0,int(startFrame)): #reads frames before the starting frame
		f.read(frame)
	for frames in range(int(startFrame), (int(startFrame) + int(GOPSize))): #reads and saves the GOP
		YUV = f.read(frame)
		result.write(YUV)
		
	f.close()
	
for line in lines:
	line = line.split()
	print line
	copyGOP(line[0], line[1], line[2], line[3])

result.close()
