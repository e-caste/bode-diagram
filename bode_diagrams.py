# docs at https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.TransferFunction.html

from scipy import signal
import matplotlib.pyplot as plt

# LTI = Linear Time Invariant | TC = Time Continuous | TD = Time Discrete

# rightmost value is lowest degree power of s (if sys is LTI TC) or z (if sys is LTI TD)
num = [3., 5.]
den = [1., 1.]
k = .5  # gain
sample_time = .1  # seconds

# specify dt (sampling time of the discrete time system) if LTI sys is TD
# do NOT specify dt (not even dt=None) if LTI sys is TC
sys = signal.TransferFunction([k*num_coeff for num_coeff in num], den)  # LTI TC
# sys = signal.TransferFunction([k*num_coeff for num_coeff in num], den, dt=sample_time)  # LTI TD
print("Zeros {}".format(sys.zeros))
print("Poles {}".format(sys.poles))
w, mag, phase = sys.bode()
# print("w={} \n\n mag={} \n\n phase={}".format(w, mag, phase))  # too verbose

plot = plt.figure(figsize=(8, 8))  # each unit is an inch = 80 pixels
plot.suptitle("Bode Diagram")

ax_mag = plot.add_subplot(211)
ax_mag.set_title("Magnitude")
ax_mag.set_ylabel("dB")
ax_mag.semilogx(w, mag)
plt.grid(which="both")

ax_phs = plot.add_subplot(212)
ax_phs.set_title("Phase")
ax_phs.set_ylabel("degrees °")
ax_phs.set_xlabel("rad/s - Hz")  # 1 Hz = 2π rad/s | 1 rad/s = 1/2π Hz
ax_phs.semilogx(w, phase)
plt.grid(which="both")

plt.show()
