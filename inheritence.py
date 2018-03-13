class girlfriends():
    names = ('amrutha','pallavi','tushara','jyothi','supritha')
    def names_of_gf(self):
         names = ('amrutha','pallavi','tushara','jyothi','supritha')
       

class myself(girlfriends):
    def me(self):
        print("prajwal has these many crushes")
        print("prajwal's first crush is "+self.names[0])
        print("but life partner is always "+self.names[2])
        
prajwal = myself()
prajwal.me()
prajwal.names_of_gf()
