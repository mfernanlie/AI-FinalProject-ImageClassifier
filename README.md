# Mineral Classifier

Mineral Classifier is an image classifier application for our Artificial Intelligence class at Binus International. The application
will identify a given image of mineral and classify its most likely category. The application will receive a certain dataset for training
before being able to identify any image. The dataset and category is fully customizable by the user but here we use 4 datasets of different
minerals which are Bauxite, Gypsum, Malachite and Amethyst. Each category contains 100 training images.

## Getting Started

This section will explains the pre-requisites and steps of installing the application on your computer and using it.

### Prerequisites

#### Docker

Docker is a container platform that provides a Linux or Windows Virtual Machine for both MacOS and Windows.
Docker is free to download and you can get yours on the link below.

```
https://www.docker.com/get-docker
```


#### Tensorflow

Tensoflow is an open-source software librabry developed and released by Google in 2015. Tensorflow provides library for various tasks and one of them including a machine learning applications like neural networks. 

We will be using Tensorflow Python API and since tensorflow are using calculation very extensively, it is suggested to set up an conda environement which will provide you the libraries that tensorflow are going to need, like Numpy. 
To establish conda environment, run the following command in order.

```
conda create --name TensorflowEnv biopython
```

```
source activate TensorFlowEnv
```

pip is a standard installation tool for conda environment, so we will use that. It's recommended to update your pip before installing tensorflow to avoid possible conflict during the installation.

```
pip install --upgrade pip
```

And then we are ready to install Tensorflow

```
pip install tensorflow
```


#### Fatkun

For our dataset, we are downloading it manually from google image search results. To help us with the tedious work, we are using a chrome extension called Fatkun to enable us to download all images that appears on google search first page. We will have to manually filter each image before downloading since we want to avoid bad dataset.

Fatkun extension for google chrome can be found on the link below

```
https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en
```


#### Inception Model

Inception model is a pre-trained Convolutional Neural Networks that we use for this project. It saves us from training the data over all the neural network layers for each new dataset. It was developed by Google and has been tested with over 100k images.

Inception model is available here

```
https://github.com/llSourcell/tensorflow_image_classifier
```


## Installation and Running process

The details regarding the installation of all pre-requisites and running the application is explained on a 3-minute video we have made.

```
https://drive.google.com/open?id=1QQTGaBs_7iZDUGBfzYdpc2Rkxugd1oYS
```

## Authors

* **Michael Fernanlie** - *1901530133*
* **Steven Muliamin** - *1901499280*

## Acknowledgments

The application is inspired by Siraj Raval work.
The details of his image classifier work can be found on the link below.

```
https://www.youtube.com/watch?v=QfNvhPx5Px8
```

