from application import db

class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    @staticmethod
    def register_user(email, name, role, password):
        user = User(email=email, name=name, role=role, password=password)
        db.session.add(user)
        db.session.commit()
        return user

class Datasets(db.Model):
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(20), nullable=False)
    owner = db.Column(db.String(20), nullable=True)
