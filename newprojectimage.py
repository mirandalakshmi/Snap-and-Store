from PIL import Image ,ImageDraw, ImageFont                                                                                
img = Image.open('d://apython/College.jpg')
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',90)
d = ImageDraw.Draw(img)
d.text((800,600),text="Address by Rev.Fr.Alex in Compein'20 (An Intercollegiate Competition) ",fill=(0,255,0),font=font)
img.show()
img.rotate(45).show()
img.resize((128, 128)).show()



