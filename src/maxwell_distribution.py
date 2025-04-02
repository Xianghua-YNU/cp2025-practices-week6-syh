import numpy as np
from scipy.integrate import quad
import time


# 定义常量，最概然速率
MOST_PROBABLE_SPEED = 1578


# 麦克斯韦分布函数
def maxwell_speed_distribution(speed, probable_speed):
    exponent_part = np.exp(-(speed ** 2) / (probable_speed ** 2))
    coefficient = 4 * np.pi * (speed ** 2 / probable_speed ** 3)
    return coefficient * exponent_part


# 积分计算函数（使用quad）
def calculate_integral_quad(func, lower_bound, upper_bound, args):
    result, _ = quad(func, lower_bound, upper_bound, args=args)
    return result * 100


# 梯形积分函数
def trapezoidal_integration(func, lower, upper, num_segments):
    step_size = (upper - lower) / num_segments
    sum_value = 0.5 * (func(lower, MOST_PROBABLE_SPEED) + func(upper, MOST_PROBABLE_SPEED))
    for i in range(1, num_segments):
        current_point = lower + i * step_size
        sum_value += func(current_point, MOST_PROBABLE_SPEED)
    return sum_value * step_size * 100


# 任务 1：0 到 vp 的概率百分比（quad）
def task_1_quad():
    return calculate_integral_quad(maxwell_speed_distribution, 0, MOST_PROBABLE_SPEED, (MOST_PROBABLE_SPEED,))


# 任务 2：0 到 3.3vp 的概率百分比（quad）
def task_2_quad():
    upper = 3.3 * MOST_PROBABLE_SPEED
    return calculate_integral_quad(maxwell_speed_distribution, 0, upper, (MOST_PROBABLE_SPEED,))


# 任务 3：3×10^4 到 3×10^8 m/s 的概率百分比（quad）
def task_3_quad():
    lower = 3e4
    upper = 3e8
    return calculate_integral_quad(maxwell_speed_distribution, lower, upper, (MOST_PROBABLE_SPEED,))


# 任务 1：0 到 vp 的概率百分比（梯形积分）
def task_1_trapezoidal(num_segments=1000):
    return trapezoidal_integration(maxwell_speed_distribution, 0, MOST_PROBABLE_SPEED, num_segments)


# 方法比较函数
def compare_integration_methods(task_name, quad_method, trapezoidal_method, segment_list=[10, 100, 1000]):
    print(f"\n{task_name} 的方法对比:")

    # quad 方法计算
    start_time = time.time()
    quad_result = quad_method()
    quad_time = time.time() - start_time
    print(f"quad 方法: {quad_result:.6f}%, 耗时: {quad_time:.6f} 秒")

    # 梯形积分法计算
    print("\n梯形积分法结果:")
    print(f"{'区间划分数':<12}{'结果 (%)':<15}{'相对误差 (%)':<15}{'计算时间 (秒)':<15}")
    for segments in segment_list:
        start = time.time()
        trapezoidal_result = trapezoidal_method(segments)
        end = time.time()
        relative_error = abs(trapezoidal_result - quad_result) / quad_result * 100
        trapezoidal_time = end - start
        print(f"{segments:<12}{trapezoidal_result:<15.6f}{relative_error:<15.6f}{trapezoidal_time:<15.6f}")


if __name__ == "__main__":
    print("=== 使用 quad 方法的结果 ===")
    print(f"0 到 vp 间概率百分比: {task_1_quad()} %")
    print(f"0 到 3.3vp 间概率百分比: {task_2_quad()} %")
    print(f"3×10^4 到 3×10^8 间概率百分比: {task_3_quad()} %")

    print("\n=== quad 方法与梯形积分法对比 ===")
    compare_integration_methods("任务 1: 0 到 vp", task_1_quad, task_1_trapezoidal)
