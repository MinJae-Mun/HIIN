from flask import Blueprint, jsonify

from HIIN.models import HICEN_department, HICEN_employment, HICEN_class, HICEN_SCSC, HICEN_scholarship



bp = Blueprint('HICEN', __name__, url_prefix='/HICEN')


@bp.route('/department/')
def department_list():
    length = len(HICEN_department.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HICEN_department.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/employment/')
def employment_list():
    length = len(HICEN_employment.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HICEN_employment.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/class/')
def class_list():
    length = len(HICEN_class.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HICEN_class.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/SCSC/')
def SCSC_list():
    length = len(HICEN_SCSC.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HICEN_SCSC.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response


@bp.route('/scholarship/')
def scholarship_list():
    length = len(HICEN_scholarship.query.all())
    dictionary = {}

    for i in range(1, length+1):
        d = HICEN_scholarship.query.get(i)
        dictupdate = {
            d.id: [d.subject, d.writer, d.date, d.link, d.width, d.height]
        }
        dictionary.update(dictupdate)

    response = jsonify(dictionary)
    response.status_code = 200

    return response