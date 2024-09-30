#The program should let the user enter a course number and then it should display the course's room number, instructor, and meeting time.
# create three dictionaries: 
# one that maps course numbers to room numbers, 
# one that maps course numbers to instructors, 
# and one that maps course numbers to meeting times.

# create a function that gets user input for a course number and then displays the course's room number, instructor, and meeting time.
# If the course number doesn't exist in the dictionaries, the program should display a message saying that the course number doesn't exist.
# The program should continue to prompt the user for input until the user enters a valid

# Main function:
def main():
    # Room number dicytionary
    classroom = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755', 'NET110': '1244', 'COM241': '1411'}
    # Instructor dictionary
    instructor = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}
    # Meeting time dictionary
    start_time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

    while True:
        # get user input
        course_number= input("Enter a course number (e.g., CSC101): ").strip().upper()
        # Print the course details
        if course_number in classroom:
            print(f"Course Number: {course_number}")
            print(f"Instructor: {instructor[course_number]}")
            print(f"Room Number: {classroom[course_number]}")
            print(f"Meeting Time: {start_time[course_number]}")
            break #exit the loop if the course number is valid
        else:
            print("That course number does not exist.")
#call the fuinction
if __name__ == "__main__":
    main()