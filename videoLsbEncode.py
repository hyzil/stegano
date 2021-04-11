import bitarray
import cv2
from PIL import Image

# accepted video formats are avi
def video_lsb_encode(file_name, message):
    # add a end of transmission character to the end of the message
    EOT = chr(4)
    message = message + EOT
    
    # convert the message into a array of bits
    ba = bitarray.bitarray()
    ba.frombytes(message.encode(encoding="latin_1", errors="replace"))
    bit_array = [int(i) for i in ba]

    # open video for reading
    orig_file = file_name
    new_file = "media/lsb_" + orig_file.split("/")[-1]
    cap = cv2.VideoCapture(orig_file)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"HFYU")
    out = cv2.VideoWriter(new_file,fourcc, fps, (width,height))
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for y in range(0,height):
            for x in range(0,width):
                r,g,b = frame[y,x]

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

                frame[y,x] = (new_red_pixel,new_green_pixel,new_blue_pixel)
                
                if i >= len(bit_array):
                    break
            if i >= len(bit_array):
                    break
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def get_new_bits(old_bits, new_bit):
    new_bits = int(old_bits[:-1]+str(new_bit),2)
    return new_bits

def get_max_message_len(file_name):
    cap = cv2.VideoCapture(file_name)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return int(width * height * total_frames / 8)
