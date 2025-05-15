import numpy as np

def calculate(list):

    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape((3, 3))

    def to_list(x):
        return x.tolist() if hasattr(x, "tolist") else x.item()
    
    calculations = {}
    metrics = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    for name, func in metrics.items():

        col = func(matrix, axis=0)
        row = func(matrix, axis=1)
        flat = func(matrix)
        
        calculations[name] = [
            to_list(col),
            to_list(row),
            to_list(flat)
        ]

    return calculations