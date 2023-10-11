from flask import Blueprint, render_template
import pymongo

mongodb_list_bp = Blueprint('mongodb_list', __name__)

@mongodb_list_bp.route('/mongodb_list')
def mongodb_list():
    try:
        # Replace with your MongoDB connection string
        mongo_url = "YOUR_MONGODB_CONNECTION_STRING"
        client = pymongo.MongoClient(mongo_url)

        # List all the databases in your cluster
        all_databases = client.list_database_names()

        database_collections = {}  # To store collections for each database

        for db_name in all_databases:
            db = client[db_name]
            collections = db.list_collection_names()
            database_collections[db_name] = collections

        client.close()

        return render_template('mongodb_list.html', database_collections=database_collections)

    except pymongo.errors.ConnectionFailure:
        error_message = "Failed to connect to MongoDB. Please check the connection URL."
        return render_template('mongodb_list.html', error_message=error_message)

