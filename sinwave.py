import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    t = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * t)
    plt.plot(t, y)
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()