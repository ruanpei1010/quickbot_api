"""
PID controller
"""


class PID:
    """
    Classical PID controller.

    Example:

        pid = PID(Kp=1.0, Ki=0.1, Kd=0.05)

        for input in read_input():
            output = pid(input)
    """

    def __init__(self, Kp, Ki=0, Kd=0, x0=0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self._x_prev = x0
        self._acc = 0

    def __call__(self, x):
        self._acc += x

        out = self.Kp * x + self.Ki * self._acc + self.Kd * (x - self._x_prev)
        self._x_prev = x

        return out
