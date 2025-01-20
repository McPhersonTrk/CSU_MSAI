import logging
from abc import ABC, abstractmethod

# Configure logging for debugging and tracking execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Abstract Builder Interface
class TraitsBuilder(ABC):
    @abstractmethod
    def adaptability_add(self):
        pass
    @abstractmethod
    def collaboration_add(self):
        pass
    @abstractmethod
    def problem_solving_add(self):
        pass
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder Class
class DeveloperTraitsBuilder(TraitsBuilder):
    def __init__(self):
        self.traits = []
    def adaptability_add(self):
        logging.info("Adding adaptability trait.")
        self.traits.append({
            "trait": "Adaptability",
            "description": "Ability to handle changing requirements and environments."})
        return self
    def collaboration_add(self):
        logging.info("Adding collaboration trait.")
        self.traits.append({
            "trait": "Collaboration",
            "description": "Strong teamwork and communication skills."})
        return self
    def problem_solving_add(self):
        logging.info("Adding problem-solving trait.")
        self.traits.append({
            "trait": "Problem-Solving",
            "description": "Analytical thinking and troubleshooting abilities."})
        return self
    def get_result(self):
        logging.info("Fetching all traits.")
        return self.traits

# Director Class to Orchestrate the Building Process
class TraitsDirector:
    def __init__(self, builder: TraitsBuilder):
        self.builder = builder

    def construct_developer_traits(self):
        logging.info("Starting trait construction process.")
        self.builder.adaptability_add().collaboration_add().problem_solving_add()

# Main Execution Program
if __name__ == "__main__":
    # Instantiate the Builder and Director
    logging.info("Instantiating the DeveloperTraitsBuilder.")
    builder = DeveloperTraitsBuilder()
    director = TraitsDirector(builder)

    # Build the traits
    logging.info("Constructing developer traits using the director.")
    director.construct_developer_traits()

    # Fetch and display the traits
    traits = builder.get_result()

    # Prints a detailed description of the program's functionality
    print("\n=== Software Developer Personality Traits ===")
    print("This program demonstrates the Builder Pattern to model three essential personality traits of excellent software developers.")
    print("Important Steps in the Program:")
    print("1. Define an Abstract Builder Interface to establish a contract for the builder methods.")
    print("2. Implement the Concrete Builder Class to provide specific behaviors for the traits.")
    print("3. Use a Director Class to manage the construction process.")
    print("4. Fetch and display the constructed traits with descriptions.\n")

    print("=== Developer Personality Traits ===")
    for i, trait in enumerate(traits, 1):
        print(f"{i}. {trait['trait']} - {trait['description']}")
