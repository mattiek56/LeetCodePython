
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        i = 0
        while employees[i].id != id:   
            i += 1

        employee = employees[i]
     


        score = employee.importance
     
        if employee.subordinates == []:
            return score
        else: 
            for j in employee.subordinates:
                score += self.getImportance(employees, j)
        return score 

        
#Tester
# a = Employee(1, 5, [2, 3])
# b = Employee(2, 3, [])
# c = Employee(3, 3, [])
# employees_list = (a,b,c)
# obj = Solution()
# print(obj.getImportance(employees_list, 1))


