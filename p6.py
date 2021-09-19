class employee:
	def __init__(self, id, name, salary):
		self.id = id
		self.name = name
		self.salary = salary
	def show(self):
		print("id = ", self.id)
		print("name = ", self.name)
		print("salary = ", self.salary)
	def bonus(self):
		amt = self.salary * 0.10
		print("bouns amt = ", amt)
class aemployee(employee):
	pass
a = aemployee(10, "neha", 1000)
a.show()
a.bonus()

class pemployee(employee):
	def bonus(self):
		amt = self.salary * 0.15
		print("bouns amt = ", amt)
p = pemployee(102, "asha", 10000)
p.show()
p.bonus()

class manager(employee):
	def bonus(self):
		amt = self.salary * 0.20
		print("bouns amt = ", amt)
m = manager(19, "anit", 15000)
m.show()
m.bonus()





