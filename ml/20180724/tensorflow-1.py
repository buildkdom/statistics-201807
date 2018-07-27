import tensorflow as tf
#
# Tensorflow's big two step:
# (1) graph building
# (2) graph execution
#

#
# (1) graph building
#
hello = tf.constant("Hello tensorflow!")
print (hello)

a = tf.constant(10)
b = tf.constant(33)
c = tf.add(a, b)
print (c)

#
# (2) graph execution
#
sess = tf.Session()
print (str(sess.run(hello), encoding='utf-8'))
print (sess.run([a, b, c]))
sess.close()