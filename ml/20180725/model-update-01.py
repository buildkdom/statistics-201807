import os
from keras.callbacks import ModelCheckpoint
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

path_model = './model/{epoch:02d}-{val_loss:.4f}.hdf5'

# keras를 이용해서 특정 값을 모니터하도록 지정할 수 있다.
checkpointer = ModelCheckpoint(filepath=path_model,
                               monitor='val_loss',
                               verbose=1)

