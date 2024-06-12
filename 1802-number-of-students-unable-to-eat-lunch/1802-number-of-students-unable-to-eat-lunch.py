class Solution:
    def countStudents(self,students:List[int],sandwiches:List[int]):
        stdCount=len(students)
        while sandwiches and students and sandwiches[0] in students:
            if students[0]!=sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
                stdCount-=1
        return stdCount