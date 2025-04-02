import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def plot_wien_equation():
    x = np.linspace(-1, 6, 100)
    plt.figure(figsize=(8, 6))
    plt.plot(x, 5 * np.exp(-x), 'r', label='y = 5 * exp(-x)')
    plt.plot(x, 5 - x, label='y = 5 - x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphical Solution of Wien Equation')
    plt.legend()
    plt.grid(True)
    plt.show()

def wien_equation(x):
    return 5 * np.exp(-x) + x - 5

def solve_wien_constant(x0):
    try:
        # 求解非线性方程
        x = float(fsolve(wien_equation, x0)[0])
    except Exception as e:
        print(f"求解非线性方程时出错: {e}")
        return None, None

    # 计算维恩位移常数
    b = constants.h * constants.c / (constants.k * x)
    return x, b

def calculate_temperature(wavelength, x0=5.0):
    if wavelength <= 0:
        print("波长必须为正数。")
        return None
    _, b = solve_wien_constant(x0)
    if b is None:
        return None
    return b / wavelength

if __name__ == "__main__":
    # 绘制方程图像
    plot_wien_equation()

    # 从键盘输入初值
    while True:
        try:
            x0 = float(input("请根据图像输入方程求解的初始值（建议值为4 - 6）："))
            break
        except ValueError:
            print("输入无效，请输入一个有效的数字。")
    x0 = x0 if 4 <= x0 <= 6 else 5

    # 计算维恩位移常数
    x, b = solve_wien_constant(x0)
    if x is not None and b is not None:
        print(f"\n使用初值 x0 = {x0}")
        print(f"方程的解 x = {x:.6f}")
        print(f"维恩位移常数 b = {b:.6e} m·K")

        # 计算太阳表面温度
        wavelength_sun = 502e-9  # 502 nm 转换为米
        temperature_sun = calculate_temperature(wavelength_sun, x0)
        if temperature_sun is not None:
            print(f"\n太阳表面温度估计值：{temperature_sun:.0f} K")    
