# 多行字符串
s='''2
  0.0921787   0.0896389   0.0821939   0.0765463   0.0701444    0.091055    0.133166    0.186218    0.153501   0.0647567   0.0192885  -0.0238278 -0.00282181    0.123261     0.14121    0.166935   0.0602784   0.0459804   0.0532976     0.42656     0.42656
   0.493087     0.47105      0.4221    0.361013    0.322395    0.373903    0.368174    0.432629    0.487236    0.373774    0.369428    0.437144    0.499124    0.491666    0.604207     0.70461    0.494546    0.610246    0.707122    0.763715    0.763715
          1           1           1           1           1           1           1           1           1           1           1           1           1           1           1           1           1           1           1           0           0
0.546845 0.546278 0.544383 0.543404 0.545967 0.553259 0.583735 0.622878 0.619292 0.534033 0.501729 0.452733 0.476608  0.56995 0.594633 0.560007 0.523414 0.516753  0.51482 0.571452 0.511123
0.532429 0.512589 0.458956  0.40359 0.365978 0.412904  0.41131 0.472732 0.502305 0.415257 0.419358 0.477759 0.530108 0.531395 0.614344 0.683178 0.533478  0.62122 0.702946 0.718088  0.73364
       1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1        1
2'''

# 字符串拆分成行
lines=s.split('\n') # 字符串->字符串列表
# 打印列表元素个数
print(len(lines))
print(lines)

# 取出第2个元素，也是一个字符串
line=lines[1]
print(line)

# 移除字符串两边的空格
line=line.strip()
print(line)

# 按空格将字符串分割成列表
line=line.split() #如果不传入参数，就会默认按照空白的字符分割，如space、tab、换行，——》
print(line)

# 把列表元素转换成数字, 也就是字符串列表-> 数字列表

numbers=[float(x) for x in line] #

print(numbers)

