import tkinter,PyPDF2
from tkinter import filedialog


def openFile():
     filename = filedialog.askopenfilename(title="Open PDF file", 
                                                  initialdir='E:\PYTHON STUFF',
                                                  filetypes=[('PDF files', '*.pdf')])
     print(filename)
     outputfile_text.delete("1.0",tkinter.END)
     filename_label.configure(text=filename)
     reader = PyPDF2.PdfReader(filename)
     for i in range(len(reader.pages)):
          current_text = reader.pages[i].extract_text()
          outputfile_text.insert(tkinter.END,current_text)

root = tkinter.Tk()
root.title("PDF TO TEXT By Jahin")

filename_label = tkinter.Label(root , text="No file is selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root,text="Select pdf file",command=openFile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()



root.mainloop()