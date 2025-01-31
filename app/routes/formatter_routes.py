import json
from flask import Blueprint, request, jsonify

formatter_bp = Blueprint('formatter', __name__)


@formatter_bp.route('/api/format', methods=['POST'])
def format_data():
    # Get the data from the request
    data = request.get_json()

    # Check for the data key in the JSON
    if 'data' not in data:
        return jsonify({"message": "missing data key"}), 400

    # Get the data from the JSON
    data = data['data']

    try:
        columns = data['columns']
        results = data['results']

        # Create the transformed JSON structure
        transformed_data = {
            "data_type": "table",
            "content": {
                "columns": columns,
                "rows": results
            }
        }

        return jsonify({
            "message": "Data formatted successfully",
            "formatted_data": transformed_data
        }), 200

    except (json.JSONDecodeError, KeyError, ValueError) as e:
        return jsonify({
            "message": "Error formatting data",
            "error": str(e)
        }), 400
