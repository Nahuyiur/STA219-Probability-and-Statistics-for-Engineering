import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

# 定义不同的 λ 值
lambda_values = [5, 10, 20, 50]

# 创建图形
plt.figure(figsize=(12, 10))

for i, lam in enumerate(lambda_values):
    # 泊松分布
    x_poisson = np.arange(0, lam + 3 * np.sqrt(lam))  # 范围从 0 到 λ + 3σ
    y_poisson = poisson.pmf(x_poisson, lam)
    
    # 正态分布近似
    x_normal = np.linspace(0, lam + 3 * np.sqrt(lam), 1000)
    y_normal = norm.pdf(x_normal, lam, np.sqrt(lam))
    
    # 创建子图
    plt.subplot(2, 2, i + 1)
    plt.bar(x_poisson, y_poisson, width=0.5, color='yellow', alpha=0.6, label=f'Poisson λ={lam}')
    plt.plot(x_normal, y_normal, 'b-', label=f'Normal Approx. λ={lam}')
    plt.title(f'Poisson and Normal Approximation (λ={lam})')
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.legend()

# 显示图形
plt.tight_layout()
plt.show()