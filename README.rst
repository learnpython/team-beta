**About:**
    Some info

**Requirements:**
    OS requirements - Python 2.7, python-virtualenv, python-imaging
    ENV - all from requirements.txt file

**Install:**

To install app you need do next steps:
    Go to you projects dir, and clone git
    git clone https://github.com/learnpython/team-beta.git

    Next, go to team-beta, and create virtual environment
    cd team-beta && virtualenv env
    and install requirements
    source env/bin/activate 
    pip install -r requirements.txt

    download http://twitter.github.com/bootstrap/index.html imto /static/

    Next, sync projects
    python zo/manage.py syncdb
    python zo/manage.py collectstatic

Run:
    (activate your env if isn't)
    cd zo && gunicorn_django -b 0.0.0.0:8000
    
    Open your Web browser and go to http://127.0.0.1:8000
    That's all!
    
    To join as administrator, go to http://127.0.0.1:8000/admin and input 
        user: admin
        pass: nimda

Windows:
    If you run your project on OS windows with runserver, 
    you need add --nostatic key when start runserver
    ex. python manage.py runserver --nostatic