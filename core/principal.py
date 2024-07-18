# core/principal.py

from flask import Blueprint, request, jsonify
from core.models import Assignment, Teacher, db
from core.models import Assignment, db
from core.models import Teacher, db
from core.models.assignments import AssignmentStateEnum, GradeEnum

principal_bp = Blueprint('principal', __name__)

@principal_bp.route('/principal/assignments', methods=['GET'])
def list_all_assignments():
    assignments = Assignment.query.filter(Assignment.state.in_([AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED])).all()
    return jsonify(data=[assignment.to_dict() for assignment in assignments])

principal_bp = Blueprint('principal', __name__)

@principal_bp.route('/principal/teachers', methods=['GET'])
def list_all_teachers():
    teachers = Teacher.query.all()
    return jsonify(data=[teacher.to_dict() for teacher in teachers])

principal_bp = Blueprint('principal', __name__)

@principal_bp.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.json
    assignment_id = data.get('id')
    grade = data.get('grade')

    assignment = Assignment.query.get(assignment_id)
    if not assignment:
        return jsonify(error="Assignment not found"), 404

    if assignment.state == AssignmentStateEnum.DRAFT:
        return jsonify(error="Cannot grade a draft assignment"), 400

    assignment.grade = GradeEnum(grade)
    assignment.state = AssignmentStateEnum.GRADED
    db.session.commit()
    return jsonify(data=assignment.to_dict())

