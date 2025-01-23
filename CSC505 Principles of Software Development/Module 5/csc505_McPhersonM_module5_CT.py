'''
# Pothole Tracking System.
# Use Python to write a script that will print out the different actors and use cases
# actors: The People, The office staff & Road Crew.
# Preconditions: Internet access (ALL), UI/UX System, (ALL), Computing system (ALL), Ui/UX must have mapping and logging sytem, as welll as a schedule, and and a materials and work database
# Main Flow: 
- Complaintant logs onto the UI/UX, 
- Submits a complaint report, 
- Staff reads the report, assigns crew, materials, anad shedules repairs.
- Crew arrives at work site, makes repairs, updates the UI/UX with status/completion
- Staff updates the UI/UX system/database.
# Alternative Flow:
- If duplicate report is made, merges complaints
- If crew is delayed, can't fiish/fix the hole, it logs a reason and changes status.
# Postconditions:
- Status' are kept  up to database
- People are can access job status and times of work, as well as future work
# Non-functional Requirements
- UI/UX must be compaltible with numerous sysytems, Web/Android/apple
- UI/UX must comply with the law
- expandability, sytem must be able to add in new districts.
- System should be able to handle the digital volume.
- Data security, Ui/UX communication and database  systems must me secure to ensure customer data protection.
'''
# Pothole Tracking System
# Actors: The People, The Office Staff & Road Crew.
# Create a dictionary for actors
actors = {
    'people': "The People",
    'office_staff': "The Office Staff",
    'road_crew': "Road Crew"
}

# Create a dictionary for the use cases
use_cases = {
    'report_pothole': "Report Pothole",
    'add_pothole': "Add Pothole",
    'assign_pothole': "Assign Pothole",
    'assign_crew': "Assign Crew",
    'assign_materials': "Assign Materials",
    'crew_arrives': "Crew Arrives",
    'verify_pothole': "Verify Pothole",
    'fix_pothole': "Crew Fixes Pothole",
    'update_pothole': "Update Pothole Status",
    'pothole_report': "Create Pothole Report",
    'remove_fixed_pothole': "Remove Fixed Pothole from the list",
    'close_pothole': "Close Pothole Report"
}

# Create a dictionary for the pothole work queue
work_queue = []

# Accept user inputs
def people_input():
    name = input("Enter your name: ").strip()
    print(f"Hello {name}, welcome to the Pothole Tracking and Repair System.")
    
    while True:
        report = input("Would you like to report a pothole? (yes/no): ").strip().lower()
        if report == "yes":
            address = input("Enter the address of the pothole: ").strip()
            diameter = input("Enter the diameter of the pothole (in inches): ").strip()
            depth = input("Enter the depth of the pothole (in inches): ").strip()
            comments = input("Enter any additional comments: ").strip()
            
            # Add the pothole data to the work queue
            pothole_data = {
                "address": address,
                "diameter": diameter,
                "depth": depth,
                "comments": comments
            }
            work_queue.append(pothole_data)
            print("Thank you for reporting the pothole. It has been added to the work queue.")
        elif report == "no":
            print("Thank you for visiting the Pothole Tracking and Repair System. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to print actors and use cases
def print_PhTS():
    try:
        print("\nPothole Tracking and Repair System - Actors:")
        for actor, description in actors.items():
            print(f'- {actor}: {description}')
        
        print("\nPothole Tracking and Repair System - Use Cases:")
        for use_case, description in use_cases.items():
            print(f'- {use_case}: {description}')
    except Exception as e:
        print(f"An error occurred while printing system details: {e}")

# Main function
def main():
    try:
        print_PhTS()  # Print actors and use cases
        people_input()  # Ask for user inputs
        print("\nCurrent Work Queue:")
        for idx, pothole in enumerate(work_queue, start=1):
            print(f"{idx}. Address: {pothole['address']}, Diameter: {pothole['diameter']} inches, Depth: {pothole['depth']} inches, Comments: {pothole['comments']}")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Call the main function
if __name__ == "__main__":
    main()