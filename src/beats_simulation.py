import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    任务1: 拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
    """
    # 学生任务1: 生成时间范围
    t = None
    
    # 学生任务2: 生成两个正弦波
    wave1 = None
    wave2 = None

    # 学生任务3: 叠加两个波
    superposed_wave = None

    # 学生任务4: 计算拍频
    beat_frequency = None

    # 学生任务5: 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 6))
        
        # 绘制第一个波
        plt.subplot(3, 1, 1)
        # 学生任务6: 完成wave1的绘制
        
        # 绘制第二个波
        plt.subplot(3, 1, 2)
        # 学生任务7: 完成wave2的绘制
        
        # 绘制叠加波
        plt.subplot(3, 1, 3)
        # 学生任务8: 完成superposed_wave的绘制

        plt.tight_layout()
        plt.show()
import numpy as np
import matplotlib.pyplot as plt


def create_time_array(t_start, t_end, num_points):
    """生成时间数组"""
    return np.linspace(t_start, t_end, num_points)


def generate_sine_waves(f1, f2, A1, A2, t):
    """生成两个正弦波"""
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)
    return wave1, wave2


def superpose_waves(wave1, wave2):
    """叠加两个正弦波"""
    return wave1 + wave2


def calculate_beat(f1, f2):
    """计算拍频"""
    return np.abs(f1 - f2)


def plot_waves(t, wave1, wave2, superposed_wave, beat_frequency, f1, f2, A1, A2):
    """绘制波形图"""
    plt.figure(figsize=(12, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t, wave1, label=f'Wave 1 (f={f1} Hz, A={A1})')
    plt.title('Wave 1')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, wave2, label=f'Wave 2 (f={f2} Hz, A={A2})')
    plt.title('Wave 2')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, superposed_wave, label=f'Superposed Wave (Beat f={beat_frequency} Hz)')
    plt.title('Superposed Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.tight_layout()
    plt.show()


def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    模拟并可视化两个正弦波叠加产生的拍频现象
    """
    t = create_time_array(t_start, t_end, num_points)
    wave1, wave2 = generate_sine_waves(f1, f2, A1, A2, t)
    superposed_wave = superpose_waves(wave1, wave2)
    beat_frequency = calculate_beat(f1, f2)

    if show_plot:
        plot_waves(t, wave1, wave2, superposed_wave, beat_frequency, f1, f2, A1, A2)

    return t, superposed_wave, beat_frequency


def analyze_frequency_difference():
    """分析频率差对拍频现象的影响"""
    base_freq = 440
    freq_diffs = [1, 2, 5, 10]
    plt.figure(figsize=(12, 8))

    for idx, diff in enumerate(freq_diffs, start=1):
        t, wave, _ = simulate_beat_frequency(f1=base_freq, f2=base_freq + diff, show_plot=False)
        plt.subplot(2, 2, idx)
        plt.plot(t, wave)
        plt.title(f'Frequency diff = {diff} Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()


def analyze_amplitude_ratio():
    """分析振幅比例对拍频现象的影响"""
    amplitude_ratios = [0.5, 1.0, 2.0, 5.0]
    plt.figure(figsize=(12, 8))

    for idx, ratio in enumerate(amplitude_ratios, start=1):
        t, wave, _ = simulate_beat_frequency(A2=ratio, show_plot=False)
        plt.subplot(2, 2, idx)
        plt.plot(t, wave)
        plt.title(f'Amplitude ratio = {ratio}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()


def parameter_sensitivity_analysis():
    """综合分析频率差和振幅比例对拍频现象的影响"""
    analyze_frequency_difference()
    analyze_amplitude_ratio()


if __name__ == "__main__":
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")

    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
