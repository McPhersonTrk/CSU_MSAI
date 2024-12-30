import xml.etree.ElementTree as ET

# Ceate a class McPherson_uml that has a method communication that takes in user input for the following:
# Initial Project Details
# Requirements
# Design
# Implementation
# Testing
# Deployment
# The method should store the user input in a dictionary with the keys being the names of the input and the values being the user input.
# The method should print "This is a communication diagram" and then print the dictionary with the user input.
class McPherson_uml:
    # Constructor to initialize the class and an empty dictionary to store project data.
    def __init__(self):
        self.data = {}
    # Communication method to collect user inputs for the initial stage of the project.
    # Inputs include Initial Project Details, Requirements, Design, Implementation, Testing, and Deployment.
    def communication(self):
        print('\n ********** Communication **********')
        print("This is a communication diagram")
        # Store user inputs in the dictionary under the 'communication' key.
        self.data['communication'] = {
            "new_project": input('Enter Initial Project Details: '),
            'requirements': input('Enter Requirements: '),
            'design': input('Enter Design: '),
            'implementation': input('Enter Implementation: '),
            'testing': input('Enter Testing: '),
            'deployment': input('Enter Deployment: ')
            }
    # Plan method to collect user inputs for the planning stage of the project.
    # This method collects similar inputs as the communication method and stores them under the 'plan' key.    
    def plan(self):
        print( '\n ********** Plan **********')
        print(self.data) # Print current data for context.
        self.data['plan'] = {
            'plan': input('Enter Plan: '),
            'requirements': input('Enter Requirements: '),
            'design': input('Enter Design: '),
            'implementation': input('Enter Implementation: '),
            'testing': input('Enter Testing: '),
            'deployment': input('Enter Deployment: ')
            }
    # Model method to collect user inputs for the modeling stage of the project.
    # Inputs are stored under the 'model' key in the dictionary.
    def model(self):
        print( '\n ********** Model **********')
        print(self.data) # Print current data for context.
        self.data['model'] = {
            'model': input('Enter Model: '),
            'requirements': input('Enter Requirements: '),
            'design': input('Enter Design: '),
            'implementation': input('Enter Implementation: '),
            'testing': input('Enter Testing: '),
            'deployment': input('Enter Deployment: ')
            }
    # Construction method to collect user inputs for the construction stage of the project.
    # Inputs are stored under the 'construction' key in the dictionary.    
    def construction(self):
        print( '\n ********** Construction **********')
        print(self.data) # Print current data for context.
        self.data['construction'] = {
            'construction': input('Enter Construction: '),
            'requirements': input('Enter Requirements: '),
            'design': input('Enter Design: '),
            'implementation': input('Enter Implementation: '),
            'testing': input('Enter Testing: '),
            'deployment': input('Enter Deployment: ')
            }
    # Feedback method to collect user inputs for the feedback stage of the project.
    # Inputs are stored under the 'feedback' key in the dictionary    
    def feedback(self):
        print( '\n ********** Feedback **********')
        print(self.data) # Print current data for context.
        self.data['feedback'] = {
                'feedback': input('Enter Feedback: '),
                'requirements': input('Enter Requirements: '),
                'design': input('Enter Design: '),
                'implementation': input('Enter Implementation: '),
                'testing': input('Enter Testing: '),
                'deployment': input('Enter Deployment: ')
                }
    # Deployment method to collect user inputs for the deployment stage of the project.
    # Inputs are stored under the 'deployment' key in the dictionary.
    def deployment(self):
        print( '\n ********** Deployment **********')
        print(self.data) # Print current data for context.
        self.data['deployment'] = {
                'deployment': input('Enter Deployment: '),
                'requirements': input('Enter Requirements: '),
                'design': input('Enter Design: '),
                'implementation': input('Enter Implementation: '),
                'testing': input('Enter Testing: '),
                'deployment': input('Enter Deployment: ')
                }
    def save_as_uxf(self, filename='csc505_McPhersonsM_mod2.uxf'):
    # Create the root element
        root = ET.Element('diagram')

    # Iterate through stages and add UMLNote elements for each stage
        for index, (stage, details) in enumerate(self.data.items()):
            element = ET.SubElement(root, 'element')
            ET.SubElement(element, 'type').text = 'UMLNote'
            # Adjust coordinates to ensure proper layout
            ET.SubElement(element, 'coordinates').text = f"{50}, {index * 150 + 50}, 200, 100"
            # Add the stage name and details to panel_attributes
            ET.SubElement(element, 'panel_attributes').text = f"{stage.upper()}\\n" + "\\n".join(
                f"{key}: {value}" for key, value in details.items()
                )
            ET.SubElement(element, 'additional_attributes')

    # Add arrows (Relation elements) to connect the stages
        for index in range(len(self.data) - 1):
            arrow = ET.SubElement(root, 'element')
            ET.SubElement(arrow, 'type').text = 'Relation'
            # Adjust coordinates for arrow positions
            ET.SubElement(arrow, 'coordinates').text = f"{150}, {index * 150 + 100}, {150}, {index * 150 + 200}"
            ET.SubElement(arrow, 'panel_attributes').text = '-->'
            ET.SubElement(arrow, 'additional_attributes')

        # Save the XML tree to a .uxf file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"File {filename} saved successfully.")
    
    # Run method to execute all stages sequentially.
    # This method calls each stage method in order and stores the collected data.    
    def run(self):
            self.communication()
            self.plan()
            self.model()
            self.construction()
            self.feedback()
            self.deployment()
            print(self.data) # Print all collected data at the end.
            # Print output method to display the collected data in a formatted manner.
    def print_output(self):
            print('\n ********** Output **********')
            print(self.data)  # Print raw data dictionary.
            for stage, details in self.data.items():
                print(f'{stage}: {details}') # Print each stage and its details.
                for key, value in details.items():
                    # Print each key-value pair in a formatted manner.
                    print(f'{key.capitalize()}: {value}')
# Main function to create an instance of the class and execute the run and print_output methods.
if __name__ == '__main__':
    model = McPherson_uml()
    model.run()
    model.print_output()
    model.save_as_uxf()