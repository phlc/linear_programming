from backend import create_app

#Starts API server

app = create_app()

if __name__ == '__main__':
    app.run(port=8000, debug=True)