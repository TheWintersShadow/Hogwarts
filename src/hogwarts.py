# Created by Albus Percival Wulfric Brain Dumbledore
# Date: 8/9/2019
# Time: 16:49

import logging

import Plugins.geo_ip as geo
import Plugins.news as news
import Plugins.quote as quote
import Plugins.weather as weather
import Posts.challenge_four as c4
import Posts.challenge_one as c1
import Posts.challenge_three as c3
import Posts.challenge_two as c2
from flask import Flask, render_template, request, send_file

logging.basicConfig(filename='API.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')

app = Flask(__name__)


###########################################################
################## Main Returns ###########################
###########################################################


@app.route("/")
def load_index():
    return render_template("index.html")


@app.route("/splash_page")
def load_splash_page():
    return render_template("Splash_Page.html")


@app.route('/api/geo_ip/', methods=['POST'])
def IP():
    IP_ADDR = request.json['IP']
    logging.info('Geo IP accessed by: ' + request.remote_addr)
    logging.info(request.remote_addr + ' ran GEO IP with the IP address: ' + IP_ADDR)
    return geo.main(IP_ADDR)


@app.route('/api/weather/', methods=['GET'])
def Weather():
    logging.info('Weather accessed by: ' + request.remote_addr)
    return weather.main()


@app.route('/api/news/', methods=['GET'])
def News():
    logging.info('News accessed by: ' + request.remote_addr)
    return news.main()


@app.route('/api/quote/', methods=['GET'])
def Quote():
    QoD = dict()
    QoD['Quote'], QoD['Author'] = quote.main()
    logging.info('Quote accessed by: ' + request.remote_addr)
    return QoD


###########################################################
################## File Returns ###########################
###########################################################


@app.route('/images/hogwarts.jpg')
def send_hogwarts():
    return send_file('./templates/images/hogwarts.jpg')


@app.route('/javascript/plugins.js')
def send_plugins():
    return send_file('./templates/javascript/plugins.js')


@app.route('/images/hogwarts-logo.png')
def send_hogwarts_logo():
    return send_file('./templates/images/hogwarts-logo.png')


@app.route('/challengeItems/stegasour.png')
def send_stegasour():
    return send_file('./templates/challengeItems/stegasour.png')


@app.route('/challengeItems/challenge1.txt')
def send_text_file():
    return send_file('./templates/challengeItems/challenge1.txt')


###########################################################
################## GF Returns #############################
###########################################################


@app.route('/fpiS3GQz4Zx99')
def return_gf_page():
    """
    The Grey Fellows Induction Home Page
    :return:
    """
    return render_template("gf_page.html")


@app.route('/api/0EHEOgBABoeLR', methods=['POST'])
def check_c1():
    logging.info(request.form['UniqueID'] + ' ran a C1 check with the flag: ' + request.form['Flag'])
    return c1.check_flag(request.form['Flag'])


@app.route('/api/W4qu75hmCXVJE', methods=['POST'])
def check_c2():
    logging.info(request.form['UniqueID'] + ' ran a C2 check with the flag: ' + request.form['Flag'])
    return c2.check_flag(request.form['Flag'])


@app.route('/api/4dhSX6b839wJr', methods=['POST'])
def check_c3():
    logging.info(request.form['UniqueID'] + ' ran a C3 check with the flag: ' + request.form['Flag'])
    return c3.check_flag(request.form['Flag'])


@app.route('/api/GDloAXlt0jsJZ', methods=['POST'])
def check_c4():
    logging.info(request.form['UniqueID'] + ' ran a C4 check with the flag: ' + request.form['Flag'])
    return c4.check_flag(request.form['Flag'])


if __name__ == "__main__":
    app.run()
