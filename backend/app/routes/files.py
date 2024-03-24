from app.controllers.files import upload_file, execute_file
from flask import Blueprint, abort, jsonify, request
from flask_login import current_user, login_required

files_bp = Blueprint("files", __name__)


@files_bp.route("/files/<qid>/upload", methods=["POST"])
@login_required
def upload_file_route(qid: str):
    """
    Upload a file to the server. The file will be saved in the backend/data/user_files directory. The request body should be in form-data format and should contain a file field with the file to upload.

    Route:
        http://localhost:5000/files/<qid>/upload

    Returns:
        dict: A message indicating that the file was uploaded successfully
    """
    if "file" not in request.files:
        abort(400, description="No file part")
    file = request.files["file"]
    if file.filename == "":
        abort(400, description="No selected file")
    path = upload_file(current_user.user_dict["username"], qid, file)
    return jsonify({"message": f"File uploaded successfully to {path}"}), 200


@files_bp.route("/files/<qid>/execute", methods=["GET"])
@login_required
def execute_file_route(qid: str):
    """
    Execute the test cases for the file uploaded by the user. It will be tested against the test cases for the question with the given ID.

    Route:
        http://localhost:5000/files/<qid>/execute

    Returns:
        dict: Either the number of test cases passed by the file or an error message
    """
    result = execute_file(current_user.user_dict["username"], qid)
    return jsonify({"result": result}), 200
