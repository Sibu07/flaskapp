# routes/mongodb_routes.py
from flask import Blueprint, request, render_template
import pymongo

mongodbzm_bp = Blueprint('mongodbzm', __name__)

# Define a route to take input from the user for the MongoDB connection URL
@mongodbzm_bp.route('/mongodbzm_query', methods=['GET', 'POST'])
def mongodb_query():
    if request.method == 'POST':
        # Retrieve the MongoDB connection URL from the form input
        mongo_url = request.form.get('mongo_url')

        try:
            # Create a MongoClient
            client = pymongo.MongoClient(mongo_url)

            # Access your database (Replace 'wzmlx' with your actual database name)
            db = client['zmirror']

            # List all the collections in the database
            collections = db.list_collection_names()

            # Create a dictionary to store the collection documents
            collection_documents = {}

            # Iterate through the collections and retrieve data from each one
            for collection_name in collections:
                collection = db[collection_name]
                all_documents = list(collection.find())
                collection_documents[collection_name] = all_documents

            return render_template('mongodb_results.html', collections=collections, documents=collection_documents)

        except pymongo.errors.ConnectionFailure:
            error_message = "Failed to connect to MongoDB. Please check the connection URL."
            return render_template('mongodb_results.html', error_message=error_message)

    return render_template('mongodb_query.html')
    