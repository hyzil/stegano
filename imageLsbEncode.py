from PIL import Image
import bitarray

# supports latin_1 text encoding and subsequently ascii
def image_lsb_encode(file_name, message):
    # add a end of transmission character to the end of the message
    EOT = chr(4)
    message = message + EOT

    # convert the message into a array of bits
    ba = bitarray.bitarray()
    ba.frombytes(message.encode(encoding="latin_1", errors="replace"))
    bit_array = [int(i) for i in ba]

    # duplicate the original picture
    new_file_name = "media/lsb_" + file_name.split("/")[-1]
    im = Image.open(file_name)
    im.save(new_file_name)

    im = Image.open(new_file_name)
    width, height = im.size
    pixels = im.load()

    i = 0
    # iterate over all pixels in image. break if we reach end of message
    for y in range(0,height):
        for x in range(0,width):
            r,g,b = pixels[x,y]

            # default values in case no bit has to be modified
            new_red_pixel = r
            new_green_pixel = g
            new_blue_pixel = b

            if i < len(bit_array):
                new_red_pixel = get_new_bits(bin(r), bit_array[i])
                i+=1

            if i < len(bit_array):
                new_green_pixel = get_new_bits(bin(g), bit_array[i])
                i+=1

            if i < len(bit_array):
                new_blue_pixel = get_new_bits(bin(b), bit_array[i])
                i+=1

            pixels[x,y] = (new_red_pixel,new_green_pixel,new_blue_pixel)

            if i >= len(bit_array):
                break
        if i >= len(bit_array):
                break

    im.save(new_file_name)
    im.close()
    
def get_new_bits(old_bits, new_bit):
    new_bits = int(old_bits[:-1]+str(new_bit),2)
    return new_bits

def get_max_message_len(file_name):
    im = Image.open(file_name)
    width, height = im.size
    im.close()
    return int(width * height / 8)