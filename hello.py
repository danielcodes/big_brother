from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def home():
    # 2 goals
    # get the tooltip to display a title, image
    # pull in data from csv file

    # grab data
    # data = [
            # {'timestamp' : '06-10-17', 'ip_address' : '138.34.42.10', 'source_url' : 'google.com', 'current_url' : 'violence.com', 'lattitude' : '14', 'longitude' : '139'},
            # {'timestamp' : '06-10-17', 'ip_address' : '138.34.42.10', 'source_url' : 'google.com', 'current_url' : 'violence.com', 'lattitude' : '14', 'longitude' : '139'},
            # {'timestamp' : '06-10-17', 'ip_address' : '138.34.42.10', 'source_url' : 'google.com', 'current_url' : 'violence.com', 'lattitude' : '14', 'longitude' : '139'},
            # {'timestamp' : '06-10-17', 'ip_address' : '138.34.42.10', 'source_url' : 'google.com', 'current_url' : 'violence.com', 'lattitude' : '14', 'longitude' : '139'},
           # ]
    
    data = []
    # pass data to template
    with open('data/janak_data.csv', 'rU') as f:
        reader = csv.reader(f)
        header = reader.next()
        # print header
        for row in reader:
            formatted = dict(zip(header, row))
            data.append(formatted)
            # print formatted

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)


