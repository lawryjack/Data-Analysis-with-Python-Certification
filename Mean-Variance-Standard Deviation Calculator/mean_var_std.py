import numpy as np

def calculate(list1):

    #Error handling (list must be 9 elements)
    if len(list1) != 9:
        raise ValueError("List must contain nine numbers.");

    x = np.array(list1);
    array1 = np.split(x, 3);
    array1 = np.array(array1);

    #Calculating all math functions

    #Mean
    meanTotal = [list(np.mean(array1, axis=0)), list(np.mean(array1, axis=1)), np.mean(array1)];

    #Variance
    varTotal = [list(np.var(array1, axis=0)), list(np.var(array1, axis=1)), np.var(array1)];

    #Standard Deviation
    stdTotal = [list(np.std(array1, axis=0)), list(np.std(array1, axis=1)), np.std(array1)];

    #Max
    maxTotal = [list(np.max(array1, axis=0)), list(np.max(array1, axis=1)), np.max(array1)];

    #Min
    minTotal = [list(np.min(array1, axis=0)), list(np.min(array1, axis=1)), np.min(array1)];

    #Sum
    sumTotal = [list(np.sum(array1, axis=0)), list(np.sum(array1, axis=1)), np.sum(array1)];

    calculations = {"mean": meanTotal, "variance": varTotal, "standard deviation": stdTotal, "max": maxTotal, "min": minTotal, "sum": sumTotal};

    return calculations;
