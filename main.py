from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import audioLsbDecode
import audioLsbEncode
import imageLsbDecode
import imageLsbEncode

#filename = askopenfilename()

window = Tk()
window.geometry("600x800")

def base_view():
    supported_formats1.pack(padx=15, pady=15)
    supported_formats2.pack(padx=15, pady=15)
    file_chooser1.pack(padx=15, pady=10)
    file_chooser2.pack(padx=15, pady=10)
    message_field1.pack_forget()
    message_field2.pack_forget()
    file_format_error_label1.pack_forget()
    file_format_error_label2.pack_forget()
    message_error_label1.pack_forget()
    message_error_label2.pack_forget()
    file_name_label1.pack_forget()
    file_name_label2.pack_forget()
    max_char_message1.pack_forget()
    max_char_message2.pack_forget()
    hide_message_button1.pack_forget()
    hide_message_button2.pack_forget()
    message_hidden_success1.pack_forget()
    message_hidden_success2.pack_forget()

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
    message_error_label1.pack_forget()
    hide_message_button1.pack_forget()
    if success:
        message_hidden_success1.pack(padx=15, pady=10)

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

def choose_image_file():
    path = askopenfilename()
    if path:
        filename = path.split("/")[-1]
        if filename.endswith(".png"):
            image_encode_tab_message_view(0,filename)
        else:
            image_encode_tab_initial_view(1,0)

def encode_image_file():
    message = message_field1.get("1.0","end-1c")
    file_name = file_name_label1["text"]
    if len(message) <= imageLsbEncode.get_max_message_len(file_name):
        imageLsbEncode.image_lsb_encode(file_name, message)
        image_encode_tab_initial_view(0, 1)
    else:
        image_encode_tab_message_view(1, file_name)



"""
def choose_audio_file():
    path = askopenfilename()
    if path:
        filename = path.split("/")[-1]
        if filename.endswith((".wav",".flac")):
            audio_encode_tab_message_view(0,filename)
        else:
            audio_encode_tab_initial_view(1)

def encode_audio_file():
"""

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Image LSB":
        image_encode_tab_initial_view(0,0)
    if tab_text == "Audio LSB":
        image_encode_tab_initial_view(0,0)

tab_parent = ttk.Notebook(window)
image_lsb_tab = ttk.Notebook(tab_parent)
audio_lsb_tab = ttk.Notebook(tab_parent)

image_encode_tab = ttk.Frame(image_lsb_tab)
image_decode_tab = ttk.Frame(image_lsb_tab)
audio_encode_tab = ttk.Frame(audio_lsb_tab)
audio_decode_tab = ttk.Frame(audio_lsb_tab)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(image_lsb_tab, text="Image LSB")
tab_parent.add(audio_lsb_tab, text="Audio LSB")
image_lsb_tab.add(image_encode_tab, text="encode")
image_lsb_tab.add(image_decode_tab, text="decode")
audio_lsb_tab.add(audio_encode_tab, text="encode")
audio_lsb_tab.add(audio_decode_tab, text="decode")

supported_formats1 = Label(image_encode_tab, text="Supported File Formats:\npng")
supported_formats2 = Label(audio_encode_tab, text="Supported File Formats:\nwav, flac")

file_chooser1 = Button(image_encode_tab, text="choose file", command=choose_image_file)
file_chooser2 = Button(audio_encode_tab, text="choose file", command=choose_image_file) # change back to audio file

message_field1 = Text(image_encode_tab)
message_field2 = Text(audio_encode_tab)

file_format_error_label1 = Label(image_encode_tab, text="Incompatible file format", fg="red")
file_format_error_label2 = Label(audio_encode_tab, text="Incompatible file format", fg="red")
message_error_label1 = Label(image_encode_tab, text="Message too long", fg="red")
message_error_label2 = Label(audio_encode_tab, text="Message too long", fg="red")

file_name_label1 = Label(image_encode_tab, text="")
file_name_label2 = Label(audio_encode_tab, text="")

max_char_message1 = Label(image_encode_tab, text="Max character length for your message is: ")
max_char_message2 = Label(audio_encode_tab, text="Max character length for your message is: ")

hide_message_button1 = Button(image_encode_tab, text="hide message", command=encode_image_file)
hide_message_button2 = Button(audio_encode_tab, text="hide message", command=choose_image_file) # change command

message_hidden_success1 = Label(image_encode_tab, text="Your message has been hidden")
message_hidden_success2 = Label(audio_encode_tab, text="Your message has been hidden")

base_view()

tab_parent.pack(expand=1, fill="both")

window.mainloop()



