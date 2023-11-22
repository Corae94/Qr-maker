import tkinter
import tkinter.filedialog
import tkinter.messagebox
import turtle
import segno


# noinspection PyMethodMayBeStatic
class QRMaker:

    def __init__(self):
        self.__choice = ["write text which will be converted", "choose a text file to get converted"]
        self.__root = tkinter.Tk()
        self.__root.title("QR code maker")
        self.__root.eval('tk::PlaceWindow . center')
        self.__root.protocol("WM_DELETE_WINDOW", self.__close)
        self.__root.grid()
        tkinter.Label(self.__root, text='choose the input method from the menu', width=37).grid(row=0, column=0)
        self.__variable = tkinter.StringVar(self.__root)
        self.__variable.set(self.__choice[0])
        self.__selection = tkinter.OptionMenu(self.__root, self.__variable, *self.__choice)
        self.__selection.grid(row=1, column=0)
        tkinter.Button(self.__root, text='Confirm', command=lambda: self.__choice_execution(self.__variable.get())).grid(row=2, column=0)
        tkinter.Button(self.__root, text='Info', command=self.__info).grid(row=0, column=1)
        self.__root.mainloop()

    def __info(self):
        tkinter.messagebox.showinfo(title='Info', message='Autore: Corae94\nSi ringraziano:\nla caffeina\nle ore di sonno perse\ni neuroni che si son dati all\'ippica\n  ∧_∧\n( ̳• · • ̳)\n/    づ ☕︎')

    def __choice_execution(self, variable):
        if variable == self.__choice[0]:
            writer = self.__write_text()
            if writer is not None:
                qr = segno.make_qr(writer)
                name = self.__name_input()
                if name is not None:
                    path = self.__select_directory()
                    if path is not None:
                        try:
                            qr.save(path + '/' + name + '.png', scale=5)
                            tkinter.messagebox.showinfo(title='Info', message=('il file è stato salvato con questo '
                                                                               'path assoluto: '+path+'/'+name+'.png'))
                        except IOError as ioe:
                            print('Error: \n\t' + ioe.strerror)
        elif variable == self.__choice[1]:
            text_from_file = self.__open_text_file()
            if text_from_file is not None:
                qr = segno.make_qr(text_from_file)
                name = self.__name_input()
                if name is not None:
                    path = self.__select_directory()
                    if path is not None:
                        try:
                            qr.save(path + '/' + name + '.png', scale=5)
                            tkinter.messagebox.showinfo(title='Info', message=('il file è stato salvato con questo '
                                                                               'path assoluto: '+path+'/'+name+'.png'))
                        except IOError as ioe:
                            print('Error: \n\t' + ioe.strerror)

    def __write_text(self):
        master = tkinter.Tk()
        master.withdraw()
        c = tkinter.Canvas(master=master)
        t = turtle.TurtleScreen(c)
        text = t.textinput('Insert text', 'Text here')
        c.destroy()
        master.destroy()
        return text

    def __select_directory(self):
        return tkinter.filedialog.askdirectory(title='Select the target location for the qr code')

    def __name_input(self):
        master = tkinter.Tk()
        master.withdraw()
        c = tkinter.Canvas(master=master)
        t = turtle.TurtleScreen(c)
        text = t.textinput('Insert name of file', 'Name here')
        c.destroy()
        master.destroy()
        return text

    def __open_text_file(self):
        try:
            file = tkinter.filedialog.askopenfile(title='Select the target text file to convert to QR')
            line = file.read()
            file.close()
            return line
        except IOError as ioe:
            print('Error: \n\t' + ioe.strerror)

    def __close(self):
        self.__root.destroy()


if __name__ == '__main__':
    qr_maker = QRMaker()
