from HIIN import db
from HIIN.models import HIUN_corona, HIUN_generalno, HIUN_studentsno, HIUN_contest, HICEN_department, HICEN_employment, HICEN_class, HICEN_SCSC, HICEN_scholarship

from flask import Blueprint, url_for
from werkzeug.utils import redirect

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


bp = Blueprint('main', __name__, url_prefix='/')

webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_argument('headless')

s = Service("C:\\projects\\HIIN\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=webdriver_options)


@bp.route('/')
def index():
    return redirect(url_for('HIUN.corona_list'))


@bp.route('/dbreset_hiun_corona/')
def dbreset_hiun_corona():
    db.session.query(HIUN_corona).delete()
    db.session.commit()
    DB_input_hiun_corona()
    return redirect(url_for('HIUN.corona_list'))


@bp.route('/dbreset_hiun_generalno/')
def dbreset_hiun_generalno():
    db.session.query(HIUN_generalno).delete()
    db.session.commit()
    DB_input_hiun_generalno()
    return redirect(url_for('HIUN.generalno_list'))


@bp.route('/dbreset_hiun_studentsno/')
def dbreset_hiun_studentsno():
    db.session.query(HIUN_studentsno).delete()
    db.session.commit()
    DB_input_hiun_studentsno()
    return redirect(url_for('HIUN.studentsno_list'))


@bp.route('/dbreset_hiun_contest/')
def dbreset_hiun_contest():
    db.session.query(HIUN_contest).delete()
    db.session.commit()
    DB_input_hiun_contest()
    return redirect(url_for('HIUN.contest_list'))


@bp.route('/dbreset_hicen_department/')
def dbreset_hicen_department():
    db.session.query(HICEN_department).delete()
    db.session.commit()
    DB_input_hicen_department()
    return redirect(url_for('HICEN.department_list'))


@bp.route('/dbreset_hicen_employment/')
def dbreset_hicen_employment():
    db.session.query(HICEN_employment).delete()
    db.session.commit()
    DB_input_hicen_employment()
    return redirect(url_for('HICEN.employment_list'))


@bp.route('/dbreset_hicen_class/')
def dbreset_hicen_class():
    db.session.query(HICEN_class).delete()
    db.session.commit()
    DB_input_hicen_class()
    return redirect(url_for('HICEN.class_list'))


@bp.route('/dbreset_hicen_SCSC/')
def dbreset_hicen_SCSC():
    db.session.query(HICEN_SCSC).delete()
    db.session.commit()
    DB_input_hicen_SCSC()
    return redirect(url_for('HICEN.SCSC_list'))


@bp.route('/dbreset_hicen_scholarship/')
def dbreset_hicen_scholarship():
    db.session.query(HICEN_scholarship).delete()
    db.session.commit()
    DB_input_hicen_scholarship()
    return redirect(url_for('HICEN.scholarship_list'))


# Crawler
def DB_input_hiun_corona():
    driver.get(url='https://www.hongik.ac.kr/contents/www/cor/corona.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HIUN_corona(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hiun_generalno():
    driver.get(url='https://www.hongik.ac.kr/contents/www/cor/generalno.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HIUN_generalno(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hiun_studentsno():
    driver.get(url='https://www.hongik.ac.kr/contents/www/cor/studentsno.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.bbs-pane")))
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HIUN_studentsno(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hiun_contest():
    driver.get(url='https://www.hongik.ac.kr/contents/www/cor/contest.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HIUN_contest(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_department():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/0401.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_department(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_employment():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/cs/0402.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_employment(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_employment():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/cs/0402.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_employment(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_class():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/cs/0403.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_class(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_SCSC():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/cs/0404.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_SCSC(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)

def DB_input_hicen_scholarship():
    driver.get(url='https://wwwce.hongik.ac.kr/dept/cs/0405.html')

    moveFrm = driver.find_element(By.ID, 'mainFrm')
    driver.switch_to.frame(moveFrm)

    endPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(6) > div > div > div:nth-child(3) > a.d.last')
    endPageBtn.send_keys(Keys.ENTER)

    currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a').get_attribute('href')
    currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
    currentUrl = currentUrlVer2.replace('^', '&')

    firstElementBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(3) > div > table > tbody > tr:nth-last-child(1) > td:nth-child(2) > div > a')
    firstElementBtn.send_keys(Keys.ENTER)

    while True:
        subject = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(1) > th > div > span').text
        writer = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > span.value').text
        date = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(1) > div.grid.bbs-read > table > tbody > tr:nth-child(2) > td > div > div > div:nth-child(2) > span.value').text
        link = currentUrl

        driver.switch_to.default_content()

        style = driver.find_element(By.ID, 'mainFrm').get_attribute('style')

        widthstr = style.split(' ')[3]
        heightstr = style.split(' ')[1]

        width = int(widthstr.split('p')[0])
        height = int(heightstr.split('p')[0])

        moveFrm = driver.find_element(By.ID, 'mainFrm')
        driver.switch_to.frame(moveFrm)

        d = HICEN_scholarship(subject=subject, writer=writer, date=date, link=link, width=width, height=height)
        db.session.add(d)
        db.session.commit()

        nextPageExist = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div').get_attribute('class')

        if nextPageExist == 'subject empty':
            break

        currentUrlVer1 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a').get_attribute('href')
        currentUrlVer2 = currentUrlVer1.replace('/viewcount.do?rtnUrl=', '')
        currentUrl = currentUrlVer2.replace('^', '&')

        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td > div > a')
        nextPageBtn.send_keys(Keys.ENTER)