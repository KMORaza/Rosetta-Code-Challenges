# Euler method
import numpy as np
def euler_method(initial_time, initial_temperature, elapsed_time, step_size):
    room_temperature = 20
    cooling_constant = 0.07
    num_steps = int(elapsed_time / step_size)
    time = np.zeros(num_steps + 1)
    temperature = np.zeros(num_steps + 1)
    time[0] = initial_time
    temperature[0] = initial_temperature
    for i in range(num_steps):
        time[i + 1] = time[i] + step_size
        temperature[i + 1] = temperature[i] - cooling_constant * (temperature[i] - room_temperature) * step_size
    return time, temperature
initial_time = 0
initial_temperature = 100
elapsed_time = 100
step_sizes = [2, 5, 10]
for step_size in step_sizes:
    time, temperature = euler_method(initial_time, initial_temperature, elapsed_time, step_size)
    print(f"Step Size: {step_size} s")
    print("Time (s)\tTemperature (°C)")
    for t, T in zip(time, temperature):
        print(f"{t:.2f}\t\t{T:.2f}")
    print()