from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_professor(professor_idt):
    return Professor.query.filter_by(id=professor_idt).first()

class Professor(db.Model, UserMixin):
    __tablename__ = 'tb_professor'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nme_professor = db.Column(db.String(86), nullable=False)
    senha_professor = db.Column(db.String(128), nullable=False)
    matricula_professor = db.Column(db.Integer, nullable=False)
    formacao_professor = db.Column(db.String(45), nullable=False)
    nasc_professor = db.Column(db.String(11), nullable=False)
    sangue_professor = db.Column(db.String(5), nullable=False)
    disc_professor = db.Column(db.String(45), nullable=False)

    def __init__(self, nme_professor, senha_professor, matricula_professor, formacao_professor,  nasc_professor, sangue_professor, disc_professor):
        self.nme_professor = nme_professor
        self.senha_professor = generate_password_hash(senha_professor)
        self.matricula_professor = matricula_professor
        self.formacao_professor = formacao_professor
        self.nasc_professor = nasc_professor
        self.sangue_professor = sangue_professor
        self.disc_professor = disc_professor

    def verify_password(self, senha_professor):
        return check_password_hash(self.senha_professor, senha_professor)

