

def register_routes(app, db):

    @app.route('/')
    def home():
        return 'Hello Flask'
