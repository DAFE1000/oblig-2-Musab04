import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ─────────────────────────────────────────────
# Funksjonen og den kritiske likninga
# f(x) = e^(-x/4) * arctan(x)
# f'(x) = 0  =>  arctan(x) - 4/(x^2+1) = 0
# ─────────────────────────────────────────────

def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    # g(x) = arctan(x) - 4/(x^2+1)  →  løys g(x) = 0
    return np.arctan(x) - 4 / (x**2 + 1)

# ─────────────────────────────────────────────
# Finn rota numerisk med Brent-metoden
# ─────────────────────────────────────────────
x_max = brentq(g, 0.1, 5.0)
y_max = f(x_max)

print(f"x-koordinat: {x_max:.6f}")
print(f"y-koordinat: {y_max:.6f}")
print(f"Kontroll g(x_max) ≈ {g(x_max):.2e}")

# ─────────────────────────────────────────────
# Plott
# ─────────────────────────────────────────────
x = np.linspace(-3, 10, 800)
y = f(x)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x, y, color='#c8a96e', linewidth=2.2,
        label=r'$f(x)=e^{-x/4}\cdot\arctan x$')
ax.axhline(0, color='#555', linewidth=0.8)
ax.axvline(0, color='#555', linewidth=0.8)

ax.scatter([x_max], [y_max], color='#7eb8c9', s=90, zorder=5)
ax.annotate(
    f"Toppunkt\n({x_max:.4f}, {y_max:.4f})",
    xy=(x_max, y_max), xytext=(x_max + 1.2, y_max - 0.08),
    arrowprops=dict(arrowstyle='->', color='#7eb8c9'),
    color='#7eb8c9', fontsize=10
)

ax.set_title(r'$f(x)=e^{-x/4}\cdot\arctan x$ — Toppunkt markert', fontsize=13)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('toppunkt_plot.png', dpi=150)
plt.show()
