from HIIN import db

#교내공지

class HIUN_corona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HIUN_generalno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HIUN_studentsno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HIUN_contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)


#학과공지_컴퓨터공학과

class HICEN_department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HICEN_employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HICEN_class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HICEN_SCSC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class HICEN_scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)