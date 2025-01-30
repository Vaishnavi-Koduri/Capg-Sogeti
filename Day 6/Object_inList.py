class Management:
    def display_parent(self):
        print("This is the management")

class School(Management):
    def school(self):
        print("This is a school")

class UG(Management):
    def college(self):
        print("This is UG")

class PG(Management):
    def university(self):
        print("This is PG")

admin= School()
admin1= UG()
admin2= PG()
admin.school()
admin1.college()
admin2.university()
res = [admin, admin1.college(), admin2.university()]
res[0].school()


