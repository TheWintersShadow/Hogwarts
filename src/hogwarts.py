# Created by Albus Wulfric Brain Dumbledore
# Date: 8/9/2019
# Time: 16:49

import Plugins.geo_ip as geo
import Plugins.news as news
import Plugins.quote as quote
import Plugins.weather as weather
import Posts.challenge_four as c4
import Posts.challenge_one as c1
import Posts.challenge_three as c3
import Posts.challenge_two as c2
from flask import Flask, render_template, request, send_file

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
    return geo.main(IP_ADDR)


@app.route('/api/weather/', methods=['GET'])
def Weather():
    return weather.main()


@app.route('/api/news/', methods=['GET'])
def News():
    return news.main()


@app.route('/api/quote/', methods=['GET'])
def Quote():
    QoD = dict()
    QoD['Quote'], QoD['Author'] = quote.main()
    return QoD


@app.route('/images/hogwarts.jpg')
def send_hogwarts():
    return send_file('./templates/images/hogwarts.jpg')


@app.route('/images/hogwarts-logo.png')
def send_hogwarts_logo():
    return send_file('./templates/images/hogwarts-logo.png')


@app.route('/challengeItems/stegasour.jpg')
def send_stegasour():
    return send_file('./templates/challengeItems/stegasour.jpg')


@app.route('/challengeItems/challenge1.txt')
def send_text_file():
    return send_file('./templates/challengeItems/challenge1.txt')


###########################################################
################## IMDb Returns ###########################
###########################################################


@app.route('/imdb/name.basics.tsv')
def send_name():
    return send_file('./IMDb/DataSets/name.basics.tsv')


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
    return c1.check_flag(request.form['Flag'])


@app.route('/api/W4qu75hmCXVJE', methods=['POST'])
def check_c2():
    return c2.check_flag(request.form['Flag'])


@app.route('/api/4dhSX6b839wJr', methods=['POST'])
def check_c3():
    return c3.check_flag(request.form['Flag'])


@app.route('/api/GDloAXlt0jsJZ', methods=['POST'])
def check_c4():
    return c4.check_flag(request.form['Flag'])


if __name__ == "__main__":
    app.run()
