class Worker():

    employee = 0
    information_worker = []

    def __init__(self, name, job, type_of_work, hours, salary):
        self.name = name
        self.job = job
        self.hours = hours
        self.salary = salary
        self.type_of_work = type_of_work
        Worker.employee += 1
        Worker.information_worker.extend([self.name, self.job, self.type_of_work])

    def informations(self):
        return f'''Employee information: 
                Name: {self.name},
                Job: {self.job},
                Work hour: {self.hours}, 
                Salary: {self.salary}
                '''

boss = Worker('Jan', 'Architect programming', 'Home office', 10, 25000)
mentor = Worker('Aleksandra', 'Mentor', 'In office', 10, 12000)
worker = Worker('Tymek', 'Programer', 'Home office', 8, 3000)

print(boss.informations())
print(mentor.informations())
print(worker.informations())

#print(Worker.information_worker)
#print(Worker.employee)

#print(boss.name, ':', boss.hours, boss.salary)
#print(worker.name, ':', worker.hours, worker.salary)
