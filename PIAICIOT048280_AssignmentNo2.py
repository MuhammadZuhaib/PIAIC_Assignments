{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2],\n",
       "       [ 3,  4],\n",
       "       [ 5,  6],\n",
       "       [ 7,  8],\n",
       "       [ 9, 10],\n",
       "       [11, 12]])"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "# Task no 1\n",
    "def function1():\n",
    "    # create 2d array from 1,12 range \n",
    "    # dimension should be 6row 2 columns  \n",
    "    # and assign this array values in x values in x variable\n",
    "    # Hint: you can use arange and reshape numpy methods  \n",
    "    x =  np.arange(1,13).reshape((6,2)) \n",
    "    return x\n",
    "function1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 2],\n",
       "       [4, 3, 5],\n",
       "       [7, 6, 8]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task4\n",
    "def function4():\n",
    "    #Swap columns 1 and 2 in the array arr.\n",
    "    arr = np.arange(9).reshape(3,3)\n",
    "    arr[:, [0, 1]] = arr[:, [1, 0]]\n",
    "    return arr  #wrtie your code here \n",
    "function4()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0],\n",
       "       [0, 0, 0, 0, 0]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task5\n",
    "def function5():\n",
    "    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function\n",
    "    z = np.zeros([4,5],dtype=int) #wrtie your code here\n",
    "    return z\n",
    "function5()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n",
      "Update 5th & 8th value to 10 and 20\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 0.,  0.,  0.,  0.,  0., 10.,  0.,  0., 20.,  0.])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task6\n",
    "def function6():\n",
    "    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively\n",
    "   \n",
    "    arr = np.zeros(10)#wrtie your code here \n",
    "    print(arr)\n",
    "    print(\"Update 5th & 8th value to 10 and 20\")\n",
    "    arr[5] = 10;  arr[8]=20;\n",
    "    return arr\n",
    "function6()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 0, 0, 0]), 'dtype=int64')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task7\n",
    "import numpy as geek\n",
    "def function7():\n",
    "    #  Create an array of zeros with the same shape and type as X. Dont use reshape method\n",
    "    x = np.arange(4, dtype=np.int64) \n",
    "    x = geek.zeros(4,dtype=np.int64) \n",
    "    return(x ,'dtype=int64')  #write your code here\n",
    "function7()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 6, 6, 6, 6],\n",
       "       [6, 6, 6, 6, 6]], dtype=uint32)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task8\n",
    "def function8():\n",
    "    # Create a new array of 2x5 uints, filled with 6.\n",
    "    x = np.full((2, 5), 6, dtype=np.uint32) #write your code here\n",
    "    return x\n",
    "function8()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([6, 9])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task13\n",
    "def function13():\n",
    "    # Set a condition which gets all items between 5 and 10 from arr.\n",
    "    arr = np.array([2, 6, 1, 9, 10, 3, 27])\n",
    "    ans = [False, True, False, True, False,False,False]  #write your code here \n",
    "    newarr = arr[ans]\n",
    "    return newarr\n",
    "function13()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2]],\n",
       "\n",
       "       [[2, 3]],\n",
       "\n",
       "       [[3, 4]]])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task16\n",
    "def function16():\n",
    "    #Write a NumPy program to join a sequence of arrays along depth.\n",
    "    x = np.array([[1], [2], [3]])\n",
    "    y = np.array([[2], [3], [4]])\n",
    "    ans = np.dstack((x, y))\n",
    "    return ans\n",
    "function16()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#Task20\n",
    "def function20():\n",
    "    #apply fuction \"abc\" on each value of Array \"X\"\n",
    "    x = np.arange(1,11)\n",
    "    def abc(x):\n",
    "        return x*2+3-2\n",
    "    return x*2+3-2 #Write your Code here\n",
    "function20()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-4,  1,  7],\n",
       "       [ 8,  2, -2],\n",
       "       [ 6,  3,  9]])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "#task15\n",
    "def function15():\n",
    "    #Sort following NumPy array by the second column\n",
    "    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])\n",
    "    ans = arr[arr[:,1].argsort()]  #write your code here \n",
    "    return ans\n",
    "function15()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
