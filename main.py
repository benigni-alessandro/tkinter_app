import tkinter
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# ventana
ws = tkinter.Tk()
ws.title("Estraer pdf text :D")
ws.geometry('500x700')
ws.config(bg='yellow')
filetxt = ""


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
button = tkinter.Button(ws, textvariable= text_caricamento, command = lambda:loading(filetxt), bg="yellow", fg="black", 
width=12, height=3, relief = "groove" )
text_caricamento.set("SELECT")
button.place(x=220, y = 150)


def loading(filetxt):
    text_caricamento.set("LOADING FILE")
    file = askopenfile(parent=ws, mode="rb", title="Choose a file", filetype=[("Pdf file","*.pdf")])
    if file:
        print('FILE UPLOADED')
        read_file = PyPDF2.PdfFileReader(file)
        n_pages = read_file.getNumPages()
        i=0
        for i in range(n_pages):
            page = read_file.getPage(i)
            text_page = page.extractText()
            filetxt = filetxt + text_page 
            i=i+1
        print(i)
        text_box = tkinter.Text(ws, height= 50, width = 50) 
        text_box.insert(1.0, filetxt)
        text_box.place(x=50, y=250)
        text_caricamento.set("UPLOADED")
       
ws.mainloop()
