from PIL import Image

def image_lsb_decode():
    im = Image.open("media/lsb_tree.png")
    pixels = im.load()
    width, height = im.size
    extracted = ''
    end_of_message = 0
    chars = []

    i = 0
    # iterate over pixels of image
    for y in range(0,height):
        for x in range(0,width):
            r,g,b = pixels[x,y]
            # store LSB of each color of each pixel
            extracted += bin(r)[-1]
            extracted += bin(g)[-1]
            extracted += bin(b)[-1]
            # every 8 extracted bits decode and check for EOT
            if len(extracted) > 0 and len(extracted)%8 == 0:
                # if EOT, then message is found
                byte = extracted[i*8:(i+1)*8]
                if int(byte, 2) == 4:
                    end_of_message = 1
                    break
                chars.append(chr(int(byte, 2)))
                i+=1
        if end_of_message:
            break
    print(''.join(chars))

image_lsb_decode()