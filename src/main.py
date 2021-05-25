from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from searchdao.searchdao import SearchesDAO
from external.git_jobs import access_git_jobs
from constants import FLASK_HOST, FLASK_PORT

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

@app.route("/record_search", methods = ["POST"])
def record_search():
    data = json.loads(request.data)
    print('data', str(data))
    searches = SearchesDAO()
    response = searches.add_search_to_db(data=data)
    return jsonify(response), 200



@app.route("/get_jobs/<string:location>/<string:description>", methods = ["GET"])
def get_git_jobs(location, description):

    if all([location, description]) == None:
        return jsonify({}), 200
  
    else:
        response = access_git_jobs(location, description)
        return jsonify(response), 200
    




if __name__ == "__main__":
    #First initializes the DB to assure the existence of the searches table.
    SearchesDAO().initialize_search_table
    app.run(host=FLASK_HOST, port=FLASK_PORT)