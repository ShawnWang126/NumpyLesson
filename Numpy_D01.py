# -*- coding: utf-8 -*-
"""
Data Science Lesson-1
"""

import numpy as np
print(np.__version__) # Check Numpy Version

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
Start = 0
End = 21
Array = np.arange(Start,End)
print(Array)

#2.呈上題，將以上數列取出偶數。
Array_Even = Array[Start:End:2]
print(Array_Even)

#3.呈1題，將數列取出3的倍數。
Array_Num3 = Array[Start:End:3]
print(Array_Num3)