# // python安装环境
# // 快速安装命令
anaconda search -t conda tensorflow 
  
anaconda show jjhelmus/tensorflow

world_alcohol = numpy.genfromtxt("world_alcohol.txt",delimiter=","dtype=str)
print (help(numpy.genfrom.txt))

numpy.array([5,10,15,20] )
# // 构造二位数组
[[5,10][20,25]]

import numpy
numbers = numpy.array([1,2,3,4.0])
print(numbers)
numbers.dtype
# // numpy.array会似的所有的元素类型保持一致

// numpy中数组是按照索引形式的
import numpy 
vector =numpy.array([5,10,15,20])
print(vector[0:3])


# // [ 5 10 15]

matrix = numpy.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix[:,0:2])


# // [[ 5 10]
 # // [20 25]
 # // [35 40]] 此时获取不到2 因此取得值为0，1
 # vector.min(),max()
 print(help(numpy.array))
 import numpy
matrix =numpy.array([[5,10,15],[20,25,30],[35,40,45]])
matrix.sum(axis=0)
# axis=1行
# axis=0列
# numpy常用函数
import numpy as np
print(np.arange(15))
a=np.arange(15).reshape(3,5)
# a
# a.shape行列
# a.ndim维度
# a.dtype.name类型
# a.size大小

np.zeros((3,4))
np.ones(())
np.arange(10,30,5)

from numpy import pi
np.linspace(0,2*pi,100)
 
# array([0.        , 0.06346652, 0.12693304, 0.19039955, 0.25386607,
       # 0.31733259, 0.38079911, 0.44426563, 0.50773215, 0.57119866,
       # 0.63466518, 0.6981317 , 0.76159822, 0.82506474, 0.88853126,
       # 0.95199777, 1.01546429, 1.07893081, 1.14239733, 1.20586385,
       # 1.26933037, 1.33279688, 1.3962634 , 1.45972992, 1.52319644,
       # 1.58666296, 1.65012947, 1.71359599, 1.77706251, 1.84052903,
       # 1.90399555, 1.96746207, 2.03092858, 2.0943951 , 2.15786162,
       # 2.22132814, 2.28479466, 2.34826118, 2.41172769, 2.47519421,
       # 2.53866073, 2.60212725, 2.66559377, 2.72906028, 2.7925268 ,
       # 2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.10985939,
       # 3.17332591, 3.23679243, 3.30025895, 3.36372547, 3.42719199,
       # 3.4906585 , 3.55412502, 3.61759154, 3.68105806, 3.74452458,
       # 3.8079911 , 3.87145761, 3.93492413, 3.99839065, 4.06185717,
       # 4.12532369, 4.1887902 , 4.25225672, 4.31572324, 4.37918976,
       # 4.44265628, 4.5061228 , 4.56958931, 4.63305583, 4.69652235,
       # 4.75998887, 4.82345539, 4.88692191, 4.95038842, 5.01385494,
       # 5.07732146, 5.14078798, 5.2042545 , 5.26772102, 5.33118753,
       # 5.39465405, 5.45812057, 5.52158709, 5.58505361, 5.64852012,
       # 5.71198664, 5.77545316, 5.83891968, 5.9023862 , 5.96585272,
       # 6.02931923, 6.09278575, 6.15625227, 6.21971879, 6.28318531])
# b**2乘方
 # A.dot(B)
 # np.dot(A,B)
 # np.exp(B) e的指数函数
 # a.ravel()拉成向量
 # print(a,T)转置
 
 # np.hstack((a,b))
 # vstack横拼接 纵拼接
 np.hsplit vsplit 
 # 复制的三种格式
 
 print(id(a))
 print(id(b))
 a=b
 # ab完全相等
 c =a.view()
 # ac公用元素值
 a.copy()
 # 仅仅复制
  import numpy as np
data =np.sin(np.arange(20)).reshape(5,4)
print(data)
ind =data.argmax(axis=0)
print(ind)
data_max = data[ind,range(data.shape[1])]
print(data_max)
# np.tile用于扩展
np.argsort(a)
# 默认按照最小值排序
 