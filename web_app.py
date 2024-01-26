from flask import Flask, render_template, request
from time import sleep
import speed_100M
import speed_1G
import speed_get
import set_duplicate_ip
import delete_duplicate_ip
app = Flask(__name__)
    

@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('speed_1G') == 'speed_1G':
            speed_1G.main()
            print("Changed to eth1/5 -> 1Gbit!")
            return render_template('index.html', value1="Changed to eth1/5 -> 1Gbit!")
        elif  request.form.get('speed_100M') == 'speed_100M':
            speed_100M.main()
            print("Changed to eth1/5 -> 100M!")
            return render_template('index.html', value1="Changed to eth1/5 -> 100Mbit!")
        elif  request.form.get('What is current speed?') == 'What is current speed?':
            current = speed_get.main()
            return render_template('index.html', value2="Current speed is -> " + current)
        elif request.form.get('Set Duplicate IP') == 'Set Duplicate IP':
            set_duplicate_ip.main()
            return render_template('index.html', value3="Duplicate IP is created")
        elif request.form.get('Delete Duplicate IP') == 'Delete Duplicate IP':
            delete_duplicate_ip.main()
            return render_template('index.html', value3="Deleted Duplicate IP")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999', debug=True)
