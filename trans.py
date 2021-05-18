from tkinter import *
import sqlite3
import time
HEIGHT = 900
WEIDTH = 1600

######### CURRENT DATE ##############3
gmt_time = time.gmtime()
current_Date = str(gmt_time[0]) + "-" +  str(gmt_time[1]) + "-" +  str(gmt_time[2])

Depature_List = ["Siloam", "Biaba", "Thohoyandou", "Thathe", "Thengwe", "Soweto", "Tshiawelo", "Zola", "Tswane"]
Destination_List = ["Thathe", "Sibasa", "Makhado", "Shongwe", "Milaboni", "Sihambe", "Thembisa", "sandton", "Mapila"] #destination Not Dist

depart_Time = ["07:00", "07:45", "08:30", "09:00", "09:15", "09:30", "10:00", "10:15"]
arrival_Time = ["09:30", "10:00", "11:15", "11:00", "12:15", "12:30", "13:00", "14:45"]

class DataStorage:
      pass

class Functions():

      def get_Adult_Number(self):
            user_Object = User_Interface()
            #user_Object.
            pass
      def get_Children_Number(self):
            pass
      pass
class User_Interface():
      #HEIGHT = 600
      #WEIDTH = 600

      #def __init__(self):
      def main(self):
            root = Tk()
            root.title("TRANSPORT")
            root.configure(background="#000122")
            canvas = Canvas(root, height=HEIGHT, width = WEIDTH, bg = "#000122")
            canvas.pack()

            header_Frame = Frame(canvas, bg ="white")
            header_Frame.place(relwidth = 0.90, relheight = 0.1, relx = 0.05, rely=0.05)

            # ================= ********** HEADER INFORMATION ***********==========================#
            header_Text = Label(header_Frame, text = "TRANSPORT MANAGEMENT", fg = "gray", bg="white", font = 20)
            header_Text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)
            header_date_text = Label(header_Frame, text = current_Date, bg = "white", fg="gray", font = 16)
            header_date_text.place(relwidth = 0.3, relheight = 0.4, relx = 0.8, rely=0.55)
            
            dest_Label_Info = Label(canvas, text = "Destinations", bg = "white", font = 12)
            dest_Label_Info.place(relwidth = 0.2, relheight = 0.05, relx = 0.05, rely = 0.18)

            dest_Time_Info = Label(canvas, text = "Depart Time", bg = "white", font = 12)
            dest_Time_Info.place(relwidth = 0.2, relheight = 0.05, relx = 0.52, rely = 0.18)

            dest_Time_Info = Label(canvas, text = "Arrival Time", bg = "white", font = 12)
            dest_Time_Info.place(relwidth = 0.2, relheight = 0.05, relx = 0.75, rely = 0.18)            

            depart_Label_Info = Label(canvas, text = "From", bg ="white", font = 12 )
            depart_Label_Info.place(relwidth = 0.2, relheight = 0.05, relx = 0.28, rely = 0.18)
            ######################## BODY FRAME ###############3############3

            body_Frame = Frame(canvas, bg = "white")
            body_Frame.place(relwidth = 0.43, relheight = 0.5, relx = 0.05, rely = 0.25)

            r = StringVar()
            r.set(0)
            Radiobutton(body_Frame, text=Destination_List[0], font = 12, variable=r, value=1, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.02)
            Radiobutton(body_Frame, text=Destination_List[1], font = 12, variable=r, value=2, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.14)
            Radiobutton(body_Frame, text=Destination_List[2], font = 12, variable=r, value=3, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.26)
            Radiobutton(body_Frame, text=Destination_List[3], font = 12, variable=r, value=4, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.38)
            Radiobutton(body_Frame, text=Destination_List[4], font = 12, variable=r, value=5, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.4)
            Radiobutton(body_Frame, text=Destination_List[5], font = 12, variable=r, value=6, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.52)
            Radiobutton(body_Frame, text=Destination_List[6], font = 12, variable=r, value=7, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.64)
            Radiobutton(body_Frame, text=Destination_List[7], font = 12, variable=r, value=8, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.76)
            Radiobutton(body_Frame, text=Destination_List[8], font = 12, variable=r, value=9, anchor = W).place(relwidth =0.45,
             relheight=0.1, relx =0.02, rely=0.88)

            body_Frame_2 = Frame(canvas, bg = "white")
            body_Frame_2.place(relwidth = 0.43, relheight = 0.5, relx = 0.52, rely = 0.25)

            v = StringVar()
            v.set(0)
            Radiobutton(body_Frame, text=Depature_List[0], font = 12, variable = v, value=1, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.02)
            Radiobutton(body_Frame, text=Depature_List[1], font = 12, variable = v, value=2, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.14)
            Radiobutton(body_Frame, text=Depature_List[2], font = 12, variable = v, value=3, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.26)
            Radiobutton(body_Frame, text=Depature_List[3], font = 12, variable = v, value=4, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.38)
            Radiobutton(body_Frame, text=Depature_List[4], font = 12, variable = v, value=5, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.4)
            Radiobutton(body_Frame, text=Depature_List[5], font = 12, variable = v, value=6, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.52)
            Radiobutton(body_Frame, text=Depature_List[6], font = 12, variable = v, value=7, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.64)
            Radiobutton(body_Frame, text=Depature_List[7], font = 12, variable = v, value=8, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.76)
            Radiobutton(body_Frame, text=Depature_List[8], font = 12, variable = v, value=9, anchor = W).place(relwidth =0.45,
             relheight =0.1, relx = 0.53, rely = 0.88)

            ################ footer Frame ##############################
            footer_Frame = Frame(canvas, bg="white")
            footer_Frame.place(relwidth = 0.9, relheight = 0.17, relx = 0.05, rely = 0.78)

            adult_Label = Label(footer_Frame, text="Number of Adults", font = 12)
            adult_Label.place(relwidth= 0.2 , relheight= 0.25, relx= 0.02, rely=0.2)

            adult_Label_Entry = Entry(footer_Frame, font=12)
            adult_Label_Entry.place(relwidth= 0.2 , relheight= 0.25, relx= 0.24, rely=0.2)

            child_Label = Label(footer_Frame, text="Number of Children", font = 12)
            child_Label.place(relwidth= 0.2 , relheight= 0.25, relx= 0.02, rely=0.65)

            child_Label_Entry = Entry(footer_Frame, font=12)
            child_Label_Entry.place(relwidth= 0.2 , relheight= 0.25, relx= 0.24, rely=0.65)

            price_label = Label(footer_Frame, text = "Price R 250", font=12)
            price_label.place(relwidth= 0.4 , relheight= 0.3, relx= 0.52, rely=0.6)

            #################### total Number of Passengers ########################
            total_Passengers_Label = Label(footer_Frame, text="Total Number Of Passengers ", font = 16)
            total_Passengers_Label.place(relwidth = 0.4, relheight = 0.3, relx= 0.52, rely=0.18)

            root.mainloop()

transMain = User_Interface()
transMain.main()