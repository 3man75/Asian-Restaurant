from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)

def create_app():

    print(app)

    return returned_dict

@app.route("/")
def welcome():

    #images to be sent to the front page
    first_image = url_for('static', filename='komodo.jpg')
    second_image = url_for('static', filename='Da Teng Zhen Wei.jpeg')
    third_image = url_for('static', filename='Fuchai_Miami.jpg')
    fourth_image = url_for('static', filename='Hutong_Miami.jpg')
    fifth_image = url_for('static', filename='Yip_Doral.jpg')
    sixth_image = url_for('static', filename='Shima.jpeg')
    seventh_image = url_for('static', filename='Chow.jpeg')
    eighth_image = url_for('static', filename='Tanuki.jpeg')
    
    return render_template('home.html', komodo= first_image, Wei = second_image, Fuchai = third_image, Hutong = fourth_image
                           , Yip = fifth_image, Shima = sixth_image, Chow = seventh_image, Tanuki = eighth_image)

@app.route("/t")
def test():

    return render_template('example.html')

if __name__ == '__main__':

    app.run(host="0.0.0.0")
