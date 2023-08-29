from tkinter import*
#from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkinter.ttk import Style

class pharmacy:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1500x800+0+0")
        self.style = Style()
        self.style.theme_use("winnative")
      






        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=FLAT,bg='lightblue',fg="navy",font=("TIMES NEW ROMAN",25,"bold","underline"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
       
        DataFrame=Frame(self.root,bd=15,relief=FLAT,padx=20)   
        DataFrame.place(x=0,y=80,width=1370,height=400) 
        

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=FLAT,padx=20,text="Medicine Info",fg="navy",font=("Times New Roman",15,"bold"))
        DataFrameLeft.place(x=-30,y=3,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=FLAT,padx=20,text="Medicine Add Department",fg="navy",font=("Times New Roman",15,"bold"))
        DataFrameRight.place(x=850,y=3,width=500,height=350)

        ############button frame###########
        ButtonFrame=Frame(self.root,bd=15,relief=FLAT,padx=20)   
        ButtonFrame.place(x=0,y=480,width=1370,height=65) 
        ####### main buttons########
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("Times New Roman",10,"bold"),width=15,bg="dodgerblue3",fg="White",relief=RAISED)
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,text="Update",font=("Times New Roman",10,"bold"),width=14,bg="chartreuse4",fg="white",relief=RAISED)
        btnUpdateMed.grid(row=0,column=1)


        btnDeleteMed=Button(ButtonFrame,text="Delete",font=("Times New Roman",10,"bold"),width=14,bg="Red",fg="white",relief='raised')
        btnDeleteMed.grid(row=0,column=2)

        btnResetMed=Button(ButtonFrame,text="Resest",font=("Times New Roman",10,"bold"),width=14,bg="dodgerblue3",fg="white",relief=RAISED)
        btnResetMed.grid(row=0,column=3)

        showAll=Button(ButtonFrame,text="Show All",font=("Times New Roman",10,"bold"),width=14,bg="dodgerblue3",fg="white",relief=RAISED)
        showAll.grid(row=0,column=5)

        ######## Searh button ########
        lblSearch=Label(ButtonFrame,text="Search By",font=("Times New Roman",10,"bold"),width=14,bg="dodgerblue3",fg="white",relief=RAISED)
        lblSearch.grid(row=0,column=6,sticky=W)

        ### variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("Times New Roman",10,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=15)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=SOLID,width=12,font=("Times New Roman",13,"bold"))
        txtSearch.grid(row=0,column=16)

        searchbtn=Button(ButtonFrame,text="Search",font=("Times New Roman",10,"bold"),width=14,bg="dodgerblue3",fg="white",relief=RAISED)
        searchbtn.grid(row=0,column=17)
        

        ##### labels and entry #######
        lblrefno=Label(DataFrameLeft,text="Reference No",font=("Times New Roman",12,"bold"),padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

      
                          

        ref_combo=ttk.Combobox(DataFrameLeft,width=27,font=("Times New Roman",12,"bold"),state="readonly")
        ref_combo["values"]=("123","456","789")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        
        lblcomp_name=Label(DataFrameLeft,text="Company Name",font=("Times New Roman",12,"bold"),padx=2,pady=6,)
        lblcomp_name.grid(row=1,column=0,sticky=W)
        txtcomp_name=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtcomp_name.grid(row=1,column=1)

        lblTypeMed=Label(DataFrameLeft,text="Type of Medicine",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblTypeMed.grid(row=2,column=0,sticky=W)
        typeMed_combo=ttk.Combobox(DataFrameLeft,width=27,font=("Times New Roman",12,"bold"),state="readonly")
        typeMed_combo["values"]=("Tablet","Syrup","Ointment")
        typeMed_combo.grid(row=2,column=1)
        typeMed_combo.current(0)

        lblMedname=Label(DataFrameLeft,text="Name of Medicine",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblMedname.grid(row=3,column=0,sticky=W)


        Medname_combo=ttk.Combobox(DataFrameLeft,width=27,font=("Times New Roman",12,"bold"),state="readonly")
        Medname_combo["values"]=("abc","def","ghi")
        Medname_combo.grid(row=3,column=1)
        Medname_combo.current(0)

        lbllot_no=Label(DataFrameLeft,text="Lot Number",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lbllot_no.grid(row=4,column=0,sticky=W)
        txtlot_no=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtlot_no.grid(row=4,column=1)

        lblIssue_date=Label(DataFrameLeft,text="Issue Date(YYYY-MM-DD)",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblIssue_date.grid(row=5,column=0,sticky=W)
        txtIssue_date=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtIssue_date.grid(row=5,column=1)

        lblExp_date=Label(DataFrameLeft,text="Exp Date(YYYY-MM-DD)",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblExp_date.grid(row=6,column=0,sticky=W)
        txtExp_date=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtExp_date.grid(row=6,column=1)

        lbluses=Label(DataFrameLeft,text="Uses",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lbluses.grid(row=7,column=0,sticky=W)
        txtuses=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtuses.grid(row=7,column=1)

        lblside_effect=Label(DataFrameLeft,text="Side Effect ",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblside_effect.grid(row=8,column=0,sticky=W)
        txtside_effect=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtside_effect.grid(row=8,column=1)

        lblPrec_warning=Label(DataFrameLeft,text="Prescription Warning ",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblPrec_warning.grid(row=0,column=4,sticky=W)
        txtPrec_warning=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtPrec_warning.grid(row=0,column=5)

        lblDosage=Label(DataFrameLeft,text="Dosage",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblDosage.grid(row=1,column=4,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtDosage.grid(row=1,column=5)

        lblPrice=Label(DataFrameLeft,text="Price",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblPrice.grid(row=2,column=4,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtPrice.grid(row=2,column=5)

        lblQty=Label(DataFrameLeft,text="Quantity",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblQty.grid(row=3,column=4,sticky=W)
        txtQty=Entry(DataFrameLeft,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=29)
        txtQty.grid(row=3,column=5)
        
      
        ###### right side #####
        lblref=Label(DataFrameRight,text="Reference No",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblref.place(x=0,y=0)
        txtref=Entry(DataFrameRight,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=20)
        txtref.place(x=118,y=5,width=200)

        lblmed=Label(DataFrameRight,text="Medicine Name",font=("Times New Roman",12,"bold"),padx=2,pady=6)
        lblmed.place(x=0,y=30)
        txtmed=Entry(DataFrameRight,font=("Times New Roman",12,"bold"),bg="white",bd=2,relief=SOLID,width=25)
        txtmed.place(x=118,y=35,width=200)

        #### side frame right ####
        side_frame=Frame(DataFrameRight,bd=4,relief=FLAT,bg="white")
        side_frame.place(x=0,y=80,width=250,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>", lambda event: self.Medget_cursor(event))

        ######## Medicine add button #####
       

        btnAddmed=Button(DataFrameRight,text="Add",font=("Times New Roman",10,"bold"),width=15,bg="dodgerblue",fg="white",relief=RAISED)
        btnAddmed.place(x=300, y=110)

        btnUpdatemed=Button(DataFrameRight,text="Update",font=("Times New Roman",10,"bold"),width=15,bg="chartreuse4",fg="white",relief=RAISED)
        btnUpdatemed.place(x=300, y=140)

        btnDeletemed=Button(DataFrameRight,text="Delete",font=("Times New Roman",10,"bold"),width=15,bg="red",fg="white",relief=RAISED)
        btnDeletemed.place(x=300, y=170)

        btnClearmed=Button(DataFrameRight,text="Clear",font=("Times New Roman",10,"bold"),width=15,bg="dodgerblue",fg="white",relief=RAISED)
        btnClearmed.place(x=300, y=200)

       


           ### bottom frame ####
        frame_details=Frame(self.root,bd=4,relief=FLAT)
        frame_details.place(x=0,y=550,width=1350,height=250)

        ##### main table and scrollbar ######
        frame_table=Frame(frame_details,bd=15,relief=FLAT,padx=20)
        frame_table.place(x=0,y=0,width=1350,height=150)


        scroll_x=ttk.Scrollbar(frame_table,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(frame_table,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(frame_table,column=("Reg","Compname","type","lotno","Issuedate","Expdate","sideeffect","warning","dosage","price","qty","medicinename","Uses"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        

        self.pharmacy_table.heading("Reg",text="Reference No")
        self.pharmacy_table.heading("Compname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
       
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("Issuedate",text="Issue Date")
        self.pharmacy_table.heading("Expdate",text="Exp date")
       
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("qty",text="Quantity")
        self.pharmacy_table.heading("medicinename",text="Medicine Name")
        self.pharmacy_table.heading("Uses",text="Uses")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("Reg",width=100)
        self.pharmacy_table.column("Compname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("Issuedate",width=100)
        self.pharmacy_table.column("Expdate",width=100)
       
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("qty",width=100)
        self.pharmacy_table.column("medicinename",width=100)
        self.pharmacy_table.column("Uses",width=100)



   
if __name__ == '__main__':
    root=Tk()
    obj=pharmacy(root)
    root.mainloop()