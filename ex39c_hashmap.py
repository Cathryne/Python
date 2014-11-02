# Exercise 39: Making Your Own Dictionary Module
# http://learnpythonthehardway.org/book/ex39.html

def new(num_buckets=256):
    """Initialises list & iteratively fills its items with one empty list each (="buckets")."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """Modulos length of map against hash of key. Resulting number should be unique, given sufficient length and can therefore be used as index for buckets."""
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Finds bucket/index of given key."""
    bucket_id = hash_key(aMap, key)  # unique index number
    return aMap[bucket_id]  # accesses list at index

def get_slot(aMap, key, default=None):
    """Returns index, key and value from the bucket corresponding to given key. Much faster searching than through entire map for key."""
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):  # enumerate returns address of iterable object
        k, v = kv  # merges key and value to tuple in order to compare it to tuples in map
        if key == k:
            return i, k, v  # i is index of tuple in bucket list, not in map list => always 0 because each bucket list has only 1 tuple.
        # Why no else here with default return values? Moving it from below yields:
        # Traceback (most recent call last):
        #   File "ex39c.py", line 8, in <module>
        #     ex39c_hashmap.set(states, 'Oregon', 'OR')
        #   File "/Users/USER/Python/ex39c_hashmap.py", line 41, in set
        #     i, k, v = get_slot(aMap, key)
        # TypeError: 'NoneType' object is not iterable

    return -1, key, default  # Why can't this be passed from inside else statement?

def get(aMap, key, default=None):
    """Unpacks get_slot() returns & passes along only value."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Writes (key, value)-tuple to corresponding bucket, overwrites if bucket not empty (Should not occur for unique keys & long map.), so that only 1 value exists for given key. This check slows down setting of keys, due to design choice."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes key from corresponding bucket in map."""
    bucket = get_bucket(aMap, key)

    for i in xrange(len(bucket)):  # iterates over tuples in bucket
        k, v = bucket[i]  # retrieve tuple from bucket
        if key == k:  # checks if key exists in bucket
            del bucket[i]  # deletes tuple at bucket index
            break

def list(aMap):
    """Iterates through map & prints out tuples from filled buckets."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v
    # invisible return here
