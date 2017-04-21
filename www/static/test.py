
#打印九九乘法表
#print('\n'.join([' '.join(['%s*%s=%s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


#画五角星
# import turtle
#
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
# turtle.right(144)
# turtle.forward(100)
#
# turtle.exitonclick()

# #画六角星
# import turtle
#
# turtle.left(30)
# turtle.forward(144)
#
# turtle.right(60)
# turtle.forward(144)
#
# turtle.right(60)
# turtle.forward(144)
#
# turtle.right(60)
# turtle.forward(144)
#
# turtle.right(60)
# turtle.forward(144)
#
# turtle.right(60)
# turtle.forward(144)
#
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.left(60)
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.left(60)
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.left(60)
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.left(60)
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.left(60)
# turtle.forward(144)
# turtle.right(120)
# turtle.forward(144)
#
# turtle.exitonclick()


#二重循环
a=[1]
num=input('请输入数值：')
print (a)
for i in range(int(num) -1):
     a.append(a[-1]+1)
     print (a)
