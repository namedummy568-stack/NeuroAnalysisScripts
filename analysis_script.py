def process_neural_data(data):
    return data * 2

def filter_data(data):
    # This function filters neural data based on a threshold.
    # It returns a new list containing only the data points greater than 0.5.
    # This helps in removing noise or irrelevant low-amplitude signals.
    return [d for d in data if d > 0.5]
