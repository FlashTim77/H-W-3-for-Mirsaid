class LIC:
    def __init__(self):
        self.proper = {}

    def create_proper(self, proper_id, vacancies):
        self.proper[proper_id] = vacancies

    def read_proper(self, proper_id):
        return self.proper.get(proper_id)

    def update_proper(self, proper_id, new_vacansies):
        self.proper[proper_id] = new_vacansies

    def delete_proper(self, proper_id):
        del self.proper[proper_id]




class BIL(LIC):
    def __init__(self):
        super().__init__()

    def add_vacan(self, proper_id, level, age):
        self.proper[proper_id]['level'] = level
        self.proper[proper_id]['age'] = age

f_comp = LIC()
s_comp = BIL()

f_comp.create_proper(1, {"LIC Administrator": "Vitaliy"})
f_comp.create_proper(2, {"LIC Manager": "Sergey"})
print(f_comp.read_proper(1))
print(f_comp.read_proper(2))



f_comp.update_proper(1, {"LIC Designer": "Artur"})
f_comp.update_proper(2, {"LIC Marketolog": "Alex"})
print(f_comp.read_proper(1))
print(f_comp.read_proper(2))



f_comp.delete_proper(1)
print(f_comp.read_proper(1))

s_comp.create_proper(3, {"BIL Administrator": "Pavel"})
s_comp.add_vacan(3, "3",  24)
print(s_comp.read_proper(3))

s_comp.create_proper(3, {"BIL Manager": "Veronika"})
s_comp.add_vacan(3, "4", 32)
print(s_comp.read_proper(3))

s_comp.create_proper(4, {"BIL Designer": "Dmitriy"})
s_comp.add_vacan(4, "5", 21)
print(s_comp.read_proper(4))


s_comp.update_proper(5, {"BIL Marketolog": "Bobur"})
s_comp.add_vacan(5, "5", 40)
print(s_comp.read_proper(5))

s_comp.update_proper(5, {"BIL Director": "Faruh"})
s_comp.add_vacan(5, "3", 29)
print(s_comp.read_proper(5))

s_comp.update_proper(5, {"BIL IT-programmer": "Georgiy"})
s_comp.add_vacan(5, "6", 35)
print(s_comp.read_proper(5))







