# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# Employee

class Employee:
    def __init__(self, name, wage, hours):
        self.employee_name = name
        self.hourly_wage = wage
        self.num_hours_per_week = hours

    def compute_pay(self, number_of_weeks):
        pay_each_week = self.hourly_wage * self.num_hours_per_week
        total_pay = number_of_weeks * pay_each_week
        return total_pay

def total_pay(employees, num_weeks_lst):
    pay_total = 0
    for i in range(len(employees)):
        cur_employee = employees[i]
        cur_num_weeks = num_weeks_lst[i]
        pay_total += cur_employee.compute_pay(cur_num_weeks)
    return pay_total

def main():
    emp_lst = []
    num_weeks_lst = [52.0, 40.0, 45.0]
    emp_jane = Employee('Jane', 29.03, 20.0)
    emp_jack = Employee('Jack', 21.0, 40.0)
    emp_jill = Employee('Jill', 40.5, 10.0)
    emp_lst = [emp_jane, emp_jack, emp_jill]
    total = total_pay(emp_lst, num_weeks_lst)
    print(f"Total Pay: ${total_pay(emp_lst, num_weeks_lst):.2f}")

main()
