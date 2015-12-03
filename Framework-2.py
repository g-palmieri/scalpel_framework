## G Palmieri - 2015

import os, os.path, glob, sys, shutil

dd_Directory = raw_input('Please enter the dd absolute directory: ')	#gets user inputted value for dir
dd_Just_File = raw_input('Please enter the dd name (no extension): ')	#gets user unputted value for file name


dd_file = dd_Directory + "/" + dd_Just_File	#create the dd file and location string

number_of_files = len(glob.glob1(dd_Directory, dd_Just_File + '.[0-9][0-9][0-9]'))	#finds amount of dd files in directory that conatin the name given and end in three numbers

if glob.glob(dd_file + '.000'):	#checks to see if the first split is 000 or other
	count = 0		#initiates count to 0
else:				#other in this case is 001
	count = 1 		#initiates count to 1

	
complete_folder = r'' + dd_Directory + '/Scalpel-' + dd_Just_File + '-Complete'	#
if not os.path.exists(complete_folder):	#checks directory doesn't already exist
	os.makedirs(complete_folder)	#creates directory to store all files
print "Made Directory...."

def rename(dir, pattern, titlePattern):			#defines the function to rename the files
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))

while count <= number_of_files:
	if count < 10:		#if the count is below 10, 
		filler = "00"	#uses the filler string to pad the image name to 00n
	elif count < 100:	#if the count is below 100,
		filler = "0"	#uses the filler string to pad the image name to 0nn
	else:
		filler = ""

	os.system('scalpel ' + dd_file + '.' + filler + str(count) + ' -o ""' + dd_Directory + '"/scalpel_temp_"' + str(count) + " -O")
	rename(r'' + dd_Directory + '/scalpel_temp_' + str(count), r'*.*', r'dd' + filler + str(count) +'-(%s)')	#calls the rename funciton

	src_dir = dd_Directory + '/scalpel_temp_' + str(count)			#creates the source directory as string
	dst_dir = dd_Directory + '/Scalpel-' + dd_Just_File + '-Complete/'	#creates the destination directory as string

	for file in glob.iglob(os.path.join(src_dir, "*.*")):	#loops all files in the tmp dir
    		shutil.move(file, dst_dir)			#moves the files to the source dir
	
	os.rmdir(src_dir)	#removes the tmp dir (only if they are empty)

	count += 1	#incremnts the count

#-------------------sorts files by extension----------
	#-----------Audit Files-----------------------
text_folder = r'' + dst_dir + '/Scalpel-Audits' 
if not os.path.exists(text_folder):
	os.makedirs(text_folder)

os.chdir(dst_dir)
for file in glob.glob('*(audit).txt'):
	shutil.move(file, text_folder)

	#-----------ZIP files-------------------------
zip_counter = len(glob.glob1(dst_dir,'*.zip'))	#counts number of zip files

if zip_counter > 0:
	zip_folder = r'' + dst_dir + '/Scalpel-ZIP' 
	if not os.path.exists(zip_folder):
		os.makedirs(zip_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.zip'):
		shutil.move(file, zip_folder)
	#-----------Image Files------------------------
image_counter = len(glob.glob1(dst_dir,'*.jpg'))	#counts number of image files
image_counter = image_counter + len(glob.glob1(dst_dir,'*.gif'))
image_counter = image_counter + len(glob.glob1(dst_dir,'*.tif'))
image_counter = image_counter + len(glob.glob1(dst_dir,'*.png'))
image_counter = image_counter + len(glob.glob1(dst_dir,'*.bmp'))

if image_counter > 0:	#checks to see if any image files exists
	images_folder = r'' + dst_dir + '/Scalpel-Images' 
	if not os.path.exists(images_folder):
		os.makedirs(images_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.jpg'):
		shutil.move(file, images_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.gif'):
		shutil.move(file, images_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.tif'):
		shutil.move(file, images_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.png'):
		shutil.move(file, images_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.bmp'):
		shutil.move(file, images_folder)

	#------------Video Files------------------------
video_counter = len(glob.glob1(dst_dir,'*.mpg'))
video_counter = video_counter + len(glob.glob1(dst_dir,'*.avi'))

if video_counter > 0:	#checks to see if any video files exists
	video_folder = r'' + dst_dir + '/Scalpel-Video' 
	if not os.path.exists(video_folder):
		os.makedirs(video_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.mpg'):
		shutil.move(file, video_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.avi'):
		shutil.move(file, video_folder)

	#------------Word Files-------------------------
word_counter = len(glob.glob1(dst_dir,'*.doc'))

if word_counter > 0:	#checks to see if any word files exists
	word_folder = r'' + dst_dir + '/Scalpel-Word' 
	if not os.path.exists(word_folder):
		os.makedirs(word_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.doc'):
		shutil.move(file, word_folder)

	#-----------HTML Files--------------------------
html_counter = len(glob.glob1(dst_dir,'*.htm'))

if html_counter > 0:
	html_folder = r'' + dst_dir + '/Scalpel-HTML' 
	if not os.path.exists(html_folder):
		os.makedirs(html_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.htm'):
		shutil.move(file, html_folder)

	#-----------PDF Files---------------------------
pdf_counter = len(glob.glob1(dst_dir,'*.pdf'))

if pdf_counter > 0:
	pdf_folder = r'' + dst_dir + '/Scalpel-PDF' 
	if not os.path.exists(pdf_folder):
		os.makedirs(pdf_folder)

	os.chdir(dst_dir)
	for file in glob.glob('*.pdf'):
		shutil.move(file, pdf_folder)

#------------------end of sorting-----------------------


print
print "Finished: Completed"