import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

plt.ion()


# %%


class Experiment:
    def __init__(self, n_items):
        self.n_items = n_items
        self.t = 0
        self.reset()

    def reset(self):
        self.state = np.arange(1, self.n_items + 1, dtype=np.float32)
        ret = self.t
        self.t = 0
        return ret

    def step(self):
        # Move the ith item to position j.
        i = np.random.randint(self.n_items)
        j = np.random.randint(self.n_items + 1)
        if i == j:
            pass
        elif j == 0:
            self.state[i] = self.state[0] - 1
        elif j == self.n_items:
            self.state[i] = self.state[-1] + 1
        else:
            self.state[i] = (self.state[j - 1] + self.state[j]) / 2
        # Make sure the state is still ordered.
        self.state.sort()
        self.t += 1
        return self.required_precision()

    def required_precision(self):
        return np.diff(self.state).min()

    def step_until_losing_precision(self, max_steps=1_000_000):
        precision = self.required_precision()
        while precision > 0 and self.t < max_steps:
            precision = self.step()
        return self.reset()

exp = Experiment(100)
vals = [exp.step_until_losing_precision() for _ in tqdm(range(1000))]

plt.figure(1)
plt.clf()
plt.hist(vals)
