import numpy as np

def calculate(lst):
    # Check if the list contains exactly 9 elements
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers")
    
    # Convert the list into a 3 x 3 Numpy array
    arr = np.array(lst).reshape(3, 3)
    
    # Helper function to convert numpy outputs to standard python lists
    def get_stat_list(stat_func):
        return [
            stat_func(arr, axis=0).tolist(),
            stat_func(arr, axis=1).tolist(),
            stat_func(arr)
        ]

    # Construct and return the dictionary
    result = {
        'mean': get_stat_list(np.mean),
        'variance': get_stat_list(np.var),
        'standard deviation': get_stat_list(np.std),
        'max': get_stat_list(np.max),
        'min': get_stat_list(np.min),
        'sum': get_stat_list(np.sum)
    }
    
    return result
