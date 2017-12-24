# Q1: Difference between shallow copy and deep copy
  - import copy
  - copy.copy() <--shallow copy
  - copy.deepcopy() <-- deep copy
  
# Q2:Different between list and tuple
  - List is mutable, tuple is immutable(not changeable)
    - list.append, list.remove
    - when columns are fixed(like table's column in db), using tuple; if column not fixed, then use list
    - list is like table, and tuple is like row
  - tuple's element is still mutable
    - t1=([1,2,3],) 
    - t1[0].append(5)

# Q3: How multi-thread is achieved in Python?
  - GIL (Global Interpretor Locker) only allows one thread running at a time
  - multi-thread package
  ```python     
      import threading
         
      def worker():
          """thread worker function"""
          print 'Worker'
         return
          
     threads = []
     for i in range(5):
         t = threading.Thread(target=worker)
         threads.append(t)
         t.start()
 ```

# Q4: Ternary operation in python
  - behave like ternary operation, but not real ternary operation
  ```python
    x, y = 25, 50
    big = x if x > y else y
  ```

# Q5: Monkey patch in Python
- Monkey patch refers to dynamic modifications of class or module in runtime
- Used in quick fix or extending thirdparty package's functions
```python
'''original class definition'''
#m.py
class MyClass:
  def f(self):
    print("f()")
    
```

```python
'''after monkey patch'''
import m
def monkey_f(self):
  print("monkey_f()")
 
 m.Myclass.f = monkey_f
 obj=m.MyClass()
 obj.f #then the function is monkey_f()
```

#  Q6: How can you randomize the items of a list in place?
```python
from random import shuffle
x=['1','2','3','4']
shuffle(x)
print(x) #result is elements in list are randomly ordered
```

# Q7: Write a sorting algoritm for a numerical dataset
```python
list=["1", "10", "4", "2", "5"]
list=[int(i) for i in list] #change item from str to int
list.sort() #sorting
print(list)
```
