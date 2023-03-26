from blog.models.database import db

from blog.app import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=False,
    )
