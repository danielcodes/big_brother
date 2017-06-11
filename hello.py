from flask import Flask, render_template, json
import csv
app = Flask(__name__)

# precompute values, want to group the rows with the same ip addresses and create a line chart
data = []
ip_addresses = {}

# pass data to template
with open('data/janak_data.csv', 'rU') as f:
    reader = csv.reader(f)
    header = reader.next()
    # print header
    
    # data format should be, {ip: data_row}
    # if seen for the first time, place it
    # otherwise add the object to the list

    for row in reader:
        formatted = dict(zip(header, row))
        if formatted['ip_address'] in ip_addresses:
            ip_addresses[formatted['ip_address']].append(formatted)
        else:
            ip_addresses[formatted['ip_address']] = [formatted]

        data.append(formatted)
        # print formatted

    print '\nPrinting ip address wit the grouped rows==============================================='
    print ip_addresses


@app.route("/")
def home():
    return render_template('index.html', ip_addresses=ip_addresses)

@app.route("/get_data")
def get_data():
    return json.jsonify(ip_addresses)

if __name__ == "__main__":
    app.run(debug=True)


