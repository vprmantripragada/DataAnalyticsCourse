from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# setup mongo connection
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)

# connect to mongo db and collection
#db = client.mars
#collection = db.mars_db


@app.route("/scrape")
def scraper():
    
    # Run the scrape function
    mars_info = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")


@app.route("/")
def home():
    mars_info = mongo.db.collection.find_one()
    return render_template("index.html", mars_info = mars_info)


if __name__ == "__main__":
    app.run(debug=True)