import pyqrcode 
import png 
from pyqrcode import QRCode 
from PIL import Image, ImageFont, ImageDraw
import string, random, os
import pathlib

dirqr = "qr\\"
diroutput = "output\\"

pathlib.Path(dirqr).mkdir(parents=True, exist_ok=True)
pathlib.Path(diroutput).mkdir(parents=True, exist_ok=True)

for x in os.listdir("qr"): os.remove(dirqr+x)
for x in os.listdir("output"): os.remove(diroutput+x)

# txtnya = [''.join(random.sample(string.digits, 10)) for x in range(5)]
f = open("nomor.txt", "r")
txtnya = f.read().split("\n")
f.close()
for k, x in enumerate(txtnya):
	url = pyqrcode.create(x)
	url.png(f'qr\\{x}.png', scale = 10, quiet_zone=0)
	print(f"Success: {k+1}. {x}")

print("-"*50)
for k, x in enumerate(os.listdir("qr")):
	tmptxt = x.split(".")[0]
	txt = f"{tmptxt[:4]} {tmptxt[4:7]} {tmptxt[7:10]}"

	img = Image.open(dirqr+x, 'r')
	img_w, img_h = img.size

	basewidth = 177
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	# background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
	background = Image.open("templateempy.png", "r")
	bg_w, bg_h = background.size
	# offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
	image_editable = ImageDraw.Draw(background)
	title_font = ImageFont.truetype('credit-card.regular.ttf', 63)
	title_text = txt
	# image_editable.text((212, 255), title_text, (227,193,70), font=title_font)
	image_editable.text((280, 255), title_text, (2,30,94), font=title_font)
	image_editable.text((280, 255), title_text, (0,125,183), font=title_font)

	offset = (783, 413)
	background.paste(img, offset)
	# image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
	# image_editable.text((15,15), "2313 673 992", (000, 000, 000), font=title_font)

	# background = background.resize((1011,636), Image.ANTIALIAS)
	background.save(f'{diroutput}{tmptxt}.png')
	print(f"Image: {k+1} {x}")