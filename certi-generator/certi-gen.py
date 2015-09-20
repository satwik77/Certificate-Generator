from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
import os


for t in range(1,54):
	fopen = open('%d' % t, 'r')
	# gopen = open('%d' % t, 'r')
	for z in range(100):
		rline = fopen.readline()

		if rline:
			print rline
			plist = rline.split('$')

			print plist
			newpath = '/home/gauss/Git proj/Certificate-Generator/output/%s/' % plist[1].replace(" ", "")
			print newpath

			if not os.path.exists(newpath): 
				clg = plist[1].replace(' ','')
				os.mkdir('/home/gauss/Git proj/Certificate-Generator/output/%s/' % clg)
			elist = plist[2].split(',')
			elist1= []
			for t in elist:
				if 'BOYS' in t.upper():
					t = t.upper()
					t = t[:t.find(" (BOYS)")]
					t=t.strip()
					elist1.append(t.title())
				elif 'GIRLS' in t.upper():
					t = t.upper()
					t=t.strip()
					t = t[:t.find(" (GIRLS)")]
					elist1.append(t.title())
				else: 
					t=t.strip()
					elist1.append(t)

			# event_str = event_str.title()
			# event_str = plist[2]
			event_str= ','.join(elist1)
			print event_str

			#name correction
			temp = [x.title() for x in plist[0].split(" ")]
			plist[0] = " ".join(temp)

			with Drawing() as draw:
				with Image(filename='Participation.jpg') as image:
					draw.font = 'FoglihtenNo07_0841.otf'
					draw.font_size = 60
					draw.text_alignment ='center'
					draw.text_antialias = True
					draw.text(2216, image.height / 2  + 140 , plist[0].strip())
					draw.text(1994, image.height / 2  + 280 , plist[1].strip().upper())
					draw.text(1499, image.height / 2  + 435 , event_str)
					draw(image)

					image.save(filename="/home/gauss/dvmtest/satwik_certitest/output/%s/%s_%s" % (plist[1].replace(" ", ""), plist[0].replace(" ",""),event_str.strip())) #% (clg, plist[0].replace(" ", ""), event_str))
			print "Done"
		else:
			break

	fopen.close()