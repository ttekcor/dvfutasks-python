import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))
def logistic_func(theta: np.ndarray, x: np.ndarray) -> float:
    return sig(np.sum(theta*x))
def logistic_func_all(theta: np.ndarray, X: np.ndarray) -> np.ndarray:
    return sig(np.dot(X, theta))
    
def cross_entropy_loss(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
    cel = np.sum(theta*X, axis=1)
    return np.sum(np.log(1 + np.exp(-y*cel)))/y.shape[0]
def grad_cross_entropy_loss(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    gcel = np.sum(theta*X, axis=1)
    sigm = sig(-y*gcel)
    res_grad = np.sum(-y*X.transpose()*sigm, axis=1)/y.shape[0]
    return res_grad

# def sigmoid(x):
#     return 1/(1+np.exp(-x))

# def logistic_func(theta: np.ndarray, x: np.ndarray) -> float:
#     return sigmoid(np.sum(x*theta))

# def logistic_func_all(theta: np.ndarray, X: np.ndarray) -> np.ndarray:
#     return sigmoid(np.dot(X, theta))
    
# def cross_entropy_loss(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
#     sum = np.sum(X * theta, axis=1)
#     return np.sum(np.log(1 + np.exp(-y * sum)))/len(y)

# def grad_cross_entropy_loss(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> np.ndarray:
#     sum = np.sum(X * theta, axis=1)
#     sigma = sigmoid(-y * sum)
#     gradient = np.sum(-y * X.T * sigma, axis=1)
#     gradient /= len(y)
#     return gradient    
# def grad_cross_entropy_loss(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> np.ndarray:
#     prob = logistic_func_all(X) - y
#     return [prob * i for i in X]
theta   = np.array([1., 0])
x       = np.array([1., 4])
y       = np.array([1., 1, -1])
X       = np.array([[1, 6], [1, 10], [5, 1]])
print(X)
print(logistic_func(theta=theta, x=x))
print(logistic_func_all(theta=theta, X=X))
print(cross_entropy_loss(theta=theta, X=X, y=y))
print(grad_cross_entropy_loss(theta=theta, X=X, y=y))