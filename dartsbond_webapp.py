from config import app, db

if __name__ == "__main__":
    db.create_all()
    # Optional als je met een SSL/TLS cert wil werken, maar deze zijn niet geverifireerd waardoor hij ongeldig is anders zou dit veel security dingen fiksen
    # app.run(host='127.0.0.1',
    #         port=500,
    #         debug=True,
    #         ssl_context=('cert.pem', 'key.pem'))
    app.run(host='127.0.0.1', port=500, debug=True)
