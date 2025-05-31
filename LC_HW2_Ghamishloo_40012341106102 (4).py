import control
import matplotlib.pyplot as plt

#تابع تبدیل 1 
num1 = [1, 3, 2]
den1 = [1, 1, 1, -3]
#تابع تبدیل 2
num2 = [1, 1, 0] 
den2 = [1, 7, 6, -82, 68]


sys1 = control.TransferFunction(num1, den1)
sys2 = control.TransferFunction(num2, den2)
control.root_locus(sys1)
plt.title('Root Locus of GH(s) for K > 0')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)
plt.show()

control.root_locus(sys2)
plt.title('Root Locus of GH(s) for K > 0')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)
plt.show()

#سوال1