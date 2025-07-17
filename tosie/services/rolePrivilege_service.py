from tosie.database.connection import get_db
from tosie.database.models.rolePrivilege import RolePrivilege
from tosie.crud.rolePrivilege import create_rolePrivilege

def register_role(rolePrivilege_dict:dict) -> RolePrivilege:
    db = next(get_db())
    try:
        existing = db.query(RolePrivilege).filter_by().first()
        if existing:
            raise ValueError("rolePrivilege already exist")
        rolePrivilege = create_rolePrivilege(db, rolePrivilege_dict)
        return rolePrivilege
    finally:
        db.close()

        