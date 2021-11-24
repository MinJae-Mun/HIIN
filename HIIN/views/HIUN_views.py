from flask import Blueprint, jsonify

from HIIN.models import HIUN_corona, HIUN_generalno, HIUN_studentsno, HIUN_contest



bp = Blueprint('HIUN', __name__, url_prefix='/HIUN')


@bp.route('/corona/')
def corona_list():
    length = len(HIUN_corona.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HIUN_corona.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/generalno/')
def generalno_list():
    length = len(HIUN_generalno.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HIUN_generalno.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/studentsno/')
def studentsno_list():
    length = len(HIUN_studentsno.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HIUN_studentsno.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/contest/')
def contest_list():
    length = len(HIUN_contest.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HIUN_contest.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response