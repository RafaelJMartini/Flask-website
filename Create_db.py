 with app.app_context():
     database.drop_all()
     database.create_all()
