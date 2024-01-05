"""
命名规则：
1.内容限定：
  只允许出现：
    英文
    中文（不推荐）
    数字（不允许出现在开头）
    下划线
2.大小写敏感
  能够区分大小写
3.不可使用关键字
  以下关键字在Python中有特定的用途, 不可以使用作为标识符
    1.False  2.True  3.None  4.and  5.as  6.assert  7.break  8.class 
    9.continue  10.def  11.del  12.elif  13.else  14.except  15.finally  16.for 
    17.from  18.global  19.if  20.import  21.in  22.is  23.lambda  24.nonlocal 
    25.not  26.or  27.pass  28.raise  29.return  30.try  31.while  32.with  33.yield
"""

# 规则1：内容限定，限定只能使用：中文，英文，数字，下划线，注意：不能以数字开头
# 1_name = "张三"，运行会报错
# name_! = "张三"，运行会报错
name_ = "张三"
_name = "张三"
name_1 = "张三"

# 规则2：大小写敏感
UIC = "北师港浸大"
Uic = "北师香港浸会大学"
print(UIC)
print(Uic)

# 规则3：不能使用关键字
# class = 1 运行会报错
# def = 1 运行会报错
Class = 1 # 不会报错
Def = 1 # 不会报错
