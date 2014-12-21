from PIL import Image

def edit_article_images(request, article_id=None):
		if request.method == "POST":
				''' this is a call to crop the images of this post.  It will be cropped and
				 resized to 8 different sizes - at some point this could be more clever thab
				 it is.  As in useing the width and height for restrictions on what can be
				cropped.  The article should no if it has the correct images to be a part of a type of post '''
				x1, x2, y1, y2 = int(float(request.POST['x1'])), int(float(request.POST['x2'])), int(float(request.POST['y1'])), int(float(request.POST['y2']))
				coords = [x1, y1, x2,y2]
				image_loc = '/www/sites/crazyforus.com' + request.POST['image_url']
				result = make_eight_imgs(image_loc, coords);
				return HttpResponse("success"); 
		if not article_id == None:
				article = Articles.objects.get(pk=article_id)
				article_images = ArticleImages.objects.filter(articles=article) # article related images	
				context = {'article_images': article_images}
				return render(request, 'aggregator/admin/edit_article_images.html', context)
		return HttpResponseRedirect('/aggregator/admin/')


def make_eight_imgs():
		main_image = "/www/sites/crazyforus.com/media/aggregator/images/2014/08/09/gold_shoes.jpg"
		coords = [0, 0, 819, 470]
		img =  Image.open(main_image)
		box = (coords[0], coords[1], coords[2], coords[3])
		img = img.crop(box)
		img_arr = main_image.split(".")
		extension = img_arr.pop()
		main_image = ".".join(img_arr)
		new_main_file = main_image+'_819x452.'+extension
		print "Save: %s" % new_main_file
		img.save(new_main_file)
		print "first file saved"
		size_list = ['100x80', '115x115', '120x105', '170x150', '265x165', '300x200', '334x301', '350x150', '560x390', '75x75', '770x470']
		f = open("/www/sites/crazyforus.com/aggregator/logimage.txt", "w")
		for size in size_list:
				size_image(main_image, size, extension)
		f.close() 
		return True

def size_image(main_img, siz, extension):
		''' Receive the base image name the size and the extension which will give you an appropriate name
			This needs to decide which way to resize and crop the image.  Grabbing from the middle would be 
			best.  Size 819x452 is the default '''
		w_h_arr = siz.split('x')	
		w = w_h_arr[0]
		h = w_h_arr[1]
		img = Image.open(main_img+'_819x452.'+extension)
		print "================================================"
		print "IMAGE Size: %s" % siz
		if h > w:
				w_ratio = float(w)/819
				print "W Ratio %s" % w_ratio
				new_height = int(470*w_ratio)
				img = img.resize((int(new_height), int(w)))
				print "Resize Tall: %sx%s" % (w, new_height)
				x1 = 0
				x2 = int(w)
				y1 = int((new_height-int(h))/2)
				y2 = y1+int(h)
				box = (x1, y1, x2, y2)
				print box
				print main_img+'_'+siz+'.'+extension
				img = img.crop(box)
				img.save(main_img+'_'+siz+'.'+extension)
		else:
				h_ratio = float(h)/470
				print "H Ratio: %s" % h_ratio
				new_width = int(819*h_ratio)
				img = img.resize( (int(new_width), int(h) ))
				print "Resize Wide: %sx%s" % (new_width,h)
				# find middle of image for new crop
				x1 = int((new_width-int(w))/2)
				y1 = 0
				y2 = int(h)
				x2 = x1+int(w)
				box = (x1, y1, x2, y2)
				print box
				print main_img+'_'+siz+'.'+extension
				img = img.crop(box)
				img.save(main_img+'_'+siz+'.'+extension)

make_eight_imgs()
print "Done"
