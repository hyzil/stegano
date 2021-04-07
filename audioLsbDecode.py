import soundfile as sf
import struct

def audio_lsb_decode():
    with sf.SoundFile("media/lsb_Tartaglia1.wav", "r") as audio:
        audio_data = audio.read(frames=-1, dtype='int16')
        extracted = ""
        end_of_message = 0
        chars = []

        i = 0
        for channel in range(0,audio.channels):
            for frame in range(0,audio.frames):
                cur_frame = audio_data[frame][channel]
                
                extracted += bin(cur_frame)[-1]
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
    