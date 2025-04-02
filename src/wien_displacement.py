import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def visualize_wien_eq():
    # 设置全局字体为黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

    """
    绘制维恩方程的两个函数图像
    包括 y = 5e^(-x) 曲线和 y = 5 - x 直线，交点为方程的解
    """
    x = np.linspace(-1, 6, 200)
    plt.figure(figsize=(10, 8))
    plt.plot(x, 5 * np.exp(-x), 'g', label='y = 5 * exp(-x)')
    plt.plot(x, 5 - x, label='y = 5 - x')
    plt.xlabel('x 轴')
    plt.xticks(rotation=45)
    plt.ylabel('y 轴')
    plt.title('维恩方程的图像解法')
    plt.legend()
    plt.grid(True)
    plt.show()


def wien_eq(x):
    """
    维恩方程：5e^(-x) + x - 5 = 0
    :param x: 方程的自变量
    :return: 方程的函数值
    """
    return 5 * np.exp(-x) + x - 5


def calc_wien_constant(init_val):
    """
    求解维恩位移常数
    通过求解非线性方程 5e^(-x) + x - 5 = 0 得到 x 值，再计算维恩位移常数 b = hc/(k_B * x)
    :param init_val: 求解方程的初始值
    :return: (x, b)，x 是非线性方程的解，b 是维恩位移常数（单位：m·K）
    """
    solution = fsolve(wien_eq, init_val)
    x = float(solution[0])
    b = constants.h * constants.c / (constants.k * x)
    return x, b


def estimate_temperature(peak_wavelength, init_val=5.0):
    """
    基于维恩位移定律 λT = b，根据辐射峰值波长计算黑体温度
    :param peak_wavelength: 峰值波长（单位：米）
    :param init_val: 求解方程的初始值，默认为 5.0
    :return: 黑体温度（单位：开尔文）
    """
    _, b = calc_wien_constant(init_val)
    return b / peak_wavelength


if __name__ == "__main__":
    visualize_wien_eq()
    try:
        initial_val = float(input("请依据图像输入方程求解的初始值（推荐值 4 - 6）："))
    except ValueError:
        print("输入无效，将采用默认值 5")
        initial_val = 5

    x_val, wien_b = calc_wien_constant(initial_val)
    print(f"\n使用初值 x0 = {initial_val}")
    print(f"方程的解 x = {x_val:.6f}")
    print(f"维恩位移常数 b = {wien_b:.6e} m·K")

    sun_wavelength = 502e-9
    sun_temp = estimate_temperature(sun_wavelength, initial_val)
    print(f"\n太阳表面温度估计值：{sun_temp:.0f} K")
