from PIL import Image

def image_lsb_decode(file_name):
    im = Image.open(file_name)
    pixels = im.load()
    width, height = im.size
    gap = pseudo_random_seq(width*height)
    cur_gap = 0
    extracted = ''
    end_of_message = 0
    chars = []

    i = 0
    # iterate over pixels of image
    for y in range(0,height):
        for x in range(0,width):
            r,g,b = pixels[x,y]
            if cur_gap == gap:
                gap = pseudo_random_seq(gap)
                cur_gap = 0
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
            cur_gap+=1
        if end_of_message:
            break
    im.close()
    if end_of_message:
        return "".join(chars)
    else:
        return ""

def pseudo_random_seq(seed):
    mod1 = seed + 127
    mod2 = 461
    mult = 5
    add = 129
    return (mult*seed+add)%mod1%mod2+4