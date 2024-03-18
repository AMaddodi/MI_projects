from backend_server import creat_app

app = creat_app()

if __name__ == '__main__':
    app.run(debug=True)