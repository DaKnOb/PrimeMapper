##
#DaKnOb#
# daknob.mac@gmail.com #
##

import Tkinter
def factors(n):
    r = 0

    for i in range(1, int((n + 1)/2)+1):
        if n % i == 0:
            r = r + 1

    return r+1

class App:
    def __init__(self, t):
        
        wid = 64        #Width of the final image
        hei = 8192      #Height of the final image
        fin = 84015     #Number to go to
        fnm = "PrimeMap"  #File name to export
        
        self.i = Tkinter.PhotoImage(width=wid,height=hei)
        row = 0; col = 0   
        
        primes = 0
        
        for num in range(1, fin):
            ss = factors(num)
            if(ss==2):
                primes = primes + 1
                rps = str(bin(num))[2::].zfill(wid-4)
                rpg = wid-4
                for rep in rps:
                    if(rep == "0"):
                        self.i.put("#f00", (wid-rpg, primes))
                    else:
                        self.i.put("#0f0", (wid-rpg, primes))
                    rpg = rpg - 1
        
        self.i.write(fnm + ".gif", format="gif")
        c = Tkinter.Canvas(t, width=wid, height=hei); c.pack()
        c.create_image(0, 0, image = self.i, anchor=Tkinter.NW)

t = Tkinter.Tk()
a = App(t)    
t.mainloop()