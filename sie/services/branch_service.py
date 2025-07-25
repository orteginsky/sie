from sie.database.models.branch import Branch
from sie.crud.branch import create_branch
from sie.database.connection import get_db

def register_branch(branch_dict: dict) -> Branch:
    db = next(get_db())
    try:
        """existing = db.query(Branch).filter_by().first()
        if existing:
            raise ValueError("ocurrio un error en branch_service.py")"""
        branch = create_branch(db,branch_dict)
        return branch
    finally:
        db.close()