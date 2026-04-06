# Berhan Demirel
# Third poor function attempt with Linear Probing collision method, using basic ASCII addition

import csv
import time

class LinearProbingHashTable:
    # Initializes the hash table with a specific capacity and tracking stats
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.collisions = 0

    # Calculates hash index by adding ASCII values (poor hash function)
    def poor_hash(self, key):
        if not key:
            return 0
            
        if not isinstance(key, str):
            key = str(key)
        
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.capacity

    # Inserts new pair, if collision handle it using linear probing
    def insert(self, key, value):
        if not key: 
            return

        index = self.poor_hash(key)

        # If the spot is empty, place it right there
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            # If the spot is taken, count a collision and start probing
            self.collisions += 1
            current_index = (index + 1) % self.capacity
            
            # Keep stepping forward until we find an empty slot
            while self.table[current_index] is not None:
                self.collisions += 1
                current_index = (current_index + 1) % self.capacity
                
            self.table[current_index] = (key, value)

    # Calculates number of empty buckets remaining in table
    def get_wasted_space(self):
        return sum(1 for bucket in self.table if bucket is None)

# Loads data from a CSV file and builds two separate hash tables, tracking time
def load_data_and_build_tables(filename):
    table_capacity = 30000 
    
    title_table = LinearProbingHashTable(table_capacity)
    quote_table = LinearProbingHashTable(table_capacity)

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