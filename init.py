class enemy:
    energy =0
    def __init__(self,x):
            print("this is init function")
            self.energy = x


    def lives(self):
            print("this function regarding lives"+str(self.energy))
            
enemy1 = enemy(5)
enemy1.lives()
