1. Arrays And Strings
    - Two Pointers pointing at the start and end of the iterable
    ```
    function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--
    ```

    - Two pointers on two different iterables at the same time eg. Merging two sorted arrays
    ```
    function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i++
            2. j++
            3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    while i < arr1.length:
        Do some logic here depending on the problem
        i++

    while j < arr2.length:
        Do some logic here depending on the problem
        j++
    ```

    - Sliding window till condition is not met
    ```
    funtion fn(arr):
        left = 0
        for right in 0 ... len(arr):
            Add elements at right to the window
            while left < right and condition not met:
                some more logic
                remove elements at left
                increment left
            Update the answer using some logic
    ```
    - Sliding Window with Fixed Window size - Approach 1
    ```
    function fn(arr, k):
        current = some tracking type eg. sum for the window
        ans = store some final processing
        for i in 0 .. k - 1:
            Update current
        update ans
        for i in k .. len(arr):
            Update current: Add arr[i] to window
            Update current: Remove arr[i - k] from window i.e. current
            update ans
        
        return ans
        
    ``` 
    - Sliding Window with Fixed Window size - Approach 2
    ```
    function fn(arr, k):
        current = some tracking type eg. sum for the window
        ans = store some final processing
        for i in 0 .. len(arr):
            current = some tracking type eg. sum for the window
            if i >= k:
                Update current: Remove arr[i - k] from window
                Update current: Add arr[i] to window
                Update ans
            return ans
    ```
    - Prefix Sums
        - Consider         
        ```
                0  1  2  3  4  5
        nums = [5, 2, 1, 6, 3, 8]
        ```
        It's prefix sum
        ```
                       0  1  2  3   4   5
        prefix_sums = [5, 7, 8, 14, 17, 25]
        ```
        - Sub_array sum from index i to j = prefix_sums[j] - prefix_sums[i - 1]
                OR
            (Considering the out-of-bounds case for 0)
          Sub_array sum from index i to j = prefix_sums[j] - prefix_sums[i] + nums[i]
        - Pseudo-code to compute the sub-array sums:
        ```
        prefix = [nums[0]]
        for i in 1 .. len(nums):
            prefix.append(nums[i] + prefix[len(prefix) - 1] )
            
        ```
    - Strings: Split to list for efficient string operations such as appending a new character
    ```
    def build_string(s):
        arr = []
        arr = s.split()
        for c in s:
            arr.append(c)

        return "".join(arr)
    ```
    - Sub-array or substrings:  
        - subarray or substring is a contiguous section of an array or string.
        - Sliding Window 
            - If a problem has explicit constraints such as:
                - Sum greater than or less than k
                - Limits on what is contained, such as the maximum of k unique elements or no duplicates allowed
            - And Asks for
                - Minimum or maximum length
                - Number of subarrays/substrings
                - Total number of sub-arrays
        - The size of a subarray between i and j (inclusive) is j - i + 1. The number of subarrays ending at j is also this number
    - Subsequences:
        - A subsequence is a portion of an array/string that keeps the same order but doesn't need to be contiguous. For example, subsequences of [1, 2, 3, 4] include: [1, 3], [4], [], [2, 3]
        - Mostly applies dynamic programming
    - Subsets:
        - A subset is any group of elements from the original array or string. The order doesn't matter and neither do the elements being beside each other. For example, given [1, 2, 3, 4], the subsets will be [1], [2, 1] and so on.
        - What is the difference between subsequences and subsets if subsets with the same element
        -  This generally means that we can sort the input at the start, which will open the door to methods like two-pointers, greedy algorithms, or even a creative sliding window.
        -  if a problem involves subsequences, but the order of the subsequence doesn't actually matter (let's say it wants the sum of subsequences), then you can treat it the same as a subset, and once again sorting is a powerful tool.

2. Hashing:
    - A hash function is a function that takes any input and deterministically converts it to an integer that is less than a fixed size set by the programme. Inputs are keys and the same key when hashed will give rise to the same value.
    - Example Hash function
        - Convert a to z into its ASCII values
        - Multiply it by their position in the alphabet
        - Add this for each character in the string
        - MOD by 26
        - % is the modulo operation, and makes sure the final converted value will always be less than x, where x is the limit we set.
    -  Because hash functions can convert any input into an integer, if we combine an array with a hash function, we can create what is known as a hash map. This gives O(1) random access to the elements of the array without going through the constraints of an array to refer to elements using just indices
    - With hash maps, we map keys to values, and a key can be almost anything.
    - Only constraint on a hash map's key is that it has to be immutable
    - Hashmap reduces the time complexity of an algorithm by a factor of O(n) for a huge amount of problems
    - A hash map is an unordered data structure (An ordered data structure is one where the insertion order is "remembered") that stores key-value pairs. A hash map can add and remove elements in O(1), as well as update values associated with a key and check if a key exists, also in O(1).
    - Disadvantages:
        - For smaller input sizes, they can be slower because of overhead.
        - O(1) time complexity can be deceiving at times.  Every key needs to go through the hash function, and there can also be collisions.some keys can be very expensive to hash. For example, it may take O(m) time to hash a string, where m is the length of the string. If you want to store a huge string as a key, then the time complexity can be deceiving
        - Hash tables can also take up more space. Resizing a hash table is much more expensive because every existing key needs to be re-hashed. A hash table may use an array that is significantly larger than the number of elements stored, resulting in a huge waste of space. When you don't know how many elements you want to store, a dynamic array is much more convinient because it can be efficiently resized
    - Collisions
        - When different keys hash to the same integer, it is called a collision.
        - To fix collisions, one technique is called chaining. We store linked lists inside the hash map's array instead of the elements themselves. The linked list nodes store both the key and the value
        - When trying to access one of these key-value pairs, we traverse through the linked list until the key matches
        - Handling collisions takes time, slowing down the overall speed and efficiency of the hash map.The most important thing is that the size of your hash table's array and modulus is a prime number to handle collisions viz. 10,007, 1,000,003.
    - Hash Sets:
        - The set uses the same hash function to map keys to integers just as Hashtables
        - The difference between a set and hash table is that sets do not map their keys to anything.
        - Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in O(1)
    - Template 1: HashSet Containment Check
    - Template 2: HashMap Sliding Window to track many items / HashMap count the frequency of things
    - Template 3: HashMap for counting prefix sums to use to count sub-arrays with sum equal to k.
    - Template 4: Array used as HashMap for simple counting sort.

3. Linked Lists
    - Template 1 - Fast & Slow Pointers
    ```
    function fn(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    ```
4. Stacks and Queues:
    - Template 1 - String operations that compare the top of stack with the current character in the string iteration. 
    - Template 2 - Monotonic Stack/Queue: Monotonic stacks and queues are useful in problems that, for each element, involves finding the "next" element based on some criteria, for example, the next greater element. They're also good when you have a dynamic window of elements and you want to maintain knowledge of the maximum or minimum element as the window changes.
    ```
    Given an integer monotonic array nums
    stack = []
    for num in nums:
        while stack and stack[-1] >= num:
            stack.pop()
        stack.push(num)
    ```

