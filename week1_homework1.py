import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # 有兩個實根
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # 有一個實根
        root = -b / (2*a)
        return root, root
    else:
        # 虛數解
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

# 輸入係數
a = float(input("請輸入a的值： "))
b = float(input("請輸入b的值： "))
c = float(input("請輸入c的值： "))

# 解一元二次方程式
solutions = solve_quadratic(a, b, c)

# 輸出解
print("方程式的解為：")
if isinstance(solutions[0], tuple):
    print("解1:", solutions[0][0], "+", solutions[0][1], "i")
    print("解2:", solutions[1][0], "+", solutions[1][1], "i")
else:
    print("解1:", solutions[0])
    print("解2:", solutions[1])
