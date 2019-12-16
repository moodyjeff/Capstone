# Capstone - Flower Image Classification

This repository is work performed in creating a classifier that can classify images of flowers using transfer learning. the work was performed for a capstone project for brainstation data science program. 

Based on initial research it appears that classifying images using convolutional neural networks have performed very well at this task and have been able to achieve a high level of accuracy in classifying basic images. 

I performed different iterations of the neural networks including a neural network built from the ground up and finally a convolutional neural network using transfer learning. I found the VGG16 model to be the most successful for my classification problem with some additional dense layers added on. 

As a key component of my project I wanted to be able to make an interface that made the model operational for testing for the purposes of a third party, non-technical person. This stem-to-stern approach was important for me in fully seeing the model actually able to be used in production. This involed saving the model as an H5 file and creating a website which could interact with a flask web service via http requests. 

# Dataset and exploratory

The dataset I used was a repository of 4242 flower images in the categories, daisy, dandelion, rose, sunflower and tulip. 

I obtained the dataset from Kaggle Flowers Recognition and it can be found here: https://www.kaggle.com/alxmamaev/flowers-recognition

I performed some exploratory analysis of the dataset in order to get counts of the individual classes as well as to take a look at what the images actually looked l ike. 

EDA file name: 'exploratory_analysis'

# AWS 

Early on in building my models I realized that the time to run the models was significant, approxmating 7 hours in some cases. In order to improve upon time to train I utilitzed amazon web services, in particular amazon sagemaker as the preset environments that included python and tensorflow made setup very fast and efficient. 

# Models

In completing the following project I used 3 different model architectures. I began with a untrained model that did not involve transfer learning. I found that this model had reasonable test to train data results, however it did not achieve very good accuracy with 68% accuracy on the test data. Though not terrible results for a very basic mode I felt that it was possible to do better. In using the mobilenet model weights and making those layers untrainable I saw a strong increase in accuracy to 83% however the model was significantly overfit with approximately 98% on the training data. I likely could have improved upon this by playing with the additional dense layers that I added to the model, however when putting this model on aws sagemaker I had some problems importing the mobilenet framework and as such decided to try using the VGG16 model which has had success in image recognition and is generally a series of convolutional layers followed by 1 pooling layer 5 times. To this I added 3 dense trainable dense layers including the final layer with an output of 5 classes. In this model I saw a test data accuracy of 85% and no significant overfitting with train set accuracy of 88%. 

File names: 

The code for the above mentione models can be found in 3 seperate jupyter notebooks with the following names:

ground-up model: flowers_groundup_nn.ipynb

mobile-net model: flowers_mobilenet.ipynb

Vgg15 model: flowers_vgg.ipynb

# Web App and Flask

In order to display test my model with real images I create an html page and utilized javascript and css. In addition I created a flask web service in order to send images taken in by my webpage through my trained model.

File breakdown: All files related to the webpage an web service are found in the flask folder.

in flask/static folder there is a file 'prediction_webpage.html' which is the html page and front end of the web application which is able to receive images. It interacts to the file 'flask/predict/app4.py' by sending http post request with an copy of the encoded image that was received and is then processed by the python script to decode the image, process it and run it through the h5 model in order to obtain the model predictions which are then served back to the webpage as a json file as the response to the post request. 

some of the resources I used in creating the website are as follows: 


Webpage background image: https://www.google.com/search?biw=1280&bih=565&tbm=isch&sxsrf=ACYBGNSXKEa5SX6ttPQMHPwWZ7gWe02oqA%3A1575825520961&sa=1&ei=cDDtXd6XOo7QsAXgzZzYAQ&q=plants+background&oq=plants+background&gs_l=img.3..0i67j0i10l9.21178.22083..22153...0.0..0.299.1085.0j5j2......0....1..gws-wiz-img.......0j0i7i30j0i7i10i30.k_OQcrcGnEo&ved=0ahUKEwjej57Dx6bmAhUOKKwKHeAmBxsQ4dUDCAc&uact=5#imgrc=FAsNwQib9fnlqM:
Flask request and html: https://www.youtube.com/watch?v=INaX55V1zpY&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL&index=14
Javascript webpage: https://www.youtube.com/watch?v=RkmfXz304ck&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL&index=24
CSS:https://www.w3schools.com/howto/howto_css_hero_image.asp
CSS:https://www.w3schools.com/html/html_layout.asp


# Other tools 

In the performance of the above tasks I sought to utilize some tools learned throughout the course to improve efficiency of certain tasks. For the most part these are functions that I created in a seperate python script that could be called upon when necessary.

These functions are found in the file custom_function_tools.py

1. folder_to_train_test_split - The photo data was provided to me in a format that included folders for each of the five classes of images and all the images of a given class in said folder. In order to split out some images for test purposes I created a function that would take some inputs including test split % and would create new directories for train and test with 5 folders representing the classes in each directory. 

2. unzip_file - In importing the data files into amazon sagemaker they were in a zip file. as a result I created a unzip function in order to quickly unzip the folder when it was added to the sagemaker file directory.


# Results

My best model obtained results of 85% on unseen images. This is a strong result based on the speed in which the model can be created and the obvious similarities in the dataset. There are definitely some images that it would be very tough for even humans to indentify. This is not unexpected as the image dataset was scraped from the web and did include instances where it is possible that labels were wrong or simply that the environment in which the photograph occurred had a other feature within it. I would like to continue this project by creating similar models with different datasets including a larger number of flowers and also funghi. 
