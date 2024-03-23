from app.controllers.files import upload_file
from flask import Blueprint, abort, jsonify, request
from flask_login import current_user, login_required

files_bp = Blueprint("files", __name__)


@files_bp.route("/files/<qid>/upload", methods=["POST"])
@login_required
def upload_file_route(qid: str):
    if "file" not in request.files:
        abort(400, description="No file part")
    file = request.files["file"]
    if file.filename == "":
        abort(400, description="No selected file")
    upload_file(current_user.user_dict["username"], qid, file)
    return jsonify({"message": "File uploaded successfully"}), 200
