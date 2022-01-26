## simple flask application with task queue
 uses redis as message broker and rq for task queue

## running instructions

# set up
set up a venv and activate it
pip install -r requirements.txt
on linux:
    clone repo (git clone <repo_url>)
    cd into project folder
    export FLASK_APP=ex1
    flask run

    open another terminal in the same directory and run rq worker (make sure you have redis installed and working)

