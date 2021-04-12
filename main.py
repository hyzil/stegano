from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import audioLsbDecode
import audioLsbEncode
import imageLsbDecode
import imageLsbEncode
import videoLsbDecode
import videoLsbEncode

window = Tk()
window.geometry("600x800")

def image_encode_tab_initial_view(error, success):
    supported_formats1.pack(padx=15, pady=10)
    file_chooser1["text"] = "choose file"
    file_chooser1.pack(padx=15, pady=10)
    file_name_label1.pack_forget()
    max_char_message1.pack_forget()
    message_field1.delete(1.0,END)
    message_field1.pack_forget()
    if error:
        file_format_error_label1.pack(padx=15, pady=10)
        message_hidden_success1.pack_forget()
    message_error_label1.pack_forget()
    hide_message_button1.pack_forget()
    if success:
        message_hidden_success1.pack(padx=15, pady=10)
        file_format_error_label1.pack_forget()
    if not error or success:
        file_format_error_label1.pack_forget()
        message_hidden_success1.pack_forget()

def image_encode_tab_message_view(error, file_name):
    supported_formats1.pack(padx=15, pady=10)
    file_chooser1["text"] = "change file"
    file_chooser1.pack(padx=15, pady=10)
    file_name_label1["text"] = file_name
    file_name_label1.pack(padx=15, pady=10)
    max_char_message1["text"] = "Max character length for your message is: " + str(imageLsbEncode.get_max_message_len(file_name))
    max_char_message1.pack(padx=15, pady=10)
    message_field1.pack(padx=15, pady=10)
    file_format_error_label1.pack_forget()
    if error:
        message_error_label1.pack(padx=15, pady=10)
    hide_message_button1.pack(padx=15, pady=15)
    message_hidden_success1.pack_forget()

def image_decode_tab_initial_view(initial, file_name):
    supported_formats3.pack(padx=15, pady=10)
    file_chooser3["text"] = "choose file"
    file_chooser3.pack(padx=15, pady=10)
    if initial:
        file_format_error_label3.pack_forget()
        file_name_label3.pack_forget()
        find_message_button1.pack_forget()
    elif file_name and not initial:
        file_name_label3["text"] = file_name
        file_name_label3.pack(padx=15, pady=10)
        find_message_button1.pack(padx=15, pady=10)
        file_format_error_label3.pack_forget()
    else:
        file_format_error_label3.pack(padx=15, pady=10)
        file_name_label3.pack_forget()
        find_message_button1.pack_forget()
    message_field3.delete(1.0,END)
    message_field3.pack_forget()
    message_error_label3.pack_forget()

def image_decode_tab_message_view(error, file_name, message):
    supported_formats3.pack(padx=15, pady=10)
    file_chooser3["text"] = "change file"
    file_chooser3.pack(padx=15, pady=10)
    file_name_label3["text"] = file_name
    file_name_label3.pack(padx=15, pady=10)
    if not error:
        message_field3.delete(1.0,END)
        message_field3.insert(1.0,message)
        message_field3.pack(padx=15, pady=10)
    file_format_error_label3.pack_forget()
    if error:
        message_error_label3.pack(padx=15, pady=10)
    find_message_button1.pack_forget()

def audio_encode_tab_initial_view(error, success):
    supported_formats2.pack(padx=15, pady=10)
    file_chooser2["text"] = "choose file"
    file_chooser2.pack(padx=15, pady=10)
    file_name_label2.pack_forget()
    max_char_message2.pack_forget()
    message_field2.delete(1.0,END)
    message_field2.pack_forget()
    if error:
        file_format_error_label2.pack(padx=15, pady=10)
        message_hidden_success2.pack_forget()
    message_error_label2.pack_forget()
    hide_message_button2.pack_forget()
    if success:
        message_hidden_success2.pack(padx=15, pady=10)
        file_format_error_label2.pack_forget()
    if not error or success:
        file_format_error_label2.pack_forget()
        message_hidden_success2.pack_forget()

def audio_encode_tab_message_view(error, file_name):
    supported_formats2.pack(padx=15, pady=10)
    file_chooser2["text"] = "change file"
    file_chooser2.pack(padx=15, pady=10)
    file_name_label2["text"] = file_name
    file_name_label2.pack(padx=15, pady=10)
    max_char_message2["text"] = "Max character length for your message is: " + str(audioLsbEncode.get_max_message_len(file_name))
    max_char_message2.pack(padx=15, pady=10)
    message_field2.pack(padx=15, pady=10)
    file_format_error_label2.pack_forget()
    if error:
        message_error_label2.pack(padx=15, pady=10)
    hide_message_button2.pack(padx=15, pady=15)
    message_hidden_success2.pack_forget()

def audio_decode_tab_initial_view(initial, file_name):
    supported_formats4.pack(padx=15, pady=10)
    file_chooser4["text"] = "choose file"
    file_chooser4.pack(padx=15, pady=10)
    if initial:
        file_format_error_label4.pack_forget()
        file_name_label4.pack_forget()
        find_message_button2.pack_forget()
    elif file_name and not initial:
        file_name_label4["text"] = file_name
        file_name_label4.pack(padx=15, pady=10)
        find_message_button2.pack(padx=15, pady=10)
        file_format_error_label4.pack_forget()
    else:
        file_format_error_label4.pack(padx=15, pady=10)
        file_name_label4.pack_forget()
        find_message_button2.pack_forget()
    message_field4.delete(1.0,END)
    message_field4.pack_forget()
    message_error_label4.pack_forget()

def audio_decode_tab_message_view(error, file_name, message):
    supported_formats4.pack(padx=15, pady=10)
    file_chooser4["text"] = "change file"
    file_chooser4.pack(padx=15, pady=10)
    file_name_label4["text"] = file_name
    file_name_label4.pack(padx=15, pady=10)
    if not error:
        message_field4.delete(1.0,END)
        message_field4.insert(1.0,message)
        message_field4.pack(padx=15, pady=10)
    file_format_error_label4.pack_forget()
    if error:
        message_error_label4.pack(padx=15, pady=10)
    find_message_button2.pack_forget()

def video_encode_tab_initial_view(error, success):
    supported_formats5.pack(padx=15, pady=10)
    file_chooser5["text"] = "choose file"
    file_chooser5.pack(padx=15, pady=10)
    file_name_label5.pack_forget()
    max_char_message3.pack_forget()
    message_field5.delete(1.0,END)
    message_field5.pack_forget()
    if error:
        file_format_error_label5.pack(padx=15, pady=10)
        message_hidden_success3.pack_forget()
    message_error_label5.pack_forget()
    hide_message_button3.pack_forget()
    if success:
        message_hidden_success3.pack(padx=15, pady=10)
        file_format_error_label5.pack_forget()
    if not error or success:
        file_format_error_label5.pack_forget()
        message_hidden_success3.pack_forget()


def video_encode_tab_message_view(error, file_name):
    supported_formats5.pack(padx=15, pady=10)
    file_chooser5["text"] = "change file"
    file_chooser5.pack(padx=15, pady=10)
    file_name_label5["text"] = file_name
    file_name_label5.pack(padx=15, pady=10)
    max_char_message3["text"] = "Max character length for your message is: " + str(videoLsbEncode.get_max_message_len(file_name))
    max_char_message3.pack(padx=15, pady=10)
    message_field5.pack(padx=15, pady=10)
    file_format_error_label5.pack_forget()
    if error:
        message_error_label5.pack(padx=15, pady=10)
    hide_message_button3.pack(padx=15, pady=15)
    message_hidden_success3.pack_forget()

def video_decode_tab_initial_view(initial,file_name):
    supported_formats6.pack(padx=15, pady=10)
    file_chooser6["text"] = "choose file"
    file_chooser6.pack(padx=15, pady=10)
    if initial:
        file_format_error_label6.pack_forget()
        file_name_label6.pack_forget()
        find_message_button3.pack_forget()
    elif file_name:
        file_name_label6["text"] = file_name
        file_name_label6.pack(padx=15, pady=10)
        find_message_button3.pack(padx=15, pady=10)
        file_format_error_label6.pack_forget()
    else:
        file_format_error_label6.pack(padx=15, pady=10)
        file_name_label6.pack_forget()
        find_message_button3.pack_forget()
    message_field6.delete(1.0,END)
    message_field6.pack_forget()
    message_error_label6.pack_forget()

def video_decode_tab_message_view(error, file_name, message):
    supported_formats6.pack(padx=15, pady=10)
    file_chooser6["text"] = "change file"
    file_chooser6.pack(padx=15, pady=10)
    file_name_label6["text"] = file_name
    file_name_label6.pack(padx=15, pady=10)
    if not error:
        message_field6.delete(1.0,END)
        message_field6.insert(1.0,message)
        message_field6.pack(padx=15, pady=10)
    file_format_error_label6.pack_forget()
    if error:
        message_error_label6.pack(padx=15, pady=10)
    find_message_button3.pack_forget()

def encode_choose_image_file():
    path = askopenfilename()
    if path:
        filename = path.split("/")[-1]
        if filename.endswith((".png")):
            global image_encode_path
            image_encode_path = path
            image_encode_tab_message_view(0,filename)
        else:
            image_encode_tab_initial_view(1,0)

def encode_image_hide_message():
    message = message_field1.get("1.0","end-1c")
    file_name = file_name_label1["text"]
    if len(message)-1 <= imageLsbEncode.get_max_message_len(image_encode_path):
        imageLsbEncode.image_lsb_encode(image_encode_path, message)
        image_encode_tab_initial_view(0, 1)
    else:
        image_encode_tab_message_view(1, file_name)

def decode_choose_image_file():
    path = askopenfilename()
    if path:
        file_name = path.split("/")[-1]
        if file_name.endswith(".png"):
            global image_decode_path
            image_decode_path = path
            image_decode_tab_initial_view(False,file_name)
        else:
            image_decode_tab_initial_view(False,"")

def decode_image_find_message():
    file_name = file_name_label3["text"]
    message = imageLsbDecode.image_lsb_decode(image_decode_path)
    if message:
        image_decode_tab_message_view(0, file_name, message)
    else:
        image_decode_tab_message_view(1, file_name, message)

def encode_choose_audio_file():
    path = askopenfilename()
    if path:
        filename = path.split("/")[-1]
        if filename.endswith(("wav","flac")):
            global audio_encode_path
            audio_encode_path = path
            audio_encode_tab_message_view(0, filename)
        else:
            audio_encode_tab_initial_view(1, 0)

def encode_audio_hide_message():
    message = message_field2.get("1.0","end-1c")
    file_name = file_name_label2["text"]
    if len(message)-1 <= audioLsbEncode.get_max_message_len(audio_encode_path):
        audioLsbEncode.audio_lsb_encode(audio_encode_path, message)
        audio_encode_tab_initial_view(0, 1)
    else:
        audio_encode_tab_message_view(1, file_name)

def decode_choose_audio_file():
    path = askopenfilename()
    if path:
        file_name = path.split("/")[-1]
        if file_name.endswith(("wav","flac")):
            global audio_decode_path
            audio_decode_path = path
            audio_decode_tab_initial_view(False,file_name)
        else:
            audio_decode_tab_initial_view(False,"")

def decode_audio_find_message():
    file_name = file_name_label4["text"]
    message = audioLsbDecode.audio_lsb_decode(audio_decode_path)
    if message:
        audio_decode_tab_message_view(0, file_name, message)
    else:
        audio_decode_tab_message_view(1, file_name, message)

def encode_choose_video_file():
    path = askopenfilename()
    if path:
        filename = path.split("/")[-1]
        if filename.endswith((".avi")):
            global video_encode_path
            video_encode_path = path
            video_encode_tab_message_view(0,filename)
        else:
            video_encode_tab_initial_view(1,0)

def encode_video_hide_message():
    message = message_field5.get("1.0","end-1c")
    file_name = file_name_label5["text"]
    if len(message)-1 <= videoLsbEncode.get_max_message_len(video_encode_path):
        videoLsbEncode.video_lsb_encode(video_encode_path, message)
        video_encode_tab_initial_view(0, 1)
    else:
        video_encode_tab_message_view(1, file_name)

def decode_choose_video_file():
    path = askopenfilename()
    if path:
        file_name = path.split("/")[-1]
        if file_name.endswith(".avi"):
            global video_decode_path
            video_decode_path = path
            video_decode_tab_initial_view(False,file_name)
        else:
            video_decode_tab_initial_view(False,"")

def decode_video_find_message():
    file_name = file_name_label6["text"]
    message = videoLsbDecode.video_lsb_decode(video_decode_path)
    print(message)
    if message:
        video_decode_tab_message_view(0, file_name, message)
    else:
        video_decode_tab_message_view(1, file_name, message)

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Image LSB":
        image_encode_tab_initial_view(0,0)
    elif tab_text == "Audio LSB":
        audio_encode_tab_initial_view(0,0)
    elif tab_text == "Video LSB":
        video_encode_tab_initial_view(0,0)
    elif tab_text == "image encode":
        image_encode_tab_initial_view(0,0)
    elif tab_text == "image decode":
        image_decode_tab_initial_view(True,"")
    elif tab_text == "audio encode":
        audio_encode_tab_initial_view(0,0)
    elif tab_text == "audio decode":
        audio_decode_tab_initial_view(True,"")
    elif tab_text == "video encode":
        video_encode_tab_initial_view(0,0)
    elif tab_text == "video decode":
        video_decode_tab_initial_view(True,"")

tab_parent = ttk.Notebook(window)
image_lsb_tab = ttk.Notebook(tab_parent)
audio_lsb_tab = ttk.Notebook(tab_parent)
video_lsb_tab = ttk.Notebook(tab_parent)

image_encode_tab = ttk.Frame(image_lsb_tab)
image_decode_tab = ttk.Frame(image_lsb_tab)
audio_encode_tab = ttk.Frame(audio_lsb_tab)
audio_decode_tab = ttk.Frame(audio_lsb_tab)
video_encode_tab = ttk.Frame(video_lsb_tab)
video_decode_tab = ttk.Frame(video_lsb_tab)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(image_lsb_tab, text="Image LSB")
tab_parent.add(audio_lsb_tab, text="Audio LSB")
tab_parent.add(video_lsb_tab, text="Video LSB")
image_lsb_tab.bind("<<NotebookTabChanged>>", on_tab_selected)
audio_lsb_tab.bind("<<NotebookTabChanged>>", on_tab_selected)
video_lsb_tab.bind("<<NotebookTabChanged>>", on_tab_selected)
image_lsb_tab.add(image_encode_tab, text="image encode")
image_lsb_tab.add(image_decode_tab, text="image decode")
audio_lsb_tab.add(audio_encode_tab, text="audio encode")
audio_lsb_tab.add(audio_decode_tab, text="audio decode")
video_lsb_tab.add(video_encode_tab, text="video encode")
video_lsb_tab.add(video_decode_tab, text="video decode")

supported_formats1 = Label(image_encode_tab, text="Supported File Formats: png")
supported_formats2 = Label(audio_encode_tab, text="Supported File Formats: wav, flac")
supported_formats3 = Label(image_decode_tab, text="Supported File Formats: png")
supported_formats4 = Label(audio_decode_tab, text="Supported File Formats: wav, flac")
supported_formats5 = Label(video_encode_tab, text="Supported File Formats: avi")
supported_formats6 = Label(video_decode_tab, text="Supported File Formats: avi")

file_chooser1 = Button(image_encode_tab, text="choose file", command=encode_choose_image_file)
file_chooser2 = Button(audio_encode_tab, text="choose file", command=encode_choose_audio_file)
file_chooser3 = Button(image_decode_tab, text="choose file", command=decode_choose_image_file)
file_chooser4 = Button(audio_decode_tab, text="choose file", command=decode_choose_audio_file)
file_chooser5 = Button(video_encode_tab, text="choose file", command=encode_choose_video_file)
file_chooser6 = Button(video_decode_tab, text="choose file", command=decode_choose_video_file)

message_field1 = Text(image_encode_tab)
message_field2 = Text(audio_encode_tab)
message_field3 = Text(image_decode_tab)
message_field4 = Text(audio_decode_tab)
message_field5 = Text(video_encode_tab)
message_field6 = Text(video_decode_tab)

file_format_error_label1 = Label(image_encode_tab, text="Incompatible file format", fg="red")
file_format_error_label2 = Label(audio_encode_tab, text="Incompatible file format", fg="red")
file_format_error_label3 = Label(image_decode_tab, text="Incompatible file format", fg="red")
file_format_error_label4 = Label(audio_decode_tab, text="Incompatible file format", fg="red")
file_format_error_label5 = Label(video_encode_tab, text="Incompatible file format", fg="red")
file_format_error_label6 = Label(video_decode_tab, text="Incompatible file format", fg="red")
message_error_label1 = Label(image_encode_tab, text="Message too long", fg="red")
message_error_label2 = Label(audio_encode_tab, text="Message too long", fg="red")
message_error_label3 = Label(image_decode_tab, text="No message found", fg="red")
message_error_label4 = Label(audio_decode_tab, text="No message found", fg="red")
message_error_label5 = Label(video_encode_tab, text="Message too long", fg="red")
message_error_label6 = Label(video_decode_tab, text="No message found", fg="red")

file_name_label1 = Label(image_encode_tab, text="")
file_name_label2 = Label(audio_encode_tab, text="")
file_name_label3 = Label(image_decode_tab, text="")
file_name_label4 = Label(audio_decode_tab, text="")
file_name_label5 = Label(video_encode_tab, text="")
file_name_label6 = Label(video_decode_tab, text="")

max_char_message1 = Label(image_encode_tab, text="Max character length for your message is: ")
max_char_message2 = Label(audio_encode_tab, text="Max character length for your message is: ")
max_char_message3 = Label(video_encode_tab, text="Max character length for your message is: ")

hide_message_button1 = Button(image_encode_tab, text="hide message", command=encode_image_hide_message)
hide_message_button2 = Button(audio_encode_tab, text="hide message", command=encode_audio_hide_message)
find_message_button1 = Button(image_decode_tab, text="find message", command=decode_image_find_message)
find_message_button2 = Button(audio_decode_tab, text="find message", command=decode_audio_find_message)
hide_message_button3 = Button(video_encode_tab, text="hide message", command=encode_video_hide_message)
find_message_button3 = Button(video_decode_tab, text="find message", command=decode_video_find_message)


message_hidden_success1 = Label(image_encode_tab, text="Your message has been hidden")
message_hidden_success2 = Label(audio_encode_tab, text="Your message has been hidden")
message_hidden_success3 = Label(video_encode_tab, text="Your message has been hidden")

image_encode_path = ""
image_decode_path = ""
audio_encode_path = ""
audio_decode_path = ""
video_encode_path = ""
video_decode_path = ""

image_encode_tab_initial_view(0,0)

tab_parent.pack(expand=1, fill="both")

window.mainloop()