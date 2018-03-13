class played_games():
    def games(self):
        print("volleyball,kho-kho,chess,cricket")

class certs(played_games):
    def got_certs(self):
        print("kho-kho")

class well_played(certs):
    def district(self):
        print("kho-kho")


prajwal = well_played()
prajwal.games()
prajwal.got_certs()
praju = certs()
praju.games()
