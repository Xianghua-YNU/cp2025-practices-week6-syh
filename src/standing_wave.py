import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sineWaveZeroPhi(x, t, A, omega, k):
    """
    计算波函数y(x,t) = A*sin(kx - ωt)
    
    参数:
    x : 空间位置数组
    t : 时间值
    A : 振幅
    omega : 角频率
    k : 波数
    """
    return A * np.sin(k * x - omega * t)

# 创建绘图窗口和坐标轴
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('x (m)')
ax.set_ylabel('Amplitude (m)')
ax.grid(True, linestyle='--', alpha=0.7)

# 创建不同颜色的线条对象
right_wave, = ax.plot([], [], 'b-', lw=2, label='Right Traveling')
left_wave, = ax.plot([], [], 'r--', lw=2, label='Left Traveling')
standing_wave, = ax.plot([], [], 'g-', lw=3, label='Standing Wave')
lines = [right_wave, left_wave, standing_wave]

def init():
    """初始化动画"""
    for line in lines:
        line.set_data([], [])
    return lines

# 生成空间网格
x = np.linspace(0, 10, 1000)

def animate(frame):
    """更新每一帧的数据"""
    A = 1.0
    omega = 2 * np.pi  # 2Hz频率
    k = np.pi / 2      # 波长4m
    t = 0.01 * frame    # 时间步长

    # 计算两个方向相反的行波
    y_right = sineWaveZeroPhi(x, t, A, omega, k)
    y_left = sineWaveZeroPhi(x, t, A, -omega, k)
    
    # 叠加形成驻波
    y_standing = y_right + y_left

    # 更新线条数据
    lines[0].set_data(x, y_right)
    lines[1].set_data(x, y_left)
    lines[2].set_data(x, y_standing)
    
    return lines

if __name__ == "__main__":
    # 创建动画
    anim = FuncAnimation(fig, animate, init_func=init,
                        frames=200, interval=20, blit=True)
    
    ax.legend()
    plt.tight_layout()
    plt.show()
