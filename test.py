from PIL import Image


orig_file_name = "tree.png"
new_file_name = "weird_" + orig_file_name
im = Image.open(orig_file_name)
im.save(new_file_name)

im = Image.open(new_file_name)
width, height = im.size
pixels = im.load()

for y in range(0,height):
        for x in range(0,width):
            r,g,b = pixels[x,y]
            pixels[x,y] = (r,0,b)
im.save(new_file_name)