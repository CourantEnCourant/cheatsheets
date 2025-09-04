import torch


# -------------------------------
# Tensor Equality Check Example
# -------------------------------

T1 = torch.tensor([1., 2.])
T2 = torch.tensor([1., 2.])

are_equal = torch.allclose(T1, T2)
print("Tensors are equal:", are_equal)


# -------------------------------
# Lower Triangular Matrix Example
# -------------------------------

matrix = torch.tril(torch.ones(3, 3))
print("Lower triangular matrix:\n", matrix)
# Output:
# tensor([[1., 0., 0.],
#         [1., 1., 0.],
#         [1., 1., 1.]])


# -------------------------------
# Masked Fill Example (Attention Mask)
# -------------------------------

import torch.nn.functional as F

T = 5  # context length
tril = torch.tril(torch.ones(T, T))
print("Lower triangular mask:\n", tril)

wei = torch.zeros(T, T)
wei = wei.masked_fill(tril == 0, float('-inf'))
print("Masked weights (before softmax):\n", wei)

wei = F.softmax(wei, dim=-1)
print("Weights after softmax:\n", wei)
