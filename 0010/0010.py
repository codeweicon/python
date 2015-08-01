import Image, ImageFont, ImageDraw, ImageFilter
# f = Image.open('test.jpg')
# f.show('display')
import string
import random
def getRandomColor():
	return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
code = ''.join([random.choice(string.letters) for _ in range(4)]) #!!attention!!

print code
ff = Image.new('RGB',(300,100),(180,180,180))
fonts = ImageFont.truetype('Futura.ttf',40)

draw = ImageDraw.Draw(ff)
draw.text((120,30),str(code),font=fonts, fill="red")
for _ in range(random.randint(1500,3000)):
    draw.point((random.randint(0,300), random.randint(0,100)), fill=getRandomColor())
ff = ff.filter(ImageFilter.BLUR)
ff.save(str(code)+'.jpg', format=None)
ff.show('display')