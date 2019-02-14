class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),index = True)
    email = db.Column(db.String(20),unique = True,index = True)
    password_hash = db.Column(db.String(30))
