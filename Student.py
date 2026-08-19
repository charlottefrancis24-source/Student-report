name = input("What's your name? ")

lessons_completed = int(input("How many lessons have you completed? "))

hours_per_day = float(input("How many hours do you study daily? "))

completed_ten_lessons = lessons_completed >= 10

total_hours = hours_per_day * 7

has_long_name = len(name) >= 5

print("Student Report")
print("Name:", name)
print("Lessons completed:", lessons_completed)
print("Hours studied daily:", hours_per_day)
print("Total weekly hours:", total_hours)
print("Name has 5+ characters:", has_long_name)
print("Completed at least 10 lessons:", completed_ten_lessons)
