import os


imdir = 'images'

if not os.path.isdir(imdir):
	os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'fidget' in folder]

ctr = 0

for folder in fidget_folders:
 	for imfile in os.scandir(folder):
 		os.rename(imfile.path, os.path.join(imdir, '{:04}.png'.format(ctr)))
 		ctr += 1