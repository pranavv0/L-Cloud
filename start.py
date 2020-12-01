from server import *
import _thread
from tkinter import *

class Console:
    serverobj = ServerSocket()
    def start(self):
        self.serverobj.startRecv()
    def stop(self):
        self.serverobj.stopRecv()

SERVER = Console()
SERVER.start()
#server = Tk()

#server.title('Server')
#Label(text="SERVER", bg= "black",fg="white", height="2", width="300", font = ("Calibri",13)).pack()
#Label(text="").pack()

#Button(text="Start",bg= "grey", height="2", width="30", command=SERVER.start ).pack()
#Label(text="").pack()
#Button(text="Stop", bg= "grey", height="2", width="30", command=SERVER.stop ).pack()
#Label(text="").pack()

#Label(root,text='BestWorker Cloud Server',font='Times 20 bold',fg='#ff0099',justify=CENTER).pack(padx=10,pady=10,side=TOP,fill=X)


#Button(root,text='Stop',command = SERVER.stop,width=20,height=3,bg='#ff0011',font='Times 15 bold italic',fg='#000099').pack(padx=10,pady=10,side=LEFT)
#server.mainloop()
