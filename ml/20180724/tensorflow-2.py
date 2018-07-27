import tensorflow as tf

data = [[2, 81], [4, 93], [6,91], [8, 97]]
x_data = [xrow[0] for xrow in data]
y_data = [yrow[0] for yrow in data]
learning_rt = 0.1

a = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))

y = a * x_data + b

rmse = tf.sqrt(tf.reduce_mean(tf.square ( y - y_data )))
gradient_decent = tf.train.GradientDescentOptimizer(learning_rt).minimize(rmse)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        sess.run(gradient_decent)
        if step % 100 == 0:
            print ("Epoch: %.f, RMSE=%.04f, 기울기 = %.4f, 절편 b = %.4f" %
                   (step, sess.run(rmse), sess.run(a), sess.run(b)))