import numpy as np
import matplotlib.pyplot as plt

# One week contains 168 hours
t = np.linspace(0, 168, 1000)

# Generate periodic cycles
weekly = np.sin(2 * np.pi * t / 168)
daily = 0.6 * np.sin(2 * np.pi * t / 24)
half_daily = 0.5 * np.sin(2 * np.pi * t / 12)
eight_hour = 0.4 * np.sin(2 * np.pi * t / 8)

# Combine the cycles
resonance = weekly + daily + half_daily + eight_hour

# Plot the combined signal
plt.figure(figsize=(12, 5))
plt.plot(t, resonance, label="Combined resonance")

plt.xlabel("Time (hours)")
plt.ylabel("Amplitude")
plt.title("NeAR: Multi-scale Periodic Resonance")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()