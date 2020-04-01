import base64
import numpy as np
import io
from PIL import Image
import tensorflow.keras
from tensorflow.keras import backend as k
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from flask import request
from flask import jsonify
from flask import Flask

# set app variable for flask
app = Flask(__name__)

# define a function to get model
def get_model():
    # set as global variable
    global model
    # use keras load model and load h5 pretrained model
    model = load_model('model.h5')
    # create global variable to troubleshoot issues in functionality
    global graph
    graph = tensorflow.get_default_graph()
    # print out to confirm function has run
    print('* Model Loaded')

# define function to receive image and target size to prepare for the model
def preprocess_image(image,target_size):
    # convert image to rgb if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # resize image using function target size
    image = image.resize(target_size)
    # set image as arrage
    image = img_to_array(image)
    # add 4th dimention as is required by the model
    image = np.expand_dims(image,axis=0)


    return image
# print upon running script
print(' * Loading Keras Model....')
# call get model function so that model is loaded
get_model()

# assign url for post request
@app.route('/predict2', methods=['POST'])

# create function to receive and process post request by web service
def predict2():
    # create message variable as the post request
    message = request.get_json(force=True)
    # obtain the image element from the json request
    encoded = message['image']
    # decode the image variable from base64 encoding
    decoded = base64.b64decode(encoded)
    # open decoded image
    image = Image.open(io.BytesIO(decoded))
    # process image using above defined function
    processed_image = preprocess_image(image, target_size=(224,224))
    # use above defined variable
    with graph.as_default():
        # create prediction variable using processed image in model.predict
        prediction = model.predict(processed_image).tolist()
        Create key_pairs dictionary
        key_pairs={0: 'Daisy', 1: 'Dandelion', 2: 'Rose', 3: 'Sunflower', 4: 'Tulip'}
        # create top prediction variable using argmax function
        pred_flower = key_pairs[np.argmax(prediction)]
        # define the resonse
        response = {
            # include the top prediction as max
            'prediction': {
            'max': (f"You've got yourself a {pred_flower}!"),
            # include the prediction %'s of all classes'
            'daisy': prediction[0][0],
            'dandelion': prediction[0][1],
            'rose': prediction[0][2],
            'sunflower': prediction[0][3],
            'tulip': prediction[0][4]
            },
            # include a dictionary of desired display names in the response
            'name': {
            'daisy':'Daisy: ',
            'dandelion':'Dandelion: ',
            'rose':'Rose: ',
            'sunflower':'Sunflower: ',
            'tulip':'Tulip: '
            }
    }
    # return the response
    return jsonify(response)
