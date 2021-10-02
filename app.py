import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model7.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    battery = request.form['battery_power']
    fc = request.form['fc']
    int_memory= request.form['int_memory']
    pc = request.form['pc']
    ram = request.form['ram']
    blue = request.form['blue']
    clock_speed = request.form['clock_speed']
    dual_sim = request.form['dual_sim']
    m_dep = request.form['m_dep']
    network = request.form['network']
    mobile_wt = request.form['mobile_wt']
    n_cores = request.form['n_cores']
    px_height = request.form['pixel_height']
    px_width = request.form['pixel_width']
    sc_h = request.form['sc_h']
    sc_w = request.form['sc_w']
    talk_time = request.form['talk_time']
    touch_screen = request.form['touch_screen']
    wifi = request.form['wifi']

    four_g = 0
    three_g = 0

    if network == '3G':
        three_g = 1
    else:
        four_g = 1
    
    prediction = loadedModel.predict([[battery, blue, clock_speed, dual_sim, fc, four_g,
        int_memory, m_dep, mobile_wt,n_cores, pc, px_height,
        px_width, ram, sc_h, sc_w, talk_time, three_g,
        touch_screen, wifi]])[0]
    

    if prediction == 0:
        prediction = "0 - 5000"
    elif prediction == 1:
        prediction = "5000 - 20000"
    elif prediction == 2:
        prediction = "0 - 50000"
    else:
        prediction = "above 50000"


    return render_template('home.html', output=prediction)
    
#Main function
if __name__ == '__main__':
    app.run(debug=True)