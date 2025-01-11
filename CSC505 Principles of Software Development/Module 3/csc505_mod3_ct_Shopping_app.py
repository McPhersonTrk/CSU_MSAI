class ShoppingApp:
    # Base class for the ShoppingApp. This provides the common structure for all screens in the app.
    # Each screen in the application will inherit from this base class.
    def __init__(self, name):
        # Initializes the base class with the name of the screen.
        # Parameter:
        # - name (str): The name of the screen.
        self.name = name

class DashboardScreen(ShoppingApp):
    # Class representing the Dashboard screen, providing an overview of app features and navigation options.
    def __init__(self, name):
        super().__init__(name)
        # Widgets available on the dashboard screen, acting as shortcuts to various app features.
        self.widgets = ["Shopping List", "To-Do List", "Rewards", "Profile"]

    def display_widgets(self):
        # Method to display the widgets available on the dashboard.
        # Returns a list of widgets available for navigation.
        return self.widgets

class HomeScreen(ShoppingApp):
    # Class representing the Home screen, allowing users to create shopping or to-do lists.
    def __init__(self, name):
        super().__init__(name)
        # Step-by-step instructions for creating lists, guiding the user through the process.
        self.steps = [
            "Create a List",  # Step to start a new list.
            "Click on Store Logo",  # Step to associate a list with a specific store.
            "Go Shopping",  # Step to begin the shopping process.
            "Check out and Pay",  # Step to finalize purchases.
            "Scan Receipt",  # Step to log purchases for rewards.
            "Earn Rewards",  # Step to collect points or benefits.
            "Share with Friends"  # Optional step to gain additional rewards by sharing.
        ]

    def display_steps(self):
        # Method to display the step-by-step instructions for list creation.
        # Returns a list of instructional steps.
        return self.steps

class ShoppingListScreen(ShoppingApp):
    # Class representing the Shopping List screen, allowing users to track shopping items.
    def __init__(self, name):
        super().__init__(name)
        # List to store shopping items along with their quantity and price details.
        self.items = []

    def add_item(self, item, quantity, price):
        # Method to add a shopping item along with its quantity and price.
        # Parameters:
        # - item (str): The name of the shopping item.
        # - quantity (int): The number of items to purchase.
        # - price (float): The price per unit of the item.
        self.items.append({"item": item, "quantity": quantity, "price": price})

class ToDoListScreen(ShoppingApp):
    # Class representing the To-Do List screen, where users can manage their tasks.
    def __init__(self, name):
        super().__init__(name)
        # List to store tasks along with their location and scheduled time details.
        self.tasks = []

    def add_task(self, task, location, datetime):
        # Method to add a task along with its location and datetime.
        # Parameters:
        # - task (str): Description of the task.
        # - location (str): Location associated with the task.
        # - datetime (str): Scheduled date and time for the task.
        self.tasks.append({"task": task, "location": location, "datetime": datetime})

class RewardsScreen(ShoppingApp):
    # Class representing the Rewards screen, where users can access different reward options.
    def __init__(self, name):
        super().__init__(name)
        # List of features available on the Rewards screen, such as gift cards and cashback offers.
        self.features = ["Digital Sticker Album", "Gift Cards", "Fuel Savings", "Coupons", "Cash Back"]

    def display_features(self):
        # Method to display the list of features available on the Rewards screen.
        # Returns a list of reward options.
        return self.features

class FAQScreen(ShoppingApp):
    # Class representing the FAQ screen, providing help and support for the app.
    def __init__(self, name):
        super().__init__(name)
        # Frequently asked questions and their answers, offering guidance on common issues.
        self.faqs = {
            "How to create a list?": "Follow the instructions on the Home screen.",
            "How to earn rewards?": "Scan your receipt and share with friends.",
            "How to update profile?": "Navigate to the Profile screen."
        }

    def display_faqs(self):
        # Method to display the frequently asked questions.
        # Returns a dictionary of FAQs and their answers.
        return self.faqs

class ProfileScreen(ShoppingApp):
    # Class representing the Profile screen, where users can manage their account information.
    def __init__(self, name):
        super().__init__(name)
        # Dictionary to store user information, including name, contact details, and linked accounts.
        self.user_info = {
            "Name": "",  # User's full name.
            "Contact Info": "",  # User's email or phone number.
            "SaaS Tier": "",  # Subscription tier of the user.
            "Social Media Accounts": []  # List of linked social media accounts.
        }

    def update_info(self, key, value):
        # Method to update user information fields.
        # Parameters:
        # - key (str): The field to update (e.g., "Name").
        # - value (str): The new value for the field.
        if key in self.user_info:
            self.user_info[key] = value

class SettingsScreen(ShoppingApp):
    # Class representing the Settings screen, where users can customize their preferences.
    def __init__(self, name):
        super().__init__(name)
        # List of settings options available for customization.
        self.settings_options = ["Notifications", "Privacy", "Theme", "Language", "Account"]
        # Dictionary to track the toggle status of each setting, initialized to False.
        self.toggles = {option: False for option in self.settings_options}

    def toggle_setting(self, option):
        # Method to toggle a setting on or off.
        # Parameter:
        # - option (str): The setting to toggle.
        if option in self.toggles:
            self.toggles[option] = not self.toggles[option]

# Creating an instance of the Dashboard screen and displaying available widgets.
dashboard_screen = DashboardScreen("Dashboard")

# Call function to display application screens and their details
def display_application_screens():
    # Define the list of screens with names and descriptions.
    screens = [
        {"name": "Dashboard", "description": "Provides an overview of app features and navigation."},
        {"name": "Home", "description": "Allows users to create shopping or to-do lists."},
        {"name": "Shopping List", "description": "Enables users to track shopping items with quantity and price."},
        {"name": "To-Do List", "description": "Helps users manage tasks with location and schedule."},
        {"name": "Rewards", "description": "Displays reward options such as cashback and gift cards."},
        {"name": "FAQ", "description": "Provides help and answers to frequently asked questions."},
        {"name": "Profile", "description": "Allows users to manage account information and preferences."},
        {"name": "Settings", "description": "Lets users customize application preferences and notifications."}
    ]

    # Display a header for the list of application screens.
    print('Shopping List Application Screens:')
    print('---------------------------------')
    print('The following screens are available in the application:')

    # Loop through the screens list and display each screen's name and description.
    for i, screen in enumerate(screens, start=1):
        print(f"{i}. {screen['name']}: {screen['description']}")
    print('---------------------------------')

    # Display the total number of screens in the application.
    print(f"\nTotal number of screens in the application: {len(screens)}")
    print('---------------------------------')

    # Display the sequence of the screens in a logical order.
    print('\nScreen Sequence:')
    print('----------------')
    screen_order = [
        'Dashboard --> Home --> Shopping List --> To-Do List --> Rewards --> FAQ --> Profile --> Settings'
    ]
    for order in screen_order:
        print(order)

# Call the function to display application screen details.
display_application_screens()