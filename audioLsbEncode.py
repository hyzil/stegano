import soundfile as sf
import bitarray
from mutagen.flac import FLAC

# supports audio file types supported by Libsndfile that can be represented by int16. use loseless formats
# tested with FLAC and WAV. Only Flac is supported with keeping metadata on the steganised audio
# supports latin_1 text encoding and subsequently ascii
def audio_lsb_encode(file_name, message):
    # add a end of transmission character to the end of the message
    EOT = chr(4)
    message = message + EOT

    # Convert the message into a array of bits
    ba = bitarray.bitarray()
    ba.frombytes(message.encode(encoding="latin_1", errors="replace"))
    bit_array = [int(i) for i in ba]

    new_file_name = "media/lsb_" + file_name.split("/")[-1]

    i=0
    # open the original audio file
    with sf.SoundFile(file_name, "r") as audio:
        audio_data = audio.read(frames=-1, dtype='int16')

        # iterate over the frames on each channel of sound and change least sig bits
        for channel in range(0,audio.channels):
            for frame in range(0,audio.frames):
                if i < len(bit_array):
                    old_frame = audio_data[frame][channel]
                    # create duplicate frame with no sign
                    old_frame_dup = old_frame
                    if old_frame_dup < 0:
                        old_frame_dup *= -1
                    audio_data[frame][channel] = get_new_frame(bin(old_frame_dup), bit_array[i], old_frame < 0)

                    i+=1
                if i >= len(bit_array):
                    break
            if i >= len(bit_array):
                break

        # write the changed audio data to a new file
        sf.write(new_file_name, audio_data, audio.samplerate)
        
        # write FLAC metadata into new audiofile
        if audio.format == "FLAC":
            orig_audio = FLAC(file_name)
            orig_audio.save(new_file_name)
            
        audio.close()

def get_new_frame(old_bits, new_bit, is_negative):
    new_frame = int(old_bits[:-1]+str(new_bit),2)
    if is_negative:
        return new_frame * -1
    return new_frame

def get_max_message_len(file_name):
    max_bits = 0
    with sf.SoundFile(file_name, "r") as audio:
        max_bits = audio.frames*audio.channels
        audio.close()
    return int(max_bits / 8)