# 单引号定义法
name = 'UIC'
print(type(name))

# 双引号定义法
name = "UIC"
print(type(name))

# 三引号定义法
name = """UIC"""
print(type(name))

# 字符串内包含双引号
name = '"UIC"'
print(name)

# 字符串内包含单引号
name = "'UIC'"
print(name)

# 使用转义字符\解除引号的引用
name = "\"UIC\""
print(name)

# 字符串的拼接
print("来UIC" + "学费10万")
name = "UIC"
print("我的学校是：" + name) # 拼接只能完成字符串之间的拼接

# 字符串格式化
# 通过占位法，完成拼接
name = "UIC"
message = "全人教育：%s" % name
print(message)
graduate_year = 2023
avg_salary = 20000.58
message = "DS专业, %s%d届毕业生, 毕业平均薪资%.2f" % (name, graduate_year, avg_salary)
print(message)

# 字符串格式化方法2
name = "UIC"
graduate_year = 2023
avg_salary = 20000.58
print(f"DS专业, {name}{graduate_year}届毕业生, 毕业平均薪资{avg_salary}")

# 对表达式进行格式化
print("1 * 1的结果是: %d" % (1 * 1))
print(f"1 * 1的结果是: {1 * 1}")
print("字符串在Python中的类型名是: %s" % type("字符串"))