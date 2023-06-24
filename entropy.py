import numpy as np

def entropy(y: np.ndarray) -> float:  
    _, count = np.unique(y, return_counts=True)
    p = count / len(y)
    return -np.sum(p * np.log(p))

x = [1,3,3,5,7,7,8,0]
x = np.array(x)
print(entropy(x)) 