# routes/mongodb_routes.py
from flask import Blueprint, request, render_template, jsonify
import pymongo

mongodb_list_bp = Blueprint('mongodb_list', __name__)

# Define a route to list all databases and their collections
@mongodb_list_bp.route('/list_databases_collections', methods=['GET', 'POST'])
def list_databases_collections():
    if request.method == 'POST':
        try:
            # Retrieve the MongoDB connection URL from the form input
            mongo_uri = request.form.get('mongo_uri')

            # Create a MongoDB client
            client = pymongo.MongoClient(mongo_uri)

            # List all the databases in your cluster
            all_databases = client.list_database_names()

            # Create a dictionary to store database names and their collections
            database_collections = {}

            # Iterate through the databases and list their collections
            for db_name in all_databases:
                db = client[db_name]
                collections = db.list_collection_names()
                database_collections[db_name] = collections

            # Close the connection
            client.close()

            return render_template('mongodb_result.html', database_collections=database_collections)

        except pymongo.errors.ConnectionFailure:
            error_message = "Failed to connect to MongoDB. Please check the connection URL."
            return render_template('mongodb_result.html', error_message=error_message)

    return render_template('mongodb.html')
