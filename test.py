class Sick:
    def __init__(self, sick_id, duration):
        self.sick_id = sick_id
        self.duration = duration
        # self.doctors_id = doctors_id

    def treatment_amount(self):
        if self.sick_id == 'cancer':
            return 400
        elif self.sick_id == 'influenza':
            return 350.50


calc = Sick(0, 0)
calc.sick_id = input("enter sick id: ")
# print(calc.treatment_amount())


class Cancer(Sick):
    def __init__(self, consult_fee):
        self.consult_fee = consult_fee

    def calcu(self):
        result = calc.treatment_amount() + self.consult_fee
        return result


tot = Cancer(0)
tot.consult_fee = int(input("enter consult fee: "))
print(tot.calcu())
