# define imports
from flask import Flask, request, render_template
import pickle
from numpy import array2string

# define the path to the pickled model
model_path = "models/rf-model.pkl"

# unpickle the random forest model
with open(model_path, "rb") as file:
    unpickled_rf = pickle.load(file)

# list with flower classews
flower_class=['setosa', 'versicolor', 'virginica']

# define the app
app = Flask(__name__)



#if a form is submitted
@app.route("/", methods=["GET", "POST"])
def predict_form():

    #if a form is submitted
    if request.method=='POST':
        
        flower=[]
        flower.append(request.form.get('petal_length'))
        flower.append(request.form.get('petal_width'))
        flower.append(request.form.get('sepal_length'))
        flower.append(request.form.get('sepal_width'))

        # pred= array2string(unpickled_rf.predict([flower]))
        pred= unpickled_rf.predict([flower])
        prediction=flower_class[pred[0]]

    else:
        prediction=''


    return render_template('website.html', output = prediction) #render_template("file.HTML", name_in_HTML = name_in_Python)
        
# if input is entered into browser
# use decorator to define the /score input method and define the predict function
@app.route("/score", methods=["POST", "GET"])
def predict_browser():
    # create list and append inputs
    flower = []
    flower.append(request.args.get("petal_length"))
    flower.append(request.args.get("petal_width"))
    flower.append(request.args.get("sepal_length"))
    flower.append(request.args.get("sepal_width"))

    pred= unpickled_rf.predict([flower])
    prediction=flower_class[pred[0]]

    # return the prediction
    return prediction #array2string(unpickled_rf.predict([flower]))


# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")
    # app.run(debug=True)