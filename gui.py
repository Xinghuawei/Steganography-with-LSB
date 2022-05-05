from tkinter import *
from tkinter import messagebox
from argparse import FileType
from tkinter.filedialog import *
from PIL import ImageTk, Image
from subprocess import Popen
import os
from encode_image import encode_image
from decode_image import decode_image
from helper import ceaser_enc, decode_cipher
"""
Xinghua Wei A00978597
COMP 8505 Assignment 2
Staganography 
"""

#encode function
def encode_gui():

    #encode panel
    root.destroy()
    enc_canv=Tk()
    enc_canv.title("Encode Panel")
    enc_canv.geometry("800x900")
    
    #encode panel backgournd
    bg_enc_image=ImageTk.PhotoImage(Image.open("background/bg_2.jpg"))
    label_enc = Label(enc_canv,text="image",image=bg_enc_image)
    label_enc.pack()
    
    
    #encode message
    label_enc_message =Label(text="Password(No number)",bg="Black",fg="white")
    label_enc_message.place(relx=0.1, rely=0.1, height=25, width=120)
    entrysecmes=Entry()
    entrysecmes.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.200)

    #encode output file name
    label_out_filename =Label(text="File Output Name",bg="Black",fg="white")
    label_out_filename.place(relx=0.1, rely=0.2, height=25, width=120)
    entrysave=Entry()
    entrysave.place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.200)

    # #cyper
    # cyper_msg =Label(text="Password",bg="Black",fg="white")
    # cyper_msg.place(relx=0.53, rely=0.2, height=25, width=120)
    # entrypwd=Entry()
    # entrypwd.place(relx=0.7, rely=0.2, relheight=0.05, relwidth=0.200)

    #carrier file open button
    openfile_button=Button(text='Open Carrier File',fg="white",bg="black",width=20,command=openfile)
    openfile_button.place(relx=0.1,rely=0.3)

    def open_hide_file():
        global hide_fileopen
        global hide_display_image
        #open file 	
        hide_fileopen=StringVar()
        hide_fileopen=askopenfilename(initialdir="/Desktop",title="select file",
        filetypes=(("png, png files","*png"),("all files","*.*"))) 
        hide_display_image=ImageTk.PhotoImage(Image.open(hide_fileopen).resize((200,150), Image.ANTIALIAS))
    
        #file path label	
        hide_label_path=Label(text=hide_fileopen)
        hide_label_path.place(relx=0.3, rely=0.6, height=21, width=450)
        
        #display image
        hide_label_display_image=Label(image=hide_display_image)
        hide_label_display_image.place(relx=0.3, rely=0.64, height=200, width=300)



    #actual hidden image file open button
    hide_openfile_button=Button(text='Open Hide File',fg="white",bg="black",width=20,command=open_hide_file)
    hide_openfile_button.place(relx=0.1,rely=0.6)
    
    #image type choice radio button
    image_type=StringVar()
    radio_bmp=Radiobutton(text='bmp',value='bmp',variable=image_type)
    radio_bmp.place(relx=0.19, rely=0.37)
	
    radio_jepg=Radiobutton(text='jpg',value='jpg',variable=image_type)
    radio_jepg.place(relx=0.19, rely=0.47)
    
    #encode message to image function. 
    def encode_gui():
        pwd_len = len(entrysecmes.get())
        if pwd_len != 4:
            messagebox.showinfo("Notice","Password must be 4 chars without any numbers, eg \"abcd\"")
        
        if image_type.get()=="bmp":
            image_carrier=Image.open(fileopen)
            image_hidden=Image.open(hide_fileopen)
            resp = messagebox.askyesno("Notice","Encode using this image?")
            if resp == 1:
                try:
                    image_carrier.convert('RGB')
                    encoded_image = encode_image(image_carrier,image_hidden)
                    pwd_data=entrysecmes.get()
                    pwd_data_enc = ceaser_enc(pwd_data)
                    # newimg=image_to_enc.copy()
                    # encode_enc(newimg,data)
                    new_img_name=entrysave.get()+ pwd_data_enc + '.bmp'
                    encoded_image.save(new_img_name, str(new_img_name.split(".")[1].upper()))
                    messagebox.showinfo("Notice","successfully encode"+entrysave.get()+".bmp")
                except:
                    messagebox.showinfo("Notice","Failed to encode,encode png to a bmp image")

        if image_type.get()=="jpg":
            image_carrier=Image.open(fileopen)
            image_hidden=Image.open(hide_fileopen)
            resp = messagebox.askyesno("Notice","Encode using this image?")
            if resp == 1:
                try:
                    image_carrier.convert('RGB')
                    encoded_image = encode_image(image_carrier,image_hidden)
                    pwd_data=entrysecmes.get()
                    pwd_data_enc = ceaser_enc(pwd_data)
                    # encode_enc(newimg,data)
                    new_img_name=entrysave.get()+pwd_data_enc+'.png'
                    encoded_image.save(new_img_name, str(new_img_name.split(".")[1].upper()))
                    messagebox.showinfo("Notice","successfully encode"+entrysave.get()+".png")
                except:
                    messagebox.showinfo("Notice","Failed to encode,encode png to a jpg image")


    def back():
        enc_canv.destroy()
        Popen('python gui.py')
    
    #actual encode function button
    enc_actual_btn = Button(text="ENCODE",fg="white",bg="blue",command=encode_gui)
    enc_actual_btn.place(relx=0.2, rely=0.92, height=31, width=94)

    #back button
    back_button = Button(text="Back",fg="white",bg="red",command=back)
    back_button.place(relx=0.6, rely=0.92, height=31, width=94)
    enc_canv.mainloop()




def decode_gui():
    
    root.destroy()
    #Decode panel
    dec_canv=Tk()
    dec_canv.title("Decode Panel")
    dec_canv.geometry("800x600")
    
    #encode panel backgournd
    bg_enc_image=ImageTk.PhotoImage(Image.open("background/bg_2.jpg"))
    label_dec = Label(dec_canv,text="image",image=bg_enc_image)
    label_dec.pack()

    #file open button
    openfile_button=Button(text='Open File',fg="white",bg="black",width=20,command=openfile)
    openfile_button.place(relx=0.1,rely=0.3)

    #decode panel back button
    def back():
        dec_canv.destroy()
        Popen('python gui.py')

    #decode and extract hidden image from carrier image    
    def decode_img():
    
        pwd_len = len(dec_entrypwd.get())

        if pwd_len !=4 :
            messagebox.showinfo("Notice","Password must be 4 chars without any numbers, eg \"abcd\"")
        else:
            #entered password
            uncover_p = dec_entrypwd.get()
            #get file name

            s_carrier=Image.open(fileopen)
            full_name = str(os.path.basename(fileopen))
            #get secrect
            unknow = full_name[-8:-4]
            reveal_unknow = decode_cipher(unknow)
            #check entered password and revealed password
            if reveal_unknow != uncover_p:
                messagebox.showinfo("Notice","Password not correct")
            else:
                resp = messagebox.askyesno("Notice","Decode this image?")
                if resp == 1:
                    try:
                        s_carrier.convert('RGB')
                        decoded_image = decode_image(s_carrier)
                        new_img_name=dec_filename.get()+'.png'
                        decoded_image.save(new_img_name, str(new_img_name.split(".")[1].upper()))
                        messagebox.showinfo("Notice","successfully encode"+dec_filename.get()+".png")

                        #display orginal image
                        dec_canv.destroy()
                        final = Tk()
                        final.title(new_img_name)
                        final_display_image=ImageTk.PhotoImage(decoded_image.resize((800,600), Image.ANTIALIAS))
                        label_ori = Label(final,text="image",image=final_display_image)
                        label_ori.pack()
                        final.mainloop()
                    except:
                        messagebox.showinfo("Notice","Failed to encode,image may not be correct or it is too large")
    #deocde file name
    dec_file_name =Label(text="Output Name",bg="Black",fg="white")
    dec_file_name.place(relx=0.1, rely=0.1, height=25, width=120)
    dec_filename=Entry()
    dec_filename.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.200)

    
    #deocde cyper
    dec_cyper_msg =Label(text="Password",bg="Black",fg="white")
    dec_cyper_msg.place(relx=0.1, rely=0.2, height=25, width=120)
    dec_entrypwd=Entry()
    dec_entrypwd.place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.200)


    #decode button
    decode_button=Button(text='Decode',fg="white",bg="blue",width=20,command=decode_img)
    decode_button.place(relx=0.2,rely=0.8)

    #back button
    back_button = Button(text="Back",fg="white",bg="red",command=back)
    back_button.place(relx=0.6, rely=0.8, height=31, width=94)
    dec_canv.mainloop()

    dec_canv.mainloop()

def exit_btn():
    root.destroy()

def openfile():
    global fileopen
    global display_image

	#open file 	
    fileopen=StringVar()
    
    fileopen=askopenfilename(initialdir="/Desktop",title="select file",
    filetypes=(("bmp, bmp files","*bmp"),("png, png files","*png"),("all files","*.*"))) 
    display_image=ImageTk.PhotoImage(Image.open(fileopen).resize((200,150), Image.ANTIALIAS))
  
    #file path label	
    label_path=Label(text=fileopen)
    label_path.place(relx=0.3, rely=0.3, height=21, width=450)
    
    #display image
    label_display_image=Label(image=display_image)
    label_display_image.place(relx=0.3, rely=0.34, height=200, width=300)





global bg_image
root = Tk()
root.title('Wei Steganograph 8505 Assignment2')
root.geometry("600x300")

#background
bg_image=ImageTk.PhotoImage(Image.open("background/bg_1.jpg"))
label_main = Label(root,text="image",image=bg_image)
label_main.pack()

#main page
#encode button
encode_button=Button(text='Encode',fg="white",bg="black",width=20,command=encode_gui)
encode_button.place(relx=0.2,rely=0.3)
#decode button
decode_button=Button(text='Decode',fg="white",bg="black",width=20,command=decode_gui)
decode_button.place(relx=0.6,rely=0.3)
#exit button
exit_button=Button(text='Exit',fg="white",bg="red",width=20,command=exit_btn)
exit_button.place(relx=0.4,rely=0.7)
root.mainloop()
