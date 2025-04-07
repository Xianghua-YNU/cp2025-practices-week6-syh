import numpy as np
from scipy.integrate import quad
import time

# 最概然速率 (m/s)
vp = 1578

# 麦克斯韦速率分布函数
def maxwell_distribution(v, vp):
    return (4 / np.sqrt(np.pi)) * (v**2 / vp**3) * np.exp(-(v**2) / (vp**2))

# 任务 1：计算 0 到 vp 的概率百分比
def percentage_0_to_vp(vp):
    result, _ = quad(maxwell_distribution, 0, vp, args=(vp,))
    return result * 100

# 任务 2：计算 0 到 3.3vp 的概率百分比
def percentage_0_to_3_3vp(vp):
    result, _ = quad(maxwell_distribution, 0, 3.3 * vp, args=(vp,))
    return result * 100

# 任务 3：计算 3×10^4 到 3×10^8 m/s 的概率百分比
def percentage_3e4_to_3e8(vp):
    result, _ = quad(maxwell_distribution, 3e4, 3e8, args=(vp,))
    return result * 100

# 梯形积分法则
def trapezoidal_rule(func, lower, upper, num_divisions):
    step = (upper - lower) / num_divisions
    total = 0.5 * (func(lower, vp) + func(upper, vp))
    for i in range(1, num_divisions):
        total += func(lower + i * step, vp)
    return total * step

# 使用梯形积分法计算任务 1
def percentage_0_to_vp_trap(vp, n=1000):
    result = trapezoidal_rule(maxwell_distribution, 0, vp, n)
    return result * 100

# 比较方法
def compare_methods(task_name, quad_function, trap_function, vp, n_list=[10, 100, 1000]):
    print(f"\n{task_name} 的方法对比:")
    # 使用 quad 计算（作为参考值）
    start = time.time()
    quad_res = quad_function(vp)
    quad_time = time.time() - start
    print(f"quad 方法: {quad_res:.6f}%, 耗时: {quad_time:.6f} 秒")
    # 使用不同区间划分数的梯形法则
    print("\n梯形积分法结果:")
    print(f"{'区间划分数':<12}{'结果 (%)':<15}{'相对误差 (%)':<15}{'计算时间 (秒)':<15}")
    for n in n_list:
        start = time.time()
        trap_res = trap_function(vp, n)
        trap_time = time.time() - start
        rel_error = abs(trap_res - quad_res) / quad_res * 100
        print(f"{n:<12}{trap_res:<15.6f}{rel_error:<15.6f}{trap_time:<15.6f}")

if __name__ == "__main__":
    print("=== 使用 quad 方法的结果 ===")
    print("0 到 vp 间概率百分比:", percentage_0_to_vp(vp), "%")
    print("0 到 3.3vp 间概率百分比:", percentage_0_to_3_3vp(vp), "%")
    print("3×10^4 到 3×10^8 间概率百分比:", percentage_3e4_to_3e8(vp), "%")
    print("\n=== quad 方法与梯形积分法对比 ===")
    compare_methods("任务 1: 0 到 vp", percentage_0_to_vp, percentage_0_to_vp_trap, vp)
