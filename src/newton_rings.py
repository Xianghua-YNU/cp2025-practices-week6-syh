import numpy as np
import matplotlib.pyplot as plt


def setup_parameters():
    # 氦氖激光波长 (m)
    lambda_light = 632.8e-9
    # 透镜曲率半径 (m)
    R_lens = 0.1
    return lambda_light, R_lens


def generate_grid():
    # 生成 x 和 y 方向的坐标，调整范围至 -0.001 到 0.001，增加点数以提高分辨率
    x = np.linspace(-0.001, 0.001, 1000)
    y = np.linspace(-0.001, 0.001, 1000)
    # 生成网格坐标
    X, Y = np.meshgrid(x, y)
    # 计算径向距离
    r = np.sqrt(X**2 + Y**2)
    return X, Y, r


def calculate_intensity(r, lambda_light, R_lens):
    # 计算空气膜厚度
    d = R_lens - np.sqrt(R_lens**2 - r**2)
    # 生成干涉强度
    intensity = 4 * np.sin(2 * np.pi * d / lambda_light)**2
    return intensity


def plot_newton_rings(intensity):
    plt.figure(figsize=(10, 10))
    # 绘制图像，调整对比度，更新绘图范围
    plt.imshow(intensity, cmap='gray', extent=(-0.001, 0.001, -0.001, 0.001), vmin=0, vmax=1)
    # 添加颜色条
    plt.colorbar(label='Intensity')
    # 设置标题
    plt.title("Newton's Rings (Analytical Solution)")
    # 设置 x 轴标签
    plt.xlabel("x (m)")
    # 设置 y 轴标签
    plt.ylabel("y (m)")
    # 显示图像
    plt.show()


if __name__ == "__main__":
    # 设置参数
    lambda_light, R_lens = setup_parameters()
    # 生成网格坐标
    X, Y, r = generate_grid()
    # 计算干涉强度分布
    intensity = calculate_intensity(r, lambda_light, R_lens)
    # 绘制牛顿环
    plot_newton_rings(intensity)
