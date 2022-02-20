import tkinter
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# ventana
ws = tkinter.Tk()
ws.title("Estraer pdf text :D")
ws.geometry('500x700')
ws.config(bg='yellow')



#background
bg_image = Image.open("images/sfondo1.jpg")
bg_image = bg_image.resize((500, 700), Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(bg_image)

label = tkinter.Label(
    ws,
    image=photoimg
)
label.place(x=0, y=0)
  

#reglas
istruccion = tkinter.Label(ws, text="Elegir file pdf desde tu ordenador...", bg="black", fg="white", font=15)
istruccion.pack(fill=tkinter.X)
istruccion.place(x=150, y = 5)

text_caricamento = tkinter.StringVar()
button = tkinter.Button(ws, textvariable= text_caricamento, command = lambda:loading(), bg="red", fg="white", width=10, height=3)
text_caricamento.set("Select")
button.place(x=220, y = 150)


def loading():
    text_caricamento.set("loading file")
    file = askopenfile(parent=ws, mode="rb", title="Choose a file", filetype=[("Pdf file","*.pdf")])
    if file:
        print('gg')
        read_file = PyPDF2.PdfFileReader(file)
        page = read_file.getPage(0)
        text_file = page.extractText()
        text_box = tkinter.Text(ws, height= 50, width = 50)
        text_box.insert(1.0, text_file)
        text_box.place(x=50, y=250)

       
ws.mainloop()