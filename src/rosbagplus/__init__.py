import rosbag
import tf

class SuperBag:
    def __init__(self, fn):
        self.bag = rosbag.Bag(fn)
        self.tf = tf.Transformer()
        self.x = self.bag.read_messages()

    def __iter__(self):
        return self    

    def next(self):
        abc = self.x.next()
        while abc[0]=='/tf':
            for transform in abc[1].transforms:
                self.tf.setTransform(transform)
            abc = self.x.next()
        return abc    
