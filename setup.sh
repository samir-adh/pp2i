source env/bin/activate
python3 app/flask/setup_presentation.py
export FLASK_APP=app/flask/pp2i.py
export FLASK_DEBUG=true
flask run