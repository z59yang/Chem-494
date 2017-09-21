from Tkinter import *
import Element_Info as ei


class ICP_PT(Tk):

  def __init__(self):

    Tk.__init__(self)
    self.title("Periodic Table with Polyatomic Interferences in ICP-MS")
    self.topLabel = Label(self, text="Periodic Table of the Elements", font=("Calibri", 35))
    self.topLabel.grid(row=1, column=0, columnspan=40)

    def literature_data(txt):
        toplevel = Toplevel()
        toplevel.title(txt[1])
        blank1 = Label(toplevel, text='                        ')
        label1 = Label(toplevel,font=("Calibri", 20), text=txt[2], justify=LEFT)
        blank2 = Label(toplevel, text='                        ')
        blank3 = Label(toplevel, text='        ')
        nextpage = Button(toplevel, font=("Calibri", 15), text="Go to Experimental Data", width=25, bg="grey",
                          command=lambda expt=txt: experimental_data(expt))
        lastpage = Button(toplevel, font=("Calibri", 15), text="Return", width=25, bg="grey",
                          command=toplevel.destroy)
        lastpage.pack(side=BOTTOM)
        nextpage.pack(side=BOTTOM)
        blank3.pack(side=BOTTOM)
        blank1.pack(side=LEFT)
        label1.pack(side=LEFT)
        blank2.pack(side=LEFT)

    def experimental_data(txt):
        toplevel = Toplevel()
        toplevel.title("Experimental Interference for " + txt[1])
        blank1 = Label(toplevel, text='                        ')
        label1 = Label(toplevel, font=("Calibri", 20), text=txt[3], justify=LEFT)
        blank2 = Label(toplevel, text='                        ')
        blank3 = Label(toplevel, text='        ')
        lastpage = Button(toplevel, font=("Calibri", 15), text="Return", width=20, bg="grey",
                          command=toplevel.destroy)
        lastpage.pack(side=BOTTOM)
        blank3.pack(side=BOTTOM)
        blank1.pack(side=LEFT)
        label1.pack(side=LEFT)
        blank2.pack(side=LEFT)

    # buttons for columns
    column1 = [
        ei.Hydrogen,
        ei.Lithium,
        ei.Sodium,
        ei.Potassium,
        ei.Rubidium,
        ei.Cesium,
        ei.Francium]
    r = 1
    c = 0
    for b in column1:
        Button(self, text=b[0], font=("Calibri", 20), width=5, height=2, bg="orange", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column2 = [
        ei.Beryllium,
        ei.Magnesium,
        ei.Calcium,
        ei.Strontium,
        ei.Barium,
        ei.Radium]
    r = 2
    c = 1
    for b in column2:
        Button(self, text=b[0], font=("Calibri", 20), width=5, height=2, bg="yellow", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column3 = [
        ei.Scandium,
        ei.Yttrium,
        ei.Lanthanum,
        ei.Actinium]
    r = 4
    c = 2
    for b in column3:
        Button(self, text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column4 = [
        ei.Titanium,
        ei.Zirconium,
        ei.Hanium,
        ei.Rutherfordium]
    r = 4
    c = 3
    for b in column4:
        Button(self, text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column5 = [
        ei.Vanadium,
        ei.Niobium,
        ei.Tantalum,
        ei.Hahnium]
    r = 4
    c = 4
    for b in column5:
        Button(self, text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column6 = [
        ei.Chromium,
        ei.Molybdenum,
        ei.Tungsten,
        ei.Seaborgium]
    r = 4
    c = 5
    for b in column6:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column7 = [
        ei.Manganese,
        ei.Technetium,
        ei.Rhenium,
        ei.Bohrium]
    r = 4
    c = 6
    for b in column7:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column8 = [
        ei.Iron,
        ei.Ruthenium,
        ei.Osmium,
        ei.Hassium]
    r = 4
    c = 7
    for b in column8:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column9 = [
        ei.Cobalt,
        ei.Rhodium,
        ei.Iridium,
        ei.Meitnerium]
    r = 4
    c = 8
    for b in column9:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column10 = [
        ei.Nickle,
        ei.Palladium,
        ei.Platinum]
    r = 4
    c = 9
    for b in column10:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column11 = [
        ei.Copper,
        ei.Silver,
        ei.Gold]
    r = 4
    c = 10
    for b in column11:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column12 = [
        ei.Zinc,
        ei.Cadmium,
        ei.Mercury]
    r = 4
    c = 11
    for b in column12:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="pink", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column13_1 = [
        ei.Boron]
    r = 2
    c = 12
    for b in column13_1:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column13_2 = [
        ei.Aluminum,
        ei.Gallium,
        ei.Indium,
        ei.Thallium]
    r = 3
    c = 12
    for b in column13_2:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column14_1 = [
        ei.Carbon]
    r = 2
    c = 13
    for b in column14_1:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column14_2 = [
        ei.Silicon,
        ei.Germanium]
    r = 3
    c = 13
    for b in column14_2:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column14_3 = [
        ei.Tin,
        ei.Lead]
    r = 5
    c = 13
    for b in column14_3:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light blue", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column15_1 = [
        ei.Nitrogen,
        ei.Phosphorus]
    r = 2
    c = 14
    for b in column15_1:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column15_2 = [
        ei.Arsenic,
        ei.Antimony]
    r = 4
    c = 14
    for b in column15_2:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column15_3 = [
        ei.Bismuth]
    r = 6
    c = 14
    for b in column15_3:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light blue", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column16_1 = [
        ei.Oxygen,
        ei.Sulfur,
        ei.Selenium]
    r = 2
    c = 15
    for b in column16_1:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    column16_2 = [
        ei.Tellurium,
        ei.Polonium]
    r = 5
    c = 15
    for b in column16_2:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="light green", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column17 = [
        ei.Fluorine,
        ei.Chlorine,
        ei.Bromine,
        ei.Iodine,
        ei.Astatine]
    r = 2
    c = 16
    for b in column17:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="violet", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1


    column18 = [
        ei.Helium,
        ei.Neon,
        ei.Argon,
        ei.Krypton,
        ei.Xenon,
        ei.Radon]
    r = 1
    c = 17
    for b in column18:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="purple", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        r += 1
        if r > 7:
            r = 1
            c += 1

    self.fillerLine = Label(self, text = "")
    self.fillerLine.grid(row=8, column=0)

    lanthanoids =[
        ei.Cerium,
        ei.Praseodymium,
        ei.Neodymium,
        ei.Promethium,
        ei.Samarium,
        ei.Europium,
        ei.Gadolinium,
        ei.Terbium,
        ei.Dyprosium,
        ei.Holmium,
        ei.Erbium,
        ei.Thulium,
        ei.Ytterbium,
        ei.Lutetium]
    r = 11
    c = 3
    for b in lanthanoids:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="goldenrod", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        c += 1
        if r > 18:
            c = 1
            r += 1

    actinoids =[
        ei.Thorium,
        ei.Protactinium,
        ei.Uranium,
        ei.Neptunium,
        ei.Plutonium,
        ei.Americium,
        ei.Curium,
        ei.Berkelium,
        ei.Californium,
        ei.Einsteinium,
        ei.Fermium,
        ei.Mendelevium,
        ei.Nobelium,
        ei.Lawrencium]
    r = 12
    c = 3
    for b in actinoids:
        Button(self,text=b[0], font=("Calibri", 20), width=5, height=2, bg="goldenrod", command=lambda text=b: literature_data(text)).grid(row=r, column=c)
        c += 1
        if r > 18:
            c = 1
            r += 1

    self.mainloop()


def main():
    ICP_PT()

if __name__ == "__main__":
    main()
