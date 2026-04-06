# Berhan Demirel
# Fifth optimized attempt with LinkedList collision method, using ASCII and prime numbers and prime capacity kind of improvmenets

import csv
import time

class Node:
    # Initializes a new node to store a key, value, and reference to the next node
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedListHashTable:
    # Initializes the hash table with a specific capacity and tracking stats
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.collisions = 0

    # Calculates a custom hash using string length and character position weight
    def custom_hash(self, key):
        if not key:
            return 0
            
        if not isinstance(key, str):
            key = str(key)
        
        # improvement 1: start hash value as the length of string
        hash_value = len(key)
        prime = 37 # bigger prime number slightly for better spread
        
        # improvement 2: Multiply the character's ASCII value by its position (i + 1)
        for i, char in enumerate(key):
            hash_value = (hash_value * prime + (ord(char) * (i + 1))) % self.capacity # handle edge also
            
        return hash_value

    # Inserts new pair, if collision handle it using linked list chaining
    def insert(self, key, value):
        if not key: 
            return

        index = self.custom_hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            self.collisions += 1
            current = self.table[index]
            
            while current.next:
                self.collisions += 1
                current = current.next
            current.next = new_node

    # Calculates number of empty buckets remaining in table
    def get_wasted_space(self):
        return sum(1 for bucket in self.table if bucket is None)

# Loads data from a CSV file and builds two separate hash tables, tracking time
def load_data_and_build_tables(filename):
    # Dropped the size to save memory and used a prime number
    table_capacity = 20011 
    
    title_table = LinkedListHashTable(table_capacity)
    quote_table = LinkedListHashTable(table_capacity)

    start_time_titles = time.time()
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title_table.insert(row['movie_title'], row)
    end_time_titles = time.time()

    start_time_quotes = time.time()
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quote_table.insert(row['quote'], row)
    end_time_quotes = time.time()

    print("Table 1, Movie Title as Key")
    print("Build Time:", round(end_time_titles - start_time_titles, 4), "sec")
    print("Collisions:", title_table.collisions)
    print("Empty Buckets:", title_table.get_wasted_space(), "out of", table_capacity, "\n")

    print("Table 2, Movie Quote as Key")
    print("Build Time:", round(end_time_quotes - start_time_quotes, 4), "sec")
    print("Collisions:", quote_table.collisions)
    print("Empty Buckets:", quote_table.get_wasted_space(), "out of", table_capacity)

if __name__ == "__main__":
    load_data_and_build_tables('MOCK_DATA.csv')