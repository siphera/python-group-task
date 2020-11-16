class Sick:
    pass


class Influenza(Sick):      # Class influenza
    def __init__(self, medication,consultation):        # init method
        self.medication = medication
        self.consultation= consultation
        
    def treatment(self):        # Method treatment
        if self.consultation > 600:
            self.amount = self.medication + self.consultation * 0.98
            print(self.amount)
        else:
            self.amount = self.medication + self.consultation
            print(self.amount)


# instantiate object e.g(obj_od) and properties e.g (.medication = 400)
obj_od = Influenza(0, 0)
obj_od.medication = 350.50
obj_od.consultation = 900
obj_od.treatment()

class Cancer(Sick):
    def __init__(self, medication, scan_fee):
        self.medication = medication
        self.scan_fee = scan_fee

    def can(self):
        if self.scan_fee > 600:
            print("Sorry we cannot treat you")
        else:
            self.total = self.medication + self.scan_fee
            print(self.total)


obj_od = Cancer(0, 0)
obj_od.medication = 400
obj_od.scan_fee = 601
obj_od.can()
