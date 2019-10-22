# Created by Albus Percival Wulfric Brain Dumbledore
# Date: 8/9/2019
# Time: 16:49

import Plugins.geo_ip as geo
import Plugins.news as news
import Plugins.quote as quote
import Plugins.weather as weather
import Posts.challenge_one as c1
import Posts.challenge_three as c3
import Posts.challenge_two as c2
from flask import Flask, render_template, request, send_file

logging.basicConfig(filename='API.log', level=logging.DEBUG,
                    format='%(name)s -- %(levelname)s: %(asctime)s %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
gf = logging.getLogger('GF')
gen = logging.getLogger('GEN')

app = Flask(__name__)


###########################################################
################## Main Returns ###########################
###########################################################


@app.route("/")
def load_splash_page():
    return render_template("index.html")


@app.route('/api/geo_ip/', methods=['POST'])
def IP():
    IP_ADDR = request.form['IP']
    gen.info('Geo IP accessed by: ' + request.remote_addr)
    gen.info(request.remote_addr + ' ran GEO IP with the IP address: ' + IP_ADDR)
    return geo.main(IP_ADDR)


@app.route('/api/weather/', methods=['GET'])
def Weather():
    gen.info('Weather accessed by: ' + request.remote_addr)
    return weather.main()


@app.route('/api/news/', methods=['GET'])
def News():
    gen.info('News accessed by: ' + request.remote_addr)
    return news.main()


@app.route('/api/quote/', methods=['GET'])
def Quote():
    QoD = dict()
    QoD['Quote'], QoD['Author'] = quote.main()
    gen.info('Quote accessed by: ' + request.remote_addr)
    return QoD


###########################################################
################## File Returns ###########################
###########################################################


@app.route('/images/hogwarts.jpg')
def send_hogwarts():
    return send_file('./templates/images/hogwarts.jpg')


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
def return_c1_page():
    """
    The Grey Fellows Induction Challenge 1 Page
    :return:
    """
    return render_template("challenge_1.html")


@app.route('/lvpalS7qqDL9W')
def return_c2_page():
    """
    The Grey Fellows Induction Challenge 2 Page
    :return:
    """
    return render_template("challenge_2.html")


@app.route('/iUhS5m1Nap7vU')
def return_c3_page():
    """
    The Grey Fellows Induction Challenge 3 Page
    :return:
    """
    return render_template("challenge_3.html")


@app.route('/api/0EHEOgBABoeLR', methods=['POST'])
def check_c1():
    gf.info(request.form['ID'] + ' at IP address: ' + request.remote_addr + ' ran a C1 check with the flag: ' +
            request.form['Flag'])
    return c1.check_flag(request.form['Flag'])


@app.route('/api/W4qu75hmCXVJE', methods=['POST'])
def check_c2():
    gf.info(request.form['ID'] + ' at IP address: ' + request.remote_addr + ' ran a C2 check with the flag: ' +
            request.form['Flag'])
    return c2.check_flag(request.form['Flag'])


@app.route('/api/4dhSX6b839wJr', methods=['POST'])
def check_c3():
    gf.info(request.form['ID'] + ' at IP address: ' + request.remote_addr + ' ran a C3 check with the flag: ' +
            request.form['Flag'])
    return c3.check_flag(request.form['Flag'])




if __name__ == "__main__":
    app.run()
