from flask import current_app as app   

@app.route('/hello')
def helloworld():
    return 'Hello World! \n This is coming from __init__.py'