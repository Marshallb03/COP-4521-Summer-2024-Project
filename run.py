from WebApp import create_app, create_db

app = create_app()

with app.app_context():
    create_db(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
