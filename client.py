from base import app


@app.route('/client')
def client_main():
    with open('templates/client.html', 'r') as file:
        return file.read()




