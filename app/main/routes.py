
from flask import Blueprint, render_template, session
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

permissions = {
    'SatishD': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'JayM': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'AndrewS': ['First Bio Genetics', 'AIM Laboratories'],
    'AshlieT': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'VinceO': ['AMICO Dx'],
    'ACG': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'SonnyN': ['AMICO Dx'],
    'MinaK': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'NickC': ['AMICO Dx'],
    'MelindaC': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'Omar': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'DarangT': ['AMICO Dx', 'Enviro Labs'],
    'BobS': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'BobSilverang': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'Stat Labs'],
    'AghaA': ['AMICO Dx'],
    'Wenjun': ['AMICO Dx'],
    'NickT': ['First Bio Lab', 'First Bio Genetics', 'First Bio Lab of Illinois', 'AIM Laboratories', 'AMICO Dx', 'Enviro Labs', 'Stat Labs'],
    'AndreaM': ['AMICO Dx'],
    'BenM': ['Stat Labs'],
    'WeesL': ['Stat Labs'],
}

@main.route('/dashboard')
@login_required
def dashboard():
    username = current_user.username
    allowed_entities = permissions.get(username, [])
    return render_template('dashboard.html', entities=allowed_entities)
