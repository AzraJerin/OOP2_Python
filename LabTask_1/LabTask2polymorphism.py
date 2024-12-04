class Department:
    def displayName(self):
        return "This is the Department class."

class Teacher(Department):
    def displayName(self):
        return "This is the Teacher class."

class Author(Department):
    def displayName(self):
        return "This is the Author class."

# Demonstrating runtime polymorphism
obj1 = Teacher()
obj2 = Author()

print(obj1.displayName())  # Output: This is the Teacher class.
print(obj2.displayName())  # Output: This is the Author class.


class Teacher(Department):
    def scheduleClass(self):
        return "Scheduling a class."

    def gradeStudent(self):
        return "Grading a student."

    def displayName(self):
        return "Teacher's Name."

class Author(Department):
    def writeArticle(self):
        return "Writing an article."

    def publishBlog(self):
        return "Publishing a blog."

    def displayName(self):
        return "Author's Name."

class TeacherAuthor(Teacher, Author):
    pass  # Inherits all methods from Teacher and Author

# Creating an instance of TeacherAuthor
ta = TeacherAuthor()

# Accessing methods
print(ta.scheduleClass())  # Teacher's method
print(ta.gradeStudent())   # Teacher's method
print(ta.writeArticle())   # Author's method
print(ta.publishBlog())    # Author's method
print(ta.displayName())    # From Teacher (first in inheritance order)

class Teacher(Department):
    def profile(self):
        return "Teacher's profile."

class Author(Department):
    def profile(self):
        return "Author's profile."

class TeacherAuthor(Teacher, Author):
    pass

# Creating an instance
ta = TeacherAuthor()

# Calling profile()
print(ta.profile())  # Output: Teacher's profile (method from Teacher is called)