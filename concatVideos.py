import sys

proj = sys.argv[1]
GOPSize = sys.argv[2]

r = open("result_concatVideos.yuv", 'wb')
p = open(proj + ".txt", "r")
lines = p.readlines()
p.close

	
def copyGOP(video, h, w, startFrame):
	f = open("../../origCfP/" + video, 'rb')
	frame = 3 * (int(h) * int(w)) / 2
	
	for frames in range(0,int(startFrame)):
		f.read(frame)
	for frames in range(int(startFrame), (int(startFrame) + int(GOPSize))):
		string = f.read(frame)
		f.write(string)

for line in lines:
	line = line.split()
	print line
	copyGOP(line[0], line[1], line[2], line[3])
