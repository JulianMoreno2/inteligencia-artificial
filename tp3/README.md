# Convolutional neural network in TensorFlow and Keras

In this repository you can find out how to implement CNN in Tensorflow/Keras for multiclass classification.

## Dataset

Dataset used in this project is MNIST dataset. You can download it by using built-in TensorFlow functions. For more explanation open the .ipynb file.

## Install

### &nbsp;&nbsp;&nbsp; Supported Python version
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python version used in this project: 3.5+

### &nbsp;&nbsp;&nbsp; Libraries used

> *  [TensorFlow](http://tensorflow.org) 1.2.0
> *  [Numpy](http://www.numpy.org) 1.10.4
> *  [Time]()
> *  [tqdm](https://pypi.python.org/pypi/tqdm) 4.15.0

```console
user@user:~$ export PATH=~/anaconda3/bin:$PATH
user@user:~$ conda install -c conda-forge tensorflow
user@user:~$ conda install -c conda-forge tqdm
user@user:~$ conda install -c conda-forge scipy
```

### The following packages are needed

pip install sklearn
pip install pandas
pip install pandas-datareader
pip install matplotlib
pip install pillow
pip install requests
pip install h5py

## Code

The tensorflow version of CNN is inside **CNN-Keras-TensorFlow.ipynb**.

## Download Images for build custom Dataset

### Use app from https://github.com/hardikvasa/google-images-download
### Install -> $ pip install google_images_download
```console
googleimagesdownload --keywords "oak leaf" --no_numbering  --limit 50 --output_directory "train" --image_directory "oakleaf"
googleimagesdownload --keywords "olive leaf" --no_numbering  --limit 50 --output_directory "train" --image_directory "oliveleaf"
googleimagesdownload --keywords "salix leaf" --no_numbering  --limit 50 --output_directory "train" --image_directory "salixleaf"
```

## Run

To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).

After making sure you have that, you can run from a terminal or cmd next lines (Example  for Keras version):

`ipython notebook Keras_cnn.ipynb`

## References

- Introduction to Deep Learning [Link to Class 1](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class1_intro_python.ipynb)

- Github repository example [Link to Repository](https://github.com/lucko515/cnn-tensorflow-keras)

- Example 1: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
