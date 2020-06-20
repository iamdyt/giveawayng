from app import app,db
# Create and Update Migrations
(lambda: db.create_all(app=app))()

# Drop table
# (lambda:db.drop_all(app=app))()
