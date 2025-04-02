import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def spring_block_ode(y, t, m, k):
    """
    弹簧 - 物块系统的常微分方程。

    参数:
    y (list): 包含位置和速度的列表 [x, v]
    t (float): 时间
    m (float): 物块质量
    k (float): 弹簧系数

    返回:
    list: 包含位置和速度的导数的列表 [dx/dt, dv/dt]
    """
    x, v = y
    dxdt = v
    dvdt = -k * x / m
    return [dxdt, dvdt]


def solve_ode_odeint(m, k, t_end, num_points):
    """
    使用odeint求解弹簧 - 物块系统的常微分方程。

    参数:
    m (float): 物块质量
    k (float): 弹簧系数
    t_end (float): 模拟结束时间
    num_points (int): 模拟的点数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # 初始条件
    y0 = [0, 1]
    # 时间点
    t = np.linspace(0, t_end, num_points)
    # 使用odeint求解微分方程
    sol = odeint(spring_block_ode, y0, t, args=(m, k))
    position = sol[:, 0]
    velocity = sol[:, 1]
    return t, position, velocity


def solve_ode_euler(m, k, step_num, t_end):
    """
    使用欧拉法求解弹簧 - 物块系统的常微分方程。

    参数:
    m (float): 物块质量
    k (float): 弹簧系数
    step_num (int): 模拟的步数
    t_end (float): 模拟结束时间

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # 创建存储位置和速度的数组，长度为 step_num + 1
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)

    # 计算时间步长
    time_step = t_end / step_num

    # 设置初始位置和速度
    position[0] = 0
    velocity[0] = 1

    # 使用欧拉法迭代求解微分方程
    for i in range(step_num):
        # 根据微分方程更新位置
        position[i + 1] = position[i] + velocity[i] * time_step
        # 根据微分方程更新速度
        velocity[i + 1] = velocity[i] - (k / m) * position[i] * time_step

    # 生成时间数组
    time_points = np.arange(step_num + 1) * time_step

    return time_points, position, velocity


if __name__ == "__main__":
    m = 1.0
    k = 1.0
    t_end = 2 * np.pi
    num_points = 100

    # 使用odeint求解
    t_odeint, position_odeint, velocity_odeint = solve_ode_odeint(m, k, t_end, num_points)

    # 使用欧拉法求解
    t_euler, position_euler, velocity_euler = solve_ode_euler(m, k, num_points, t_end)

    # 绘制位置随时间的变化
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t_odeint, position_odeint, label='odeint')
    plt.plot(t_euler, position_euler, label='Euler')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Position vs Time')
    plt.legend()

    # 绘制速度随时间的变化
    plt.subplot(1, 2, 2)
    plt.plot(t_odeint, velocity_odeint, label='odeint')
    plt.plot(t_euler, velocity_euler, label='Euler')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity vs Time')
    plt.legend()

    plt.tight_layout()
    plt.show()
