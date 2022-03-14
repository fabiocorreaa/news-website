from flask import Blueprint, render_template
from .functions.scraping_functions import scrape_apnews, scrape_bbc, scrape_economist, scrape_g1


views = Blueprint('views', __name__)

@views.route('/', methods=['GET',])
def home():
    return render_template('home.html', sap=scrape_apnews(), sbb=scrape_bbc(), ste=scrape_economist(), s1=scrape_g1(), list=list)


@views.route('/apnews')
def apnews():
    return render_template('apnews.html', news=scrape_apnews(), enumerate=enumerate, zip=zip, list=list)


@views.route('/g1')
def g1():
    return render_template('g1.html', news=scrape_g1(), enumerate=enumerate, zip=zip, list=list)


@views.route('/bbc')
def bbc():
    return render_template('bbc.html', news=scrape_bbc(), enumerate=enumerate, zip=zip, list=list)


@views.route('/the-economist')
def the_economist():
    return render_template('the_economist.html', news=scrape_economist(), enumerate=enumerate, zip=zip, list=list)

