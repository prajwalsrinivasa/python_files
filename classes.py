class enemy:
    life= 3

    def attack(self):
        print("you are caught")
        self.life -= 1

    def checklife(self,en):
        if self.life<=0:
            print("you have lost every chances")
        else:
            print(str(self.life)+'chances left' '' +en)
    def whatisthis_game(self):
         print("hi this is a simple game")

enemy1 = enemy()
enemy2 = enemy()

enemy1.attack()
enemy1.whatisthis_game()
enemy1.checklife('enemyone')
enemy2.checklife('enemytwo')
enemy1.checklife('enemyone')
enemy2.attack()


