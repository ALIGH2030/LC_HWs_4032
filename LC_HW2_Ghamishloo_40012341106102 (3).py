def routh_table(coeffs):
    n = len(coeffs)
    rows = (n + 1) // 2
    table = [[0.0 for _ in range(rows)] for _ in range(n)]

    
    table[0][:len(coeffs[0::2])] = coeffs[0::2]  
    table[1][:len(coeffs[1::2])] = coeffs[1::2]  
    for i in range(2, n):
        for j in range(rows - 1):
            a = table[i - 2][0]
            b = table[i - 2][j + 1]
            c = table[i - 1][0]
            d = table[i - 1][j + 1]
            if c == 0:
                c = 1e-6  
            table[i][j] = ((c * b) - (a * d)) / c

    return table

#ضرایب تابع مشخصه 
#coeffs = [2, 9, 6, 4, 8, 8, 2, 6]
#coeffs = [2, 4, 2, 3, 2, 5]
#coeffs = [1, 1, 12, 22, 39, 59, 48, 38, 20]


table = routh_table(coeffs)

for i, row in enumerate(table):
    print(f"Row {i}: {row}")


#توی ستون اول جدول راثشون تغییر علامت داشتند
#این یعنی حداقل یک یا چند ریشه با قسمت حقیقی مثبت دارن
# بنابراین هر سه سیستم ناپایدار هستند
#سوال3