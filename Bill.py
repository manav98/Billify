from tkinter import *


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # =====================================CUSTOMER DETAILS FRAME===================================================

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20)
        cname_txt = Entry(F1, width=15, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Contact Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20)
        cphn_txt = Entry(F1, width=15, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20)
        c_bill_txt = Entry(F1, width=15, font=("arial", 15), bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, pady=15,
                                                                                        padx=5)

        # =========================================COSMETICS FRAME======================================================

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Bath soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)
        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)
        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        Hair_s_lbl = Label(F2, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        body_lsn_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_lsn_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)

        # =========================================GROCERY FRAME======================================================

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        bath_lbl = Label(F3, text="Bath soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)
        face_cream_lbl = Label(F3, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)
        face_w_lbl = Label(F3, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        Hair_s_lbl = Label(F3, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        hair_g_lbl = Label(F3, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        body_lsn_lbl = Label(F3, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_lsn_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)

        # =========================================COLD DRINK FRAME=====================================================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drink", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        bath_lbl = Label(F4, text="Bath soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)
        face_cream_lbl = Label(F4, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)
        face_w_lbl = Label(F4, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        Hair_s_lbl = Label(F4, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        hair_g_lbl = Label(F4, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        body_lsn_lbl = Label(F4, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_lsn_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)
        # ========================================= BILLING FRAME ======================================================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=185, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ========================================= BUTTON FRAME ======================================================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20,
                                                                  pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20,
                                                                  pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20,
                                                                  pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Cess", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20,
                                                                  pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Cess", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20,
                                                                  pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Cess", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20,
                                                                  pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=740, width=620, height=105)

        total_btn = Button(btn_F, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                           font="arial 15 bold").grid(row=0, column=0, padx=5,
                                                      pady=5)
        gBill_btn = Button(btn_F, text="Generate Bill", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                           font="arial 15 bold").grid(row=0, column=1, padx=5,
                                                      pady=5)
        clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                           font="arial 15 bold").grid(row=0, column=2, padx=5,
                                                      pady=5)
        exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                          font="arial 15 bold").grid(row=0, column=3, padx=5,
                                                     pady=5)


root = Tk()
obj = Bill_App(root)
root.mainloop()
