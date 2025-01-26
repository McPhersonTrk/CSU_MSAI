# Content Recommendation System using a Hash Table
# CRS = content_recommendation_system
import csv  # Import the CSV module to read and write CSV files.

# Initialize the class for the Content Recommendation System
class CRS:
    def __init__(self, capacity=1000):
        #Initialize the Content Recommendation System with a specified hash table capacity.
        #:param capacity: Size of the hash table (default is 1000).
        self.capacity = capacity  # The total size of the hash table.
        self.table = [None] * self.capacity  # Initialize the hash table as a list of None values.

    # Define a hash function that generates a hash index for a given key
    def _hash_function(self, key):        
        # Generate a hash index for the given key using Python's built-in hash function.
        # :param key: The key (user ID) to hash.
        # :return: An integer index within the hash table's bounds.
        try:
            return hash(key) % self.capacity  # Compute the hash value modulo table capacity.
        except Exception as e:
            raise ValueError(f"Error computing hash for key {key}: {e}")  # Raise an error if hashing fails.

    # Add content to the table, associating it with a user ID
    def content_add(self, user_id, content_id):
        # Add content to the hash table, associating it with a specific user ID.
        # :param user_id: The ID of the user (e.g., Instagram name).
        # :param content_id: The ID of the content (e.g., category or recommendation).
        # Ensure both user_id and content_id are strings for compatibility.
        if not isinstance(user_id, str) or not isinstance(content_id, str):
            raise TypeError("user_id and content_id must be strings.")

        # Compute the hash index for the user ID.
        index = self._hash_function(user_id)
        
        # Initialize the bucket (dictionary) at this index if it is empty.
        if not self.table[index]:
            self.table[index] = {}

        # Check if the user ID exists in the bucket; if not, initialize a list for their content.
        if user_id not in self.table[index]:
            self.table[index][user_id] = []
        
        # Add the content ID to the user's list of recommendations, avoiding duplicates.
        if content_id not in self.table[index][user_id]:
            self.table[index][user_id].append(content_id)

    # Retrieve recommendations for a specific user ID
    def get_recommendations(self, user_id):
        # Retrieve content recommendations for a specific user ID.
        # :param user_id: The ID of the user to retrieve recommendations for.
        # :return: A list of content IDs associated with the user.
        # Ensure the user_id is a string.
        if not isinstance(user_id, str):
            raise TypeError("user_id must be a string.")

        # Compute the hash index for the user ID.
        index = self._hash_function(user_id)
        
        # Check if the bucket or user ID is missing in the hash table.
        if self.table[index] is None or user_id not in self.table[index]:
            return []  # Return an empty list if no recommendations are found.

        return self.table[index][user_id]  # Return the list of recommendations.

    # Retrieve all user recommendations
    def get_all_recommendations(self):        
        # Retrieve all recommendations for all users stored in the hash table.
        # :return: A dictionary mapping user IDs to their lists of recommendations.        
        all_recommendations = {}  # Initialize an empty dictionary to store recommendations.
        # Iterate through each bucket in the hash table.
        for bucket in self.table:
            if bucket:  # Skip empty buckets.
                for user_id, recommendations in bucket.items():
                    all_recommendations[user_id] = recommendations  # Add user and recommendations to the dictionary.
        return all_recommendations

    # Retrieve summary statistics of the hash table
    def get_summary(self):
        # Compute summary statistics for the hash table.
        # :return: A tuple containing the number of non-empty buckets and the total number of users stored.
        non_empty_buckets = sum(1 for bucket in self.table if bucket)  # Count non-empty buckets.
        total_users = sum(len(bucket) for bucket in self.table if bucket)  # Count all users in non-empty buckets.
        return non_empty_buckets, total_users


# Load CSV data into the CRS system and process all records
if __name__ == "__main__":
    data_path = r"C:\Users\mikea\Desktop\CSU-MSAI\CSU_MSAI_GitHub\CSC506 Design and Analysis of Algorthims\Mod 5\social media influencers - instagram sep-2022.csv"
    system = CRS(capacity=1024)  # Initialize the CRS system with a hash table of size 1024.

    try:
        # Initialize counters for records processed and skipped.
        total_records = 0
        skipped_records = 0

        # Load CSV data
        with open(data_path, mode='r', encoding='utf-8') as file:
            csvFile = csv.reader(file)  # Open the CSV file for reading.
            next(csvFile)  # Skip the header row.

            for lines in csvFile:
                # Extract the "Instagram name" as the user ID.
                user_id = lines[1].strip()  # Strip whitespace from the Instagram name.
                
                # Combine Category_1 and Category_2 as the content ID.
                content_id = ",".join(filter(None, [lines[7].strip(), lines[8].strip()]))
                
                # Skip rows where content ID is empty.
                if not content_id:
                    skipped_records += 1
                    continue
                
                # Add the user and their associated content to the CRS system.
                system.content_add(user_id, content_id)
                total_records += 1

        # Get summary statistics of the hash table.
        non_empty_buckets, total_users = system.get_summary()
        print(f"Total records processed: {total_records}")
        print(f"Records skipped due to missing categories: {skipped_records}")
        print(f"Non-empty buckets in the hash table: {non_empty_buckets}")
        print(f"Total user-content associations stored: {total_users}")

        # Retrieve and save recommendations for all users.
        all_recommendations = system.get_all_recommendations()
        output_file = r"CSC506 Design and Analysis of Algorthims\Mod 5\user_recommendations.csv"  
        with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
            writer = csv.writer(out_file)  # Open the output file for writing.
            writer.writerow(["User ID", "Recommendations"])  # Write the header row.
            for user_id, recommendations in all_recommendations.items():
                writer.writerow([user_id, "; ".join(recommendations)])  # Write each user and their recommendations.

        print(f"All user recommendations have been saved to {output_file}")

    except Exception as e:
        # Catch and display any errors that occur during execution.
        print(f"An error occurred: {e}")
