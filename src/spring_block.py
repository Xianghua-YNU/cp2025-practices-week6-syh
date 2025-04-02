import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def solve_ode_euler(step_num):
    # 创建存储位置和速度的数组，长度为 step_num + 1
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)

    # 计算时间步长
    time_step = 2 * np.pi / step_num

    # 设置初始位置和速度
    position[0] = 0
    velocity[0] = 1

    # 使用欧拉法迭代求解微分方程
    for i in range(step_num):
        # 根据微分方程更新位置
        position[i + 1] = position[i] + velocity[i] * time_step
        # 根据微分方程更新速度，这里假设 k = m = 1
        velocity[i + 1] = velocity[i] - position[i] * time_step

    # 生成时间数组
    time_points = np.arange(step_num + 1) * time_step

    return time_points, position, velocity


def spring_mass_ode_func(state, time):
    position, velocity = state
    d_position_dt = velocity
    d_velocity_dt = -position
    return [d_position_dt, d_velocity_dt]


def solve_ode_odeint(step_num):
    # 初始条件
    initial_state = [0, 1]
    # 时间点
    time_points = np.linspace(0, 2 * np.pi, step_num + 1)
    # 使用 odeint 求解微分方程
    solution = odeint(spring_mass_ode_func, initial_state, time_points)
    position = solution[:, 0]
    velocity = solution[:, 1]
    return time_points, position, velocity


def plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint):
    plt.figure(figsize=(12, 6))

    # 绘制位置对比图
    plt.subplot(1, 2, 1)
    plt.plot(time_euler, position_euler, 'ro', label='Euler Position')
    plt.plot(time_odeint, position_odeint, 'b-', label='ODEint Position')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Position Comparison')
    plt.legend()
    plt.grid(True)

    # 绘制速度对比图
    plt.subplot(1, 2, 2)
    plt.plot(time_euler, velocity_euler, 'gs', label='Euler Velocity')
    plt.plot(time_odeint, velocity_odeint, 'm-', label='ODEint Velocity')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity Comparison')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 模拟步数
    step_count = 100
    # 欧拉法求解
    time_euler, position_euler, velocity_euler = solve_ode_euler(step_count)
    # odeint 求解
    time_odeint, position_odeint, velocity_odeint = solve_ode_odeint(step_count)
    # 绘制对比结果
    plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint)    
