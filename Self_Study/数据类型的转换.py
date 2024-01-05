# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(13.14)
print(type(float_str), float_str)

# 将字符串转换成数字
num1 = int("11")
print(type(num1), num1)

num2 = float("13.14")
print(type(num2), num2)

# 万物皆可转成字符串，但字符串不一定可以转成数字，字符串中必须要全部都是数字
number = int("UIC") # 此时会报错
print(type(number), number) # 此时会报错

# 整数转浮点数
float_num = float(11)
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(13.14)
print(type(int_num), int_num)