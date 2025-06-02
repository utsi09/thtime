import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 시각화 스타일
mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Nimbus Roman", "Times New Roman", "DejaVu Serif"],
    "font.size": 13,
    "axes.labelsize": 13,
    "axes.titlesize": 21,
    "legend.fontsize": 15,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "lines.linewidth": 1.2,
    "lines.markersize": 4,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.grid": False,
})

# 파라미터
lambda_val = 0.7
thresholds = np.linspace(5, 100, 300)
safe_colors = ['#1f77b4', '#2ca02c', '#9467bd', '#17becf', '#8c564b']
markers = ['o', '^', 'D', 's', 'v']
plt.figure(figsize=(10, 6))

color_idx = 0

for i, k in enumerate(range(1, 11, 2)):
    t_fail = (1 / lambda_val) * np.log(thresholds / k)
    marker = markers[i % len(markers)]
    
    if k == 3:
        plt.plot(thresholds, t_fail,
                 label=f'Experimental k={k}',
                 color='r', linestyle='-', linewidth=1.8,
                 marker=marker, markersize=4, markevery=20)
    else:
        plt.plot(thresholds, t_fail,
                 label=f'k={k}',
                 color=safe_colors[color_idx % len(safe_colors)],
                 linestyle='--', linewidth=1.2,
                 marker=marker, markersize=4, markevery=20)
        color_idx += 1

# 기준선
plt.axvline(x=20, color='r', linestyle='--', linewidth=1.0,
            label=r'Experimental threshold $T_h = 20$')

# 라벨, 타이틀
plt.xlabel(r'Threshold $T_h$')
plt.ylabel('Fail-safe Activation Time (s)')
plt.title('Fail-safe Operating Time in Proportion to Threshold')

# 범례
plt.legend(loc='best', frameon=False, ncol=2, handlelength=2, labelspacing=0.4)

# 출력
plt.tight_layout()
plt.savefig('/home/taewook/Downloads/failsafe_activation_time_cleaned.svg', format='svg', bbox_inches='tight')
plt.show()
