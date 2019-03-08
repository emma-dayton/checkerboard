from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # renders 8 by 8 square of red and black
def landing():
    return render_template('index.html', num1=8, num2=8, color1="red",color2="black")


@app.route('/<num1>') # renders n by n square of red and black
def custom_square(num1):
    num1 = int(num1)
    return render_template('index.html', num1=num1, num2=num1, color1="red",color2="black")

@app.route('/<num1>/<num2>') # renders n by m grid of red and black
def custom_size(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return render_template('index.html', num1=num1, num2=num2, color1="red",color2="black")


@app.route('/<num1>/<num2>/<color1>') # renders n by m grid of custom color and black
def single_color_change(num1, num2, color1):
    num1 = int(num1)
    num2 = int(num2)
    color1 = str(color1)
    return render_template('index.html', num1=num1, num2=num2, color1=color1,color2="black")

@app.route('/<num1>/<num2>/<color1>/<color2>') #renders n by m grid of 2 custom colors
def color_change(num1, num2, color1, color2):
    num1 = int(num1)
    num2 = int(num2)
    color1 = str(color1)
    color2 = str(color2)
    return render_template('index.html', num1=num1, num2=num2, color1=color1,color2=color2)





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
