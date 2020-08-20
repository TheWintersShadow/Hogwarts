# Created by Albus Percival Wulfric Brain Dumbledore
# Date: 8/9/2019
# Time: 16:49

import Plugins.geo_ip as geo
import Plugins.news as news
import Plugins.quote as quote
import Plugins.weather as weather
import logging
from flask import Flask, jsonify, render_template, request, send_file

logging.basicConfig(filename='/var/www/Hogwarts/src/API.log', level=logging.DEBUG,
                    format='%(name)s -- %(levelname)s: %(asctime)s %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')


logging.basicConfig(filename='/var/www/Hogwarts/src/API.log', level=logging.INFO, format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')

app = Flask(__name__)


###########################################################
################## Main Returns ###########################
###########################################################


@app.route("/")
def load_index():
    return render_template("index.html")


@app.route('/api/geo_ip/', methods=['POST'])
def IP():
    IP_ADDR = request.json['IP']
    logging.info('Geo IP accessed by: ' + request.remote_addr)
    logging.info(request.remote_addr + ' ran GEO IP with the IP address: ' + IP_ADDR)
    return jsonify(geo.main(IP_ADDR))


@app.route('/api/weather/', methods=['GET'])
def Weather():
    logging.info('Weather accessed by: ' + request.remote_addr)
    return jsonify(weather.main())


@app.route('/api/news/', methods=['GET'])
def News():
    logging.info('News accessed by: ' + request.remote_addr)
    return jsonify(news.main())


@app.route('/api/quote/', methods=['GET'])
def Quote():
    QoD = dict()
    QoD['Quote'], QoD['Author'] = quote.main()
    logging.info('Quote accessed by: ' + request.remote_addr)
    return jsonify(QoD)


###########################################################
################## File Returns ###########################
###########################################################


################## Website Files ##########################
@app.route('/images/bitwarden.png')
def send_bit():
    return send_file('./templates/images/bitwarden.png')


@app.route('/images/gitlab.png')
def send_git():
    return send_file('./templates/images/gitlab.png')


@app.route('/images/kibana.png')
def send_kibana():
    return send_file('./templates/images/kibana.png')


@app.route('/images/pihole.png')
def send_pihole():
    return send_file('./templates/images/pihole.png')


@app.route('/images/wiki.png')
def send_wiki():
    return send_file('./templates/images/wiki.png')


@app.route('/javascript/plugins.js')
def send_plugins():
    return send_file('./templates/javascript/plugins.js')


@app.route('/css/basic.css')
def send_css():
    return send_file('./templates/css/basic.css')


################## Data Science Files #####################
@app.route('/files/enron/emails.csv')
def return_enron_emails():
    return send_file('./files/enron/emails.csv')



if __name__ == "__main__":
    app.run()
