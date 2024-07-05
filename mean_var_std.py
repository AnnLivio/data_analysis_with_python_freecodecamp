import numpy as np

def calculate(list):
    try:
        arr = np.array(list).reshape(3,3)
        calculations = {'mean':[[],[]], 'variance':[[],[]], 'standard deviation':[[],[]], 'max':[[],[]], 'min':[[],[]], 'sum':[[],[]]}

    # calculations axis1 and axis2
        for i in range(3):
            calculations['mean'][0].append(np.mean(arr[:,i]))
            calculations['mean'][1].append(np.mean(arr[i,:]))
            calculations['variance'][0].append(np.var(arr[:,i]))
            calculations['variance'][1].append(np.var(arr[i,:]))
            calculations['standard deviation'][0].append(np.std(arr[:,i]))
            calculations['standard deviation'][1].append(np.std(arr[i,:]))
            calculations['max'][0].append(np.max(arr[:,i]))
            calculations['max'][1].append(np.max(arr[i,:]))
            calculations['min'][0].append(np.min(arr[:,i]))
            calculations['min'][1].append(np.min(arr[i,:]))
            calculations['sum'][0].append(np.sum(arr[:,i]))
            calculations['sum'][1].append(np.sum(arr[i,:]))

        calculations['mean'].append(np.mean(arr))
        calculations['variance'].append(np.var(arr))
        calculations['standard deviation'].append(np.std(arr))
        calculations['max'].append(np.max(np.array(calculations['max'])))
        calculations['min'].append(np.min(np.array(calculations['min'])))
        calculations['sum'].append(np.sum(arr))
    except ValueError:
        return "List must contain nine numbers."
    
    return calculations
