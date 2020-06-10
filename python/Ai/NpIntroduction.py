import numpy as np
import torch as tc

# a = np.array([[1, 2], [3, 3], [5, 6]])
# u, s, v = np.linalg.svd(a)
# print(u, s, v, sep="\n")
# for i in range(100):
#     print("ajsdhj")
#     i+=1

# a = np.array([1, 2, 3])
# b = tc.tensor([1, 2, 3])
# c = [1, 2, 3]
# print(type(a))  # 查看类型
# print(a.dtype)  # 查看类型里面的数据类型
# print(a.shape)  # 查看类型形状

# print("生成数组")
# data = [[1, 2, 3],[4,5,6]]
# a = np.array(data)
# print(type(a),a.shape,a.dtype,sep="\n")
# print(a.ndim)#查看维度

# x = np.zeros((2,3),dtype=np.int8)#生成0矩阵，数据类型为整数
# b = np.ones((2,3),dtype=np.int8)#生成1矩阵，数据类型为整数
# y = np.empty((2,3))#按照随机数生成未被初始化的矩阵,如果加dtype=np.int8，则是0矩阵
# print(x,b,y,sep="\n")


# print("使用arrange()生成连续数组")
# a = np.arange(30)
# a = a.reshape(3,10)
# print(a)
#
#
# print("使用astype()复制数组，并且改变类型")
# x = np.array([1,2,3,45,6,6],dtype=np.float64)
# y = x.astype(np.int8)


# print("把字符串转为数字")
# x = np.array(["1","2","3","45","6","6"])
# x = x.astype(np.int8)


# print("使用其他数组的元素的数据类型作为参数")
# x = np.array([1,2,3,45,6,6],dtype=np.float64)
# xy = np.array([1,2,3,45,6,6],dtype=np.int8)
# xy = xy.astype(x.dtype)
# print(xy.dtype,type(xy),xy,sep="\n")


# print("ndarray的运算")
# x = np.array([1,2,3],dtype=np.float64)
# y = np.array([2,2,3],dtype=np.float64)
# print(x*3)
# print(x>6)
# print(x*y)


# print("ndarray的索引,请注意，会降维")
# x = np.array([[1,2],[3,4],[5,6]])
# print(x[-1,0]) #等于([-1][0])

# a =  np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a[0])
# print(a[0,1])
# print(a[0,1,0])

# b = a.copy()#复制一个副本，
# b = a[0].copy()#复制一个特定副本，
# b[0,0,0] = 3
# print(b,a,sep="\n")


# print("ndarray的切片,不会降维")
# x = np.array([1,2,3,45,6,6],dtype=np.float64)
# print(x[1:3])
# print(x[:3])
# print(x[2:])

# y = np.array([[1,2],[3,4],[5,6]])
# print(y[:2])
# print(y[:2,:1])
# y[:2,1:2] = [[7],[7]]#切出来之后要形状一致次才能赋值
# print(y)
# y[1:2] = [2,2]
# print(y)


# print("ndarray的布尔索引")
# x = np.array([1,2,3,45,6,6],dtype=np.float64)
# y = np.array([True,False,True,True,False,True])
# print(x[y])#个数要匹配
# print(x[y==False])#取flase的索引的值
# print(x[~(x>3)])#取相反的



# print("ndarray的数组索引")
# x = np.array([1,2,3,45,6,6],dtype=np.float64)
# print(x[[0,1,2]])
# print(x[[-1,-2]])

# y = np.array([[1,2],[3,4],[5,6]])
# print(y[[0,1]])
# print(y[[0,1],[0,1]])
# print(y[[0,1]][:1,[0,1]])


# print("ndarray的轴")
# x = np.arange(8).reshape((2,4))
# print(x)
# print(x.T) #转置

# print(np.dot(x,x.T)) #乘法

# k = np.arange(24).reshape(2,3,4)
# print(k)
# print(k[0][1][0])

# k = k.transpose((1,0,2))#换轴
# print(k)

# k = k.swapaxes(0,2)#换轴（但是只交换2个）
# print(k.shape)



# print("numpy的基本统计")
# y = np.array([[1,2],[3,4],[5,6]])
# print(y.shape)

# print(y.mean())#所有数的平均值
# print(y.mean(axis=1)) #每一行
# print(y.mean(axis=0)) #每一列

# print(y.sum())#所有数的总和
# print(y.sum(axis=1))

# print(y.max())#所有数的最大值
# print(y.max(axis=1))#每一组数的最大值


# print("where函数")
# x = np.array([1,2,3,4,5,6])
# x = np.where(x>2,3,6)#满足条件取3，否则取6
# print(x)



# print("ndarray的存取")
# x = np.array([[1,2,6],[3,4,5],[5,6,7]])
# np.save("file",x)#二进制形式存储，npy格式
# t = np.load("file.npy")
# print(t)


# print("矩阵求逆")
# x = np.array([[1,1],[1,2]])
# y = np.linalg.inv(x)
# print(y)


# print("numpy的随机数")
# x = np.random.randint(0,2,100) #随机整数
# print((x>0).sum())#统计正面的次数



