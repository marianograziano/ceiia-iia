import numpy as np

def precision (ver,predi):
    mascara_tp = (ver == 1) & (predi == 1)
    mascara_fp = (ver == 0) & (predi == 0)
    mascara_fn = (ver == 1) & (predi == 0)
    mascara_fp = (ver == 0) & (predi == 1)

    tp = mascara_tp.sum()
    fp = mascara_fp.sum()
    fn = mascara_fn.sum()
    fp = mascara_fp.sum()
    
    return (tp / (tp + fp))

def recall (ver,predi):
    mascara_tp = (ver == 1) & (predi == 1)
    mascara_fp = (ver == 0) & (predi == 0)
    mascara_fn = (ver == 1) & (predi == 0)
    mascara_fp = (ver == 0) & (predi == 1)

    tp = mascara_tp.sum()
    fp = mascara_fp.sum()
    fn = mascara_fn.sum()
    fp = mascara_fp.sum()
    
    return (tp / (tp + fn))

def accuracy (ver,predi):
    mascara_tp = (ver == 1) & (predi == 1)
    mascara_fp = (ver == 0) & (predi == 0)
    mascara_fn = (ver == 1) & (predi == 0)
    mascara_fp = (ver == 0) & (predi == 1)

    tp = mascara_tp.sum()
    fp = mascara_fp.sum()
    fn = mascara_fn.sum()
    fp = mascara_fp.sum()
    
    return ((tp + tn) / (tp + tn + fp + fn))

truth = np.array([1,1,0,1,1,1,0,0,0,1])
prediction = np.array([1,1,1,1,0,0,1,1,0,0])

print(precision(truth,prediction))
print(recall(truth,prediction))
print(accuracy(truth,prediction))
