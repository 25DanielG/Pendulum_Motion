from math import sin, cos, pi, isclose
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

m = 0.1
l = 0.5
g = 9.8
c = 0.1
Tt = 0.1
dt = 0.05

def update_pendulum(theta_old, omega_old, torque_old):
    theta =  theta_old + dt * omega_old
    omega =  omega_old + (dt / (m * l ** 2)) * (m * g * l * sin(theta_old) + torque_old - c * omega_old)
    return theta, omega

assert update_pendulum(0, 1, 1) == (0.05, 2.8), "update_pendulum is not correct."
t1, t2 = update_pendulum(1, 0, 1)
assert t1 == 1.0, "update_pendulum is not correct."
assert isclose(t2, 2.8246415651117385), "update_pendulum is not correct."
print("update_pendulum is correct.")

def run_pendulum(theta_0, omega_0, n_end):
    theta_vec = [theta_0]
    omega_vec = [omega_0]

    for i in range(n_end):
        theta, omega = update_pendulum(theta_vec[-1], omega_vec[-1], Tt)
        theta_vec.append(theta)
        omega_vec.append(omega)

    return theta_vec, omega_vec

t1, t2 = run_pendulum(0, 0, 3)
assert isclose(t1[2], 0.01), "run_pendulum is not correct."
assert isclose(t1[3], 0.028), "run_pendulum is not correct."
assert isclose(t2[2], 0.36), "run_pendulum is not correct."
assert isclose(t2[3], 0.49779983666748334), "run_pendulum is not correct."
print("run_pendulum is correct.")

def plot_pendulum(theta_vec, omega_vec):
    plt.plot(theta_vec, omega_vec, label='Pendulum Motion')
    plt.xlabel('Angular Position (theta)')
    plt.ylabel('Angular Velocity (omega)')
    plt.title('Theta vs. Omega')
    plt.legend()
    plt.grid(True)
    plt.show()

n_end = 200
theta_0 = 0
omega_0 = 0

theta_vec, omega_vec = run_pendulum(theta_0, omega_0, n_end)
plot_pendulum(theta_vec, omega_vec)

def plot_pendulum_positions(theta_vec, l):
    x_vec = [-l * sin(theta) for theta in theta_vec]
    y_vec = [l * cos(theta) for theta in theta_vec]
    plt.scatter(x_vec, y_vec, label='Pendulum Positions')
    plt.xlabel('x-pos')
    plt.ylabel('y-pos')
    plt.title('Pendulum Positions')
    plt.legend()
    plt.grid(True)
    plt.show()

n_end = 200
theta_0 = 0
omega_0 = 0
l = 0.5

theta_vec, omega_vec = run_pendulum(theta_0, omega_0, n_end)
plot_pendulum_positions(theta_vec, l)

def plot_pendulum_positions(theta_vec, l):
    x_vec = [-l * sin(theta) for theta in theta_vec]
    y_vec = [l * cos(theta) for theta in theta_vec]

    plt.scatter(x_vec, y_vec, label='Pendulum Positions')
    plt.xlabel('x-pos')
    plt.ylabel('y-pos')
    plt.title('Pendulum Positions')
    plt.legend()
    plt.axis('equal')
    plt.xlim([-1.1 * l, 1.1 * l])
    plt.ylim([-1.1 * l, 1.1 * l])
    plt.grid(True)
    plt.show()

theta_0 = 1/2
omega_0 = 0
n_end = 20
n_values = [0, 5, 10, 15]

theta_vec, omega_vec = run_pendulum(theta_0, omega_0, n_end)

theta_plot = [theta_vec[n] for n in n_values]

plot_pendulum_positions(theta_plot, l)

fig = plt.figure(figsize=(6, 6))
ax = plt.gca()
plot0, = ax.plot([0, 1], [0, 1], "k--")
plot1, = ax.plot([], [], marker='o', markersize=10, markerfacecolor='red')

plt.xlim((-1.1 * l, 1.1 * l))
plt.ylim((-1.1 * l, 1.1 * l))

def update(i):
    theta_vec, omega_vec = run_pendulum(theta_0, omega_0, n_end)
    x = [-l * sin(theta) for theta in theta_vec[:i+1]]
    y = [l * cos(theta) for theta in theta_vec[:i+1]]
    plot1.set_data(x, y)
    return plot1

anim = FuncAnimation(fig, update, frames=range(n_end), interval=100, repeat=True)
HTML(anim.to_html5_video())