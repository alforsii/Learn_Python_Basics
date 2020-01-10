

class Students:


    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# Example
class Person:
  pass

# also we can write
class Job:
    work = 'Web-Dev'

job1 = Job()
print(job1.work)

