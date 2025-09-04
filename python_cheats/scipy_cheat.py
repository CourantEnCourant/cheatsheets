from scipy.stats import entropy
from scipy.special import kl_div

# Calculate entropy
P = np.array([0.5, 0.5])
ent = entropy(P, base=2)

# Relative entropy
P = np.array([0.25, 0.25, 0.25, 0.25])
Q = np.array([0.1, 0.1, 0.4, 0.4])
kl_divergence = kl_div(P, Q)

## Numpy
kl_divergence = P * np.log2(P/Q)