import numpy as np
import matplotlib.pyplot as plt


def get_parameters():
    """
    获取模拟牛顿环所需的参数。

    返回:
    tuple: 包含激光波长、透镜曲率半径的元组
    """
    # 激光波长 (m)
    wavelength = 532e-9
    # 透镜曲率半径 (m)
    curvature_radius = 0.2
    return wavelength, curvature_radius


def create_grid():
    """
    创建模拟所需的网格坐标。

    返回:
    tuple: 包含网格坐标 X、Y 以及径向距离 r 的元组
    """
    # 生成 x 和 y 方向的坐标，调整范围和点数
    x_coords = np.linspace(-0.002, 0.002, 1200)
    y_coords = np.linspace(-0.002, 0.002, 1200)
    # 生成网格坐标
    X, Y = np.meshgrid(x_coords, y_coords)
    # 计算径向距离
    radial_distance = np.sqrt(X**2 + Y**2)
    return X, Y, radial_distance


def compute_intensity(radial_distance, wavelength, curvature_radius):
    """
    计算干涉强度分布。

    参数:
    radial_distance (np.ndarray): 径向距离数组
    wavelength (float): 激光波长
    curvature_radius (float): 透镜曲率半径

    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 计算空气膜厚度
    air_thickness = curvature_radius - np.sqrt(curvature_radius**2 - radial_distance**2)
    # 生成干涉强度
    light_intensity = 4 * np.sin(2 * np.pi * air_thickness / wavelength)**2
    return light_intensity


def draw_newton_rings(light_intensity):
    """
    绘制牛顿环干涉条纹图像。

    参数:
    light_intensity (np.ndarray): 干涉强度分布数组
    """
    plt.figure(figsize=(8, 8))
    # 绘制图像，调整对比度和绘图范围
    plt.imshow(light_intensity, cmap='gray', extent=(-0.002, 0.002, -0.002, 0.002), vmin=0, vmax=1)
    # 添加颜色条
    plt.colorbar(label='Intensity')
    # 设置标题
    plt.title("Newton's Rings Simulation")
    # 设置 x 轴标签
    plt.xlabel("x (m)")
    # 设置 y 轴标签
    plt.ylabel("y (m)")
    # 显示图像
    plt.show()


def analyze_parameter_effect():
    """
    分析不同参数对干涉图样的影响
    """
    wavelength, curvature_radius = get_parameters()
    X, Y, r = create_grid()

    # 分析波长变化的影响
    wavelengths = [400e-9, 532e-9, 650e-9]
    plt.figure(figsize=(15, 5))
    for i, wl in enumerate(wavelengths):
        intensity = compute_intensity(r, wl, curvature_radius)
        plt.subplot(1, 3, i + 1)
        plt.imshow(intensity, cmap='gray', extent=(-0.002, 0.002, -0.002, 0.002), vmin=0, vmax=1)
        plt.title(f'Wavelength = {wl * 1e9} nm')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
    plt.tight_layout()
    plt.show()

    # 分析曲率半径变化的影响
    radii = [0.1, 0.2, 0.3]
    plt.figure(figsize=(15, 5))
    for i, rad in enumerate(radii):
        intensity = compute_intensity(r, wavelength, rad)
        plt.subplot(1, 3, i + 1)
        plt.imshow(intensity, cmap='gray', extent=(-0.002, 0.002, -0.002, 0.002), vmin=0, vmax=1)
        plt.title(f'Curvature Radius = {rad} m')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 获取参数
    wavelength, curvature_radius = get_parameters()
    # 创建网格坐标
    X, Y, r = create_grid()
    # 计算干涉强度分布
    intensity = compute_intensity(r, wavelength, curvature_radius)
    # 绘制牛顿环
    draw_newton_rings(intensity)
    # 分析不同参数对干涉图样的影响
    analyze_parameter_effect()
