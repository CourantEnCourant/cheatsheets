from tqdm import tqdm
from tqdm import trange

# Basic use
tasks = ['task1', 'task2', 'task3']
for task in tqdm(tasks):
    continue

# trange, to replace range. Two following examples are equivalent.
for task in trange(100):
    continue

for task in tqdm(range(100)):
    continue

# Add description
for task in tqdm(tasks, desc="Your description"):
    continue