
# coding: utf-8

# ## COMP SCI 1MD3 Introduction to Programming, Winter 2019
# ### Ming Ming Tan (Instructor), Morteza Alipour Langouri, Jack Buckley, Victor Chen (TAs).
# ### Lab 1 Assigned Monday Jan 14, Due Monday Jan 21, 10.30am
# ### Maximum grade: 16 
# 
# The purpose of this lab is to:
# * Become familiar with Jupyter notebooks
# * Understand how to test your own solutions
# * Practice writing syntactically correct expressions in Python
# 

# #### Question 0 Practice Question 
# 
# The purpose of this example is to help you understand how to correctly test your code and format it for the autograder.
# 
# For this example, you need to write a Python function that computes the sum of two numbers.
# 
# We won't talk about functions yet, but you need to know some basics. The variables in the first line are the ones you are given--in this case, x and y. The variables after the 'return' statement are the ones you need to create. In this example, we want to find the sum of x and y, and call it s. Therefore the code we need to write is just: `s = x + y`.
# 
# It is also important to note that all of the code in the cell is indented. You will need to write your code so that it is in line with the `return` statement vertically (Jupyter should do this automatically, but it's important to understand).

# In[1]:


def add(x, y):  # The variables x and y here are the ones that you are given to work with
    s = x + y
    # Your code here
    
    return s # the variable after the 'return' statement is the one you need to create.


# The two cells below are 'test' cells. When you have written your function above (and run the code cell that it's in), these two cells should evaluate to 'True' when you run them. If not, modify your code cell above, rerun it, and try the tests again.
# 
# When your code is run through the autograder it will be tested in a similar way. However, we will use different test cases, so just because you pass every test case that we provide does not guarantee you will pass every test case that the grader runs.

# In[2]:


add(3, 5) == 8  # This should evaluate to "True" when run


# In[3]:


add(2, 7) == 9 # This is another test cell.


# #### Question 1 Hypotenuse (3 points)
# 
# Given a right triangle. 
# Let $c$ denotes the length of the hypotenuse and $a$ and $b$ denote the lengths of the other two sides. By Pythagorean theorem, we have 
# $$c=\sqrt{(a^2+b^2)} .$$
# Write a function that returns the length of the hypotenuse of a right triangle. The function takes inputs $a$ and $b$ which  represent the length of the other two sides. 
# 
# Hint: The formula makes use of square roots. Consult https://docs.python.org/3/ to find out how to use square roots in Python.

# In[8]:


def hypotenuse(a,b):
    
    c = (a**2 + b**2)**0.5
    return c


# In[5]:


hypotenuse(3,4)==5


# In[6]:


hypotenuse(5,12)==13


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# ### Question 2a: Inches and Feet Conversion (3 points)
# 
# Write a Python function that converts a measurement in $d$ feet and $e$ inches to a measurement in inches. 
# 
# Hint: $12$ inches =  $1$ ft. Hence $10$ ft and $4$ inches is equivalent to $124$ inches. 

# In[9]:


def inches(d,e): 
    a = d * 12 + e
    return a
    


# In[10]:


inches(10,4)==124


# In[11]:


inches(1,4)==16


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# ### Question 2b Inches and Feet Conversion (3 points)
# Write a function that converts any number of inches into $d$ inches and $e$ feet. (Essentially, do the opposite of Question 2b).

# In[12]:


def feetInches(x): # The variable x is what you get to work with inside the function
    
    
    d = x//12
    e = x%12
    return (d,e)
    


# In[13]:


feetInches(4) == (0, 4)


# In[14]:


feetInches(12) == (1, 0)


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# #### Question 3a: Arithmetic Progression  (1 point)
# 
# An arithmetic progression is a sequence of numbers such that the difference between the consecutive terms is constant.
# If the initial term of an arithmetic progression is $a_{1}$ and the common difference of successive members is $d$, then the $n$-th term of the sequence $a_n$ is given by
# $$ a_{n}=a_{1}+(n-1)d.$$
# 
# Write a function that returns the $n$-th term of an arithmetic progression, given the initial term $a$ and the common difference $d$. 

# In[2]:


def arithmetic(a,d,n):
    
    num = a + (n - 1) * d
    return num


# In[19]:


arithmetic(1,1,100)==100


# In[20]:


arithmetic(0,2,100)==198


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# #### Question 3b: Arithmetic Series  (3 points)
# 
# The sum of the elements of a finite arithmetic progression is called an arithmetic series. 
# 
# This sum can be found quickly by taking the number $n$ of terms being added, multiplying by the sum of the first and last number in the progression, and dividing by 2:
# 
# $$ \frac{n(a_1 + a_n)}{2}.$$
# 
# Write a function that returns the sum of an arithmetic series, given the initial term $a$, the common difference $d$ of the arithmetic progression, and the number of terms $n$. 

# In[3]:


def arithmetic_series(a,d,n):
    
    num2 = (n * (a + arithmetic(a,d,n)))/2
    
    return num2
   


# In[4]:


arithmetic_series(1,1,100) == 5050


# In[5]:


arithmetic_series(1,2,100) == 10000


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# #### Question 4: Quadratic Formula (3 points)
# 
# The solutions to an equation of the form $$ ax^2 + bx + c = 0$$ is: $$x_{1}, x_{2} = \frac{-b\pm\sqrt{b^2-4ac}}{2a} $$
# 
# <br> There are two solutions: one for adding, and one for subtracting the radical.
# <br> Write a program that takes a, b, and c as input and solves for $x_1$ and $x_2$.
# <br>You may assume that $ b^2 - 4ac \geq 0$. Let $x_1$ be the solution where you add the term under the square root term, and $x_2$ be the solution where you subtract the square root term.

# In[26]:


def quadratic(a, b, c):
    x1= (-b + (b**2 -4*a*c)**0.5)/(2*a)
    x2= (-b - (b**2 -4*a*c)**0.5)/(2*a)
    return (x1, x2)
    


# In[27]:


quadratic(1, 2, 1) == (-1.0, -1.0)


# In[28]:


quadratic(2, 5, -3) == (0.5, -3.0)


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS


# In[ ]:


# HIDDEN TESTS

