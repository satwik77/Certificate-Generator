
gopen = open('namecheck.txt' , 'w')
for i in range(1,54):
	fopen = open('%d' % i, 'r')
	for z in range(100):
		rline = fopen.readline()
		if rline:
			rlist = rline.split('$')
			name = rlist[0].strip()
			clg = rlist[1].strip()
			nlist = name.split(' ')
			if len(nlist)==1:
				gopen.write('%s, %s \n' % (name,clg))
		else:
			break

	fopen.close()

gopen.close()


