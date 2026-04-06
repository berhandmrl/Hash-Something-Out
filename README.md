# Hash something out - Final Reflection

## What We Aimed For
For this assignment, the main goal was to implement two separate hash tables (one using movie titles as keys, and one using movie quotes) to store 15,000 fake movie records. The primary focus was learning how to create efficient hash tables that minimize wasted space and minimize collisions through the careful design of hash functions. We tracked construction time, total collisions, and wasted space (empty buckets) to measure our success.

## Performance Chart: Statistics Analysis
Here is the data collected across all 5 optimization attempts for the Title Hash Table. The Quote table followed nearly identical trends.

| Attempt | Collision Method | Hash Function Type | Capacity | Title Collisions | Empty Buckets |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Linked List | Poor (ASCII Sum) | 30,000 | 135,759 | 28,549 |
| **2** | Linked List | Good (Polynomial Rolling) | 30,000 | 3,302 | 18,105 |
| **3** | Linear Probing | Poor (ASCII Sum) | 30,000 | 87,838,870 | 15,000 |
| **4** | Linear Probing | Good (Polynomial Rolling) | 30,000 | 16,618 | 15,000 |
| **5** | Linked List | Custom Positional Tweaks | 20,011 | 10,335 | 11,414 |

## Analysis of the 5 Approaches
The assignment required discussing how well each of the 5 methods worked. 

* **Attempt 1:** This approach failed exactly as expected. The poor ASCII sum function clustered all 15,000 records into just about 1,500 buckets, leaving massive amounts of wasted space.
* **Attempt 2:** By simply switching to a polynomial rolling hash with a prime multiplier, collisions dropped from over 135,000 to just 3,302. This showed that the linked list structure works perfectly when the hash function spreads data evenly.
* **Attempt 3:** This was an absolute disaster. Linear probing combined with a clustering hash function created a cascading traffic jam, taking over 25 seconds to build and resulting in over 87 million collisions.
* **Attempt 4:** Using the good hash function with linear probing fixed the traffic jam. Collisions dropped down to 16,618. Empty buckets were capped at exactly 15,000 because linear probing stores 1 record per bucket.
* **Attempt 5:** For the final optimization, we tweaked the hash to multiply character values by their position and shrunk the table to a prime number capacity (20,011). This saved memory while still keeping collisions extremely low and spreading the data evenly.

## Comparing Performance and Effectiveness
When comparing the performance of the different hash function approaches, it is clear that the collision resolution method (Linked List vs Linear Probing) is entirely dependent on the quality of the hash function.

Linear probing is incredibly fragile. If the hash function is poor (Attempt 3), linear probing becomes borderline unusable due to the exponential growth of collisions. However, linked lists (Attempt 1) can survive a bad hash function; it just turns the hash table into a slow, unoptimized list, but it still functions without taking 25 seconds to compile.

**Most Effective Method:** The most effective method overall was **Attempt 5**. We learned that the easiest way to drop times and save memory is not necessarily to build a massive table, but to use clever math. By shrinking the table from 30,000 to a prime number (20,011), we saved thousands of wasted empty slots. Furthermore, writing a custom hash function that weighed the actual position of the characters ensured that anagrams and similar words were forced into completely different buckets. This proved that a properly sized prime table and a positional hash function offer the best balance of speed, low memory usage, and minimal collisions.
