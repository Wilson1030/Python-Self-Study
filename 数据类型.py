# 方法1：使用print直接输出类型信息
print(type("UIC"))
print(type(666))
print(type(13.14))

# 方法2：使用变量存储type（）语句的结果
str_type = type("UIC")
int_type = type(666)
float_type = type(13.14)
print(str_type)
print(int_type)
print(float_type)

# 方法3：使用type（）语句，查看变量中存储的数据类型信息
name = "UIC"
name_type = type(name)
print(name_type)