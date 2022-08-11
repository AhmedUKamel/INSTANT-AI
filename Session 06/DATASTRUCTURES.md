# Data Structures

> Data structure is a data organization, management, and storage format that enables efficient access and modification. 
> **More precisely**, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.

## Data Structures Main Categories:

### 1.Linear Data Structures:
#### 1.1.Array
`Flexibility:` Static
~~~python
 # Import module
import numpy as np
 # Initialize array
my_array = np.array()
my_array = np.array([E1,E2,E3])
 # Access elements
my_array[index]
my_array.get(index)
~~~

#### 1.2.Set
`Flexibility:` Dynamic
`Technique:` Remove repetition and order
`Types:` Unordered / Multi Set
~~~python
 # Initialize set
my_set = set()
my_set = set([E1,E2,E3])
 # Add elements
my_set.add(element)
 # Delete elements
my_set.remove(element)
 # Update set with another (Merge)(And)
my_set.update(another_set)
~~~

#### 1.3.Map (Dictionary)
`Flexibility:` Dynamic
`Technique:` Keys and Values
`Types:` Unordered / Multi Dictionary
~~~python
 # Initialize dictionary
my_dict = dict()
my_dict = dict(zip([K1,K2,K3],[V1,V2,V3]))
 # Add elements
my_dict[new_key] = new_value
 # Delete elements
my_dict.pop(key)
 # Update elements
my_dict[key  z ] = new_value
~~~

#### 1.4.LinkedList
`Flexibility:` Dynamic
`Direction:` Singly / Doubly Directed
`Circularity:` Circular / Non-circular
~~~python
 # Initialize list
my_list = list()
my_list = [E1,E2,E3]
 # Add elements
my_list.append(element)
my_list.insert(index,element)
 # Delete elements
my_list.pop()
my_list.pop(index)
my_list.remove(element)
 # Update elements
my_list[index] = value
~~~

#### 1.5.Stack
`Flexibility:` Depends on Implementation
`Implementation:` Array / LinkedList
`Technique:` Last-in first-out (LIFO)
~~~python
 # Import module
from queue import LifoQueue
 # Initialize stack
my_stack = LifoQueue()
 # Insert
my_stack.put(element)
 # Retrieve
my_stack.get()
~~~

#### 1.6.Queue
`Flexibility:` Depends on Implementation
`Implementation:` Array / LinkedList
`Technique:` First-in first-out (FIFO)
`Circularity:` Circular / Non-circular
`Priority:` Priority / Priority Less
~~~python
 # Import module
from queue import Queue
 # Initialize queue
my_queue = Queue()
 # Insert (Enqueue)
my_queue.put(element)
 # Retrieve (Dequeue)
my_queue.get()
~~~



### 2.Non-linear Data Structures:
#### 2.1.Graph
`Flexibility:` Dynamic
`Direction:` Directed / Undirected
`Weight:` Weighted / Unweighted
`Traversal:` DFS / BFS
`Storage method:` Adjacency List / Matrix

#### 2.2.Tree
`Flexibility:` Dynamic
`Types:` 
* General-tree
* Binary-tree
* Binary-search-tree
* AVL-tree