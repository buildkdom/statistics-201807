import numpy as np

# 여러개의 입력신호 노드 x
# 입력신호 노드들로부터의 가중치들 w
def AND(x):
    np_x = np.array(x)
    np_w = np.array([0.7, 0.7])
    bias = -1;
    if np.sum(np_x*np_w) + bias >= 0:
        return str(list(x))+' = 1'
    else:
        return str(list(x))+' = 0'

print(AND([0,0]),
      AND([1,0]),
      AND([0,1]),
      AND([1,1]))

def NAND(x):
    np_x = np.array(x)
    np_w = np.array([-0.5, -0.5])
    bias = 0.7
    if np.sum(np_x*np_w) + bias >= 0:
        return str(list(x))+' = 1'
    else:
        return str(list(x))+' = 0'

print(NAND([0,0]),
      NAND([1,0]),
      NAND([0,1]),
      NAND([1,1]))
