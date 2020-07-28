from __future__ import print_function

import os
import os.path
import matplotlib.image as mpimg
import tensorflow as tf
import argparse


parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument("--fn_root", help="Name of root file path", required = True, type=str)
parser.add_argument("--partition_fn", help="Partition file path", required = True, type=str)
parser.add_argument("--number", help="Number of files", required = True, type=str)
args = parser.parse_args()


def main():
    """Main converter function."""
    if not os.path.exists('tfrecs'):
        os.makedirs('tfrecs')

    # Celeb A
    with open(args.partition_fn, "r") as infile:
        img_fn_list = infile.readlines()

    attributes_name = img_fn_list[1].split()

    img_fn_list = img_fn_list[2:]
    img_fn_list = [elem.strip().split() for elem in img_fn_list]

    fn_root = argd.fn_root
    num_examples = len(img_fn_list)
    num_exaple_per_file = len(img_fn_list) // int(args.number)
    i = 0
    file_out = "tfrecord_{}.tfrec".format(i)
    print(file_out)
    writer = tf.io.TFRecordWriter("tfrecs/" + file_out)

    for example_idx, img_fn in enumerate(img_fn_list):
        if example_idx % 1000 == 0:
            print(example_idx, "/", num_examples)
        if example_idx != 0 and example_idx % num_exaple_per_file == 0:
            writer.close()
            i += 1
            file_out = "tfrecord_{}.tfrec".format(i)
            print(file_out)
            writer = tf.io.TFRecordWriter("tfrecs/" + file_out)
        img_path = os.path.join(fn_root, img_fn[0])
        img_shape = mpimg.imread(img_path).shape
        filename = os.path.basename(img_path)

        # Read image data in terms of bytes
        with tf.io.gfile.GFile(img_path, 'rb') as fid:
            image_data = fid.read()

        image_attributes = img_fn[1:]

        for j in range(0, len(image_attributes)):
            image_attributes[j] = int(image_attributes[j])
            if image_attributes[j] < 1:
                image_attributes[j] = 0

        feature_dict = {
            'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_data])),
            'labels': tf.train.Feature(int64_list=tf.train.Int64List(value=image_attributes))
        }
        example = tf.train.Example(features=tf.train.Features(feature=feature_dict))

        writer.write(example.SerializeToString())

    names = str(attributes_name).strip('[]')

    writer = tf.io.TFRecordWriter("tfrecs/" + "attribute_list.tfrec")
    example = tf.train.Example(features=tf.train.Features(feature={
        'names': tf.train.Feature(bytes_list=tf.train.BytesList(value=[names.encode('utf-8')])),
    }))

    writer.write(example.SerializeToString())
    writer.close()


if __name__ == "__main__":
    main()