from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root  ##here root is window of billing system
        self.root.geometry("1350x700+0+0")  ## height, weidth, X and Y axis of s/w
        self.root.title("Billing System")
        bg_color = "black"  ## background color for complete windows taken dark blue here
        title = Label(self.root, text="Customer Billing System", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 40, "bold"), pady=2).pack(
            fill=X)  ## bd= border, fg= foreground/font color
        ##******************Variables for Cosmetics*************
        self.lotion = IntVar()
        self.fwash = IntVar()
        self.bath = IntVar()
        self.pow = IntVar()
        self.tooth = IntVar()
        self.perfume = IntVar()
        self.shampoo = IntVar()

        ##*******************Variables for General Items**********
        self.bvita = IntVar()
        self.hor = IntVar()
        self.gly = IntVar()
        self.rose = IntVar()
        self.milk = IntVar()
        self.cadb = IntVar()
        self.gel = IntVar()

        ##******************Variables for Cold drinks**************
        self.thumbs = IntVar()
        self.maz = IntVar()
        self.froo = IntVar()
        self.sprite = IntVar()
        self.appy = IntVar()
        self.limca = IntVar()
        self.red = IntVar()

        ##**************Variables for Total price % tax ************
        self.cosmetic_price = StringVar()
        self.general_items_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.general_items_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        ##********Variables for Customer***************
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.bill_search = StringVar()

        ##*****************************Customer Details Frame***********************

        F1 = LabelFrame(self.root, text="Customers Detail", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=90, relwidth=1)

        c_name_label = Label(F1, text="Customer Name:", fg="white", bg=bg_color,
                             font=("times new roman", 20, "bold")).grid(row=0, column=0, padx=20,
                                                                        pady=5)  ## pad= distance from x and y axis
        c_name_txt = Entry(F1, width=15, textvariable=self.c_name, font=("times new roman", 16, "bold"), bd=7,
                           relief=GROOVE).grid(row=0, column=1, padx=10,
                                               pady=5)  ##******Entry field for Customer Name*******

        c_phone_label = Label(F1, text="Customer Phone No.:", fg="white", bg=bg_color,
                              font=("times new roman", 20, "bold")).grid(row=0, column=2, padx=20, pady=5)
        c_phone_txt = Entry(F1, width=15, textvariable=self.c_phone, font=("times new roman", 16, "bold"), bd=7,
                            relief=GROOVE).grid(row=0, column=3, padx=10, pady=5)

        c_bill_label = Label(F1, text="Bill Number:", fg="white", bg=bg_color,
                             font=("times new roman", 20, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.bill_search, font=("times new roman", 16, "bold"), bd=7,
                           relief=GROOVE).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search",command=self.find_bill, font=("aerial", 15, "bold"), width=10, bd=7, ).grid(row=0, column=6,
                                                                                                 padx=10, pady=10)

        ##****************************Cosmetics Frame********************************
        F2 = LabelFrame(self.root, bd=10, text="Cosmetics", font=("times new roman", 20, "bold"), fg="silver",
                        bg=bg_color)
        F2.place(x=5, y=190, width=365, height=430)

        ##***************************Contents of Cosmetics***************************

        lotion_label = Label(F2, text="Body Lotion", fg="light green", bg=bg_color,
                             font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10)
        lotion_txt = Entry(F2, width=12, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5).grid(
            row=0, column=1, padx=10, pady=10)

        fwash_label = Label(F2, text="Facewash", fg="light green", bg=bg_color,
                            font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10)
        fwash_wash_txt = Entry(F2, width=12, textvariable=self.fwash, font=("times new roman", 16, "bold"), bd=5).grid(
            row=1, column=1, padx=10, pady=10)

        bath_label = Label(F2, text="Bath Soap", fg="light green", bg=bg_color,
                           font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10)
        bath_txt = Entry(F2, width=12, textvariable=self.bath, font=("times new roman", 16, "bold"), bd=5).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=10,
                                                                                                                pady=10)

        powder_label = Label(F2, text="Powder", fg="light green", bg=bg_color,
                             font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10)
        powder_txt = Entry(F2, width=12, textvariable=self.pow, font=("times new roman", 16, "bold"), bd=5).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10)

        tooth_paste_label = Label(F2, text="Toothpaste", fg="light green", bg=bg_color,
                                  font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10)
        tooth_paste_txt = Entry(F2, width=12, textvariable=self.tooth, font=("times new roman", 16, "bold"), bd=5).grid(
            row=4, column=1, padx=10, pady=10)

        perfume_label = Label(F2, text="Perfume", fg="light green", bg=bg_color,
                              font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10)
        perfume_txt = Entry(F2, width=12, textvariable=self.perfume, font=("times new roman", 16, "bold"), bd=5).grid(
            row=5, column=1, padx=10, pady=10)

        shampoo_label = Label(F2, text="Shampoo", fg="light green", bg=bg_color,
                              font=("times new roman", 16, "bold")).grid(row=6, column=0, padx=10, pady=10)
        shampoo_txt = Entry(F2, width=12, textvariable=self.shampoo, font=("times new roman", 16, "bold"), bd=5).grid(
            row=6, column=1, padx=10, pady=10)

        ##**************General Items Frame******************

        F3 = LabelFrame(self.root, bd=10, text="General Items", font=("times new roman", 20, "bold"), fg="silver",
                        bg=bg_color)
        F3.place(x=370, y=190, width=385, height=430)

        ##**************Contents of general items*************
        bvita_label = Label(F3, text="Bourn Vita", fg="light green", bg=bg_color,
                            font=("times new roman", 16, "bold")).grid(row=0, column=2, padx=10, pady=10)
        bvita_txt = Entry(F3, width=12, textvariable=self.bvita, font=("times new roman", 16, "bold"), bd=5).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  padx=10,
                                                                                                                  pady=10)

        hor_label = Label(F3, text="Horlicks", fg="light green", bg=bg_color,
                          font=("times new roman", 16, "bold")).grid(row=1, column=2, padx=10, pady=10)
        hor_txt = Entry(F3, width=12, textvariable=self.hor, font=("times new roman", 16, "bold"), bd=5).grid(row=1,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)

        gly_label = Label(F3, text="Glycerine", fg="light green", bg=bg_color,
                          font=("times new roman", 16, "bold")).grid(row=2, column=2, padx=10, pady=10)
        gly_txt = Entry(F3, width=12, textvariable=self.gly, font=("times new roman", 16, "bold"), bd=5).grid(row=2,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)

        rose_label = Label(F3, text="Rose Water", fg="light green", bg=bg_color,
                           font=("times new roman", 16, "bold")).grid(row=3, column=2, padx=10, pady=10)
        rose_txt = Entry(F3, width=12, textvariable=self.rose, font=("times new roman", 16, "bold"), bd=5).grid(row=3,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=10)

        milk_label = Label(F3, text="Milk Powder", fg="light green", bg=bg_color,
                           font=("times new roman", 16, "bold")).grid(row=4, column=2, padx=10, pady=10)
        milk_txt = Entry(F3, width=12, textvariable=self.milk, font=("times new roman", 16, "bold"), bd=5).grid(row=4,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=10)

        cadb_label = Label(F3, text="Cadbury", fg="light green", bg=bg_color,
                           font=("times new roman", 16, "bold")).grid(row=5, column=2, padx=10, pady=10)
        cadb_txt = Entry(F3, width=12, textvariable=self.cadb, font=("times new roman", 16, "bold"), bd=5).grid(row=5,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=10)

        gel_label = Label(F3, text="Hair Gel", fg="light green", bg=bg_color,
                          font=("times new roman", 16, "bold")).grid(row=6, column=2, padx=10, pady=10)
        gel_txt = Entry(F3, width=12, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5).grid(row=6,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)

        ##************************Coldrinks Frame************************************
        F4 = LabelFrame(self.root, bd=10, text="Cold Drinks", font=("times new roman", 20, "bold"), fg="silver",
                        bg=bg_color)
        F4.place(x=755, y=190, width=365, height=430)

        ##************************contents of colddrinks frame*****************************
        thumb_label = Label(F4, text="Thumbs Up", fg="light green", bg=bg_color,
                            font=("times new roman", 16, "bold")).grid(row=0, column=4, padx=10, pady=10)
        thumb_txt = Entry(F4, width=12, textvariable=self.thumbs, font=("times new roman", 16, "bold"), bd=5).grid(
            row=0, column=5, padx=10, pady=10)

        maz_label = Label(F4, text="Maza", fg="light green", bg=bg_color, font=("times new roman", 16, "bold")).grid(
            row=1, column=4, padx=10, pady=10)
        maz_txt = Entry(F4, width=12, textvariable=self.maz, font=("times new roman", 16, "bold"), bd=5).grid(row=1,
                                                                                                              column=5,
                                                                                                              padx=10,
                                                                                                              pady=10)

        froo_label = Label(F4, text="Frooti", fg="light green", bg=bg_color, font=("times new roman", 16, "bold")).grid(
            row=2, column=4, padx=10, pady=10)
        froo_txt = Entry(F4, width=12, textvariable=self.froo, font=("times new roman", 16, "bold"), bd=5).grid(row=2,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=10)

        sprite_label = Label(F4, text="Sprite", fg="light green", bg=bg_color,
                             font=("times new roman", 16, "bold")).grid(row=3, column=4, padx=10, pady=10)
        sprite_txt = Entry(F4, width=12, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5).grid(
            row=3, column=5, padx=10, pady=10)

        appy_label = Label(F4, text="Appy", fg="light green", bg=bg_color, font=("times new roman", 16, "bold")).grid(
            row=4, column=4, padx=10, pady=10)
        appy_txt = Entry(F4, width=12, textvariable=self.appy, font=("times new roman", 16, "bold"), bd=5).grid(row=4,
                                                                                                                column=5,
                                                                                                                padx=10,
                                                                                                                pady=10)

        limca_label = Label(F4, text="Limca", fg="light green", bg=bg_color, font=("times new roman", 16, "bold")).grid(
            row=5, column=4, padx=10, pady=10)
        limca_txt = Entry(F4, width=12, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5).grid(row=5,
                                                                                                                  column=5,
                                                                                                                  padx=10,
                                                                                                                  pady=10)

        red_label = Label(F4, text="Red Bull", fg="light green", bg=bg_color,
                          font=("times new roman", 16, "bold")).grid(row=6, column=4, padx=10, pady=10)
        red_txt = Entry(F4, width=12, textvariable=self.red, font=("times new roman", 16, "bold"), bd=5).grid(row=6,
                                                                                                              column=5,
                                                                                                              padx=10,
                                                                                                              pady=10)

        ##*******************Bill Area********************
        F4 = LabelFrame(self.root, bd=10)
        F4.place(x=1140, y=190, width=390, height=430)
        bill_title = Label(F4, text="Bill Area", bd=5, relief=RAISED, font=("times new roman", 20, "bold")).pack(
            fill=X)  # relief= border decoration
        scrol_Y = Scrollbar(F4, orient=VERTICAL)
        self.textarea = Text(F4, yscrollcommand=scrol_Y.set)
        scrol_Y.pack(side=RIGHT, fill=Y)
        scrol_Y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        ##**************button Frame*****************
        F6 = LabelFrame(self.root, bd=10, text="Bill Menu", font=("times new roman", 20, "bold"), fg="silver",
                        bg=bg_color)
        F6.place(x=0, y=620, relwidth=1, height=190)

        menu1 = Label(F6, text="Total Cosmetic Price (₹) :", fg="light green", bg=bg_color,
                      font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=10)
        menu1_txt = Entry(F6, width=13, textvariable=self.cosmetic_price, font=("times new roman", 13, "bold"),
                          bd=5).grid(row=0, column=1, padx=1, pady=1)

        menu2 = Label(F6, text="Total General Price (₹) :", fg="light green", bg=bg_color,
                      font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=10, pady=10)
        menu2_txt = Entry(F6, width=13, textvariable=self.general_items_price, font=("times new roman", 13, "bold"),
                          bd=5).grid(row=1, column=1, padx=1, pady=1)

        menu3 = Label(F6, text="Total Cold drinks Price (₹) :", fg="light green", bg=bg_color,
                      font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=10, pady=10)
        menu3_txt = Entry(F6, width=13, textvariable=self.cold_drinks_price, font=("times new roman", 13, "bold"),
                          bd=5).grid(row=2, column=1, padx=1, pady=1)

        tax1_lbl = Label(F6, text="Cosmetic Tax :", fg="light green", bg=bg_color,
                         font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=10, pady=10)
        tax1_txt = Entry(F6, width=13, textvariable=self.cosmetic_tax, font=("times new roman", 13, "bold"), bd=5).grid(
            row=0, column=3, padx=10, pady=10)

        tax2_lbl = Label(F6, text="General Tax :", fg="light green", bg=bg_color,
                         font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=10, pady=10)
        tax2_txt = Entry(F6, width=13, textvariable=self.general_items_tax, font=("times new roman", 13, "bold"),
                         bd=5).grid(row=1, column=3, padx=10, pady=10)

        tax3_lbl = Label(F6, text="Cold drinks Tax :", fg="light green", bg=bg_color,
                         font=("times new roman", 15, "bold")).grid(row=2, column=2, padx=10, pady=10)
        tax3_txt = Entry(F6, width=13, textvariable=self.cold_drinks_tax, font=("times new roman", 13, "bold"),
                         bd=5).grid(row=2, column=3, padx=1, pady=1)

        ##***********Button frame for generation of bill, total, clear, exit********************
        btn_F = Frame(F6, bd=7, relief=RAISED)
        btn_F.place(x=780, width=720, height=140)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="black", fg="white", pady=30, width=12, bd=5,
                           font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=5, pady=10)
        bill_btn = Button(btn_F, command=self.Bill_Area, text="Generate Bill", bg="black", fg="white", pady=30,
                          width=12, bd=5, font=("times new roman", 15, "bold")).grid(row=0, column=1, padx=5, pady=10)
        clear_btn = Button(btn_F, text="Clear",command= self.clear_data, bg="black", fg="white", pady=30, width=12, bd=5,
                           font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=5, pady=10)
        exit_btn = Button(btn_F, command= self.Exit_app, text="Exit", bg="black", fg="white", pady=30, width=12, bd=5,
                          font=("times new roman", 15, "bold")).grid(row=0, column=3, padx=5, pady=10)

        self.welcome_bill()
        ##******************************Entry of no.of quantities in every field******************

    def total(self):
        self.cos_lotion_price = self.lotion.get() * 60
        self.cos_fwash_pice = self.fwash.get() * 120
        self.cos_bath_price = self.bath.get() * 40
        self.cos_pow_price = self.pow.get() * 70
        self.cos_tooth_price = self.tooth.get() * 80
        self.cos_perfume_price = self.perfume.get() * 180
        self.cos_shampoo_price = self.shampoo.get() * 100

        self.total_cosmetic_price = float(
            (self.cos_lotion_price) +
            (self.cos_fwash_pice) +
            (self.cos_bath_price) +
            (self.cos_pow_price) +
            (self.cos_tooth_price) +
            (self.cos_perfume_price) +
            (self.cos_shampoo_price)
        )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax = self.total_cosmetic_price * 0.05
        self.cosmetic_tax.set("₹" + str(self.c_tax))

        self.gen_bvita_price = self.bvita.get() * 150
        self.gen_hor_price = self.hor.get() * 150
        self.gen_gly_price = self.gly.get() * 75
        self.gen_rose_price = self.rose.get() * 65
        self.gen_milk_price = self.milk.get() * 90
        self.gen_cadb_price = self.cadb.get() * 120
        self.gen_gel_price = self.gel.get() * 80

        self.total_general_items_price = float(
            (self.gen_bvita_price) +
            (self.gen_hor_price) +
            (self.gen_gly_price) +
            (self.gen_rose_price) +
            (self.gen_milk_price) +
            (self.gen_cadb_price) +
            (self.gen_gel_price)
        )
        self.general_items_price.set(str(self.total_general_items_price))
        self.g_tax = self.total_general_items_price * 0.1
        self.general_items_tax.set("₹" + str(self.g_tax))

        self.cold_thumbs_price = self.thumbs.get() * 80
        self.cold_maz_price = self.maz.get() * 40
        self.cold_froo_price = self.froo.get() * 40
        self.cold_sprite_price = self.sprite.get() * 60
        self.cold_appy_price = self.appy.get() * 50
        self.cold_limca_price = self.limca.get() * 30
        self.cold_red_price = self.red.get() * 70
        self.total_cold_drinks_price = float(
            (self.cold_thumbs_price) +
            (self.cold_maz_price) +
            (self.cold_froo_price) +
            (self.cold_sprite_price) +
            (self.cold_appy_price) +
            (self.cold_limca_price) +
            (self.cold_red_price)
        )
        self.cold_drinks_price.set(str(self.total_cold_drinks_price))
        self.c_d_tax = self.total_cold_drinks_price * 0.05
        self.cold_drinks_tax.set("₹" + str(self.c_d_tax))

        self.Total_bill = "₹" + str(
            self.total_cosmetic_price + self.total_general_items_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    def welcome_bill(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "\t Welcome to Dhokla Shop\n")
        self.textarea.insert(END, f"\n Bill no.: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Customer Phone No.: {self.c_phone.get()}")
        self.textarea.insert(END, "\n ******************************************")
        self.textarea.insert(END, "\n Products\t\t Qty\t\t Price")
        self.textarea.insert(END, "\n ******************************************")

    def Bill_Area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are empty")

        elif self.cosmetic_price.get() == "0.0" and self.general_items_price.get() == "0.0" and self.cold_drinks_price.get() == "0.0":
            messagebox.showerror("Error", "No items purchased")
        else:
            self.welcome_bill()

            ##*************cosmetics bill************
            if self.lotion.get() != 0:
                self.textarea.insert(END, f"\n Body Lotion\t\t {self.lotion.get()}\t\t {self.cos_lotion_price}")

            if self.fwash.get() != 0:
                self.textarea.insert(END, f"\n Face Wash\t\t {self.fwash.get()}\t\t {self.cos_fwash_pice}")

            if self.bath.get() != 0:
                self.textarea.insert(END, f"\n Bath Soap\t\t {self.bath.get()}\t\t {self.cos_bath_price}")

            if self.pow.get() != 0:
                self.textarea.insert(END, f"\n Powder\t\t {self.pow.get()}\t\t {self.cos_pow_price}")

            if self.tooth.get() != 0:
                self.textarea.insert(END, f"\n Tooth Paste\t\t {self.tooth.get()}\t\t {self.cos_tooth_price}")

            if self.perfume.get() != 0:
                self.textarea.insert(END, f"\n Perfume\t\t {self.perfume.get()}\t\t {self.cos_perfume_price}")

            if self.shampoo.get() != 0:
                self.textarea.insert(END, f"\n Shampoo\t\t {self.shampoo.get()}\t\t {self.cos_shampoo_price}")

                ##*************general items************
            if self.bvita.get() != 0:
                self.textarea.insert(END, f"\n Bourn Vita\t\t {self.bvita.get()}\t\t {self.gen_bvita_price}")

            if self.hor.get() != 0:
                self.textarea.insert(END, f"\n Horlicks\t\t {self.hor.get()}\t\t {self.gen_hor_price}")

            if self.gly.get() != 0:
                self.textarea.insert(END, f"\n Glycerine\t\t {self.gly.get()}\t\t {self.gen_gly_price}")

            if self.rose.get() != 0:
                self.textarea.insert(END, f"\n Rose Water\t\t {self.rose.get()}\t\t {self.gen_rose_price}")

            if self.milk.get() != 0:
                self.textarea.insert(END, f"\n Milk Powder\t\t {self.milk.get()}\t\t {self.gen_milk_price}")

            if self.cadb.get() != 0:
                self.textarea.insert(END, f"\n Cadbury\t\t {self.cadb.get()}\t\t {self.gen_cadb_price}")

            if self.gel.get() != 0:
                self.textarea.insert(END, f"\n Hair Gel\t\t {self.gel.get()}\t\t {self.gen_gel_price}")

            ##*************cold drinks bill************
            if self.thumbs.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t {self.thumbs.get()}\t\t {self.cold_thumbs_price}")

            if self.maz.get() != 0:
                self.textarea.insert(END, f"\n Maza\t\t {self.maz.get()}\t\t {self.cold_maz_price}")

            if self.froo.get() != 0:
                self.textarea.insert(END, f"\n Frooti\t\t {self.froo.get()}\t\t {self.cold_froo_price}")

            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t {self.sprite.get()}\t\t {self.cold_sprite_price}")

            if self.appy.get() != 0:
                self.textarea.insert(END, f"\n Appy\t\t {self.appy.get()}\t\t {self.cold_appy_price}")

            if self.limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t {self.limca.get()}\t\t {self.cold_limca_price}")

            if self.red.get() != 0:
                self.textarea.insert(END, f"\n Red Bull\t\t {self.red.get()}\t\t {self.cold_red_price}")

            ##******************Tax representation in bill area*****************
            self.textarea.insert(END, "\n ------------------------------------------")

            if self.cosmetic_tax.get() != "₹0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax\t\t\t\t {self.cosmetic_tax.get()}")

            if self.general_items_tax.get() != "₹0.0":
                self.textarea.insert(END, f"\n General Items Tax\t\t\t\t {self.general_items_tax.get()}")

            if self.cold_drinks_tax.get() != "₹0.0":
                self.textarea.insert(END, f"\n Cold drinks Tax\t\t\t\t {self.cold_drinks_tax.get()}")

            self.textarea.insert(END, "\n ------------------------------------------")
            self.textarea.insert(END, f"\n Total : \t\t\t\t {str(self.Total_bill)}")
            self.textarea.insert(END, "\n ------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            self.bill_info= self.textarea.get('1.0',END)
            f1 = open("bill/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_info)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved successfully")
        else:
            return

            
    def find_bill(self):
        present="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.bill_search.get():
                f1=open(f"bill/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)  
                f1.close()
                present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill No.")    


    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data?")
        if op > 0:
            ##*******************Variables for Cosmetics**********
            self.lotion.set(0)
            self.fwash.set(0)
            self.bath.set(0)
            self.pow.set(0)
            self.tooth.set(0)
            self.perfume.set(0)
            self.shampoo.set(0)

            ##*******************Variables for General Items**********
            self.bvita.set(0)
            self.hor.set(0)
            self.gly.set(0)
            self.rose.set(0)
            self.milk.set(0)
            self.cadb.set(0)
            self.gel.set(0)

            ##******************Variables for Cold drinks**************
            self.thumbs.set(0)
            self.maz.set(0)
            self.froo.set(0)
            self.sprite.set(0)
            self.appy.set(0)
            self.limca.set(0)
            self.red.set(0)

            ##**************Variables for Total price % tax ************
            self.cosmetic_price.set("")
            self.general_items_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetic_tax.set("")
            self.general_items_tax.set("")
            self.cold_drinks_tax.set("")

            ##********Variables for Customer***************
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.bill_search.set("")
            self.welcome_bill()

    def Exit_app(self):
        op= messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)  ## object for class Bill_App
root.mainloop()
   

