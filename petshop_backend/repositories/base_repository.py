from extensions import db

class BaseRepository:
    model=None
    @classmethod
    def get_all(cls):
        return cls.model.query.all()
    
    @classmethod
    def get_by_id(cls, item_id):
        return db.session.get(cls.model, item_id)
    
    @classmethod
    def add(cls, instance):
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        return instance
    
    @classmethod
    def delete(cls, instance):
        db.session.delete(instance)
        db.session.commit()

    @classmethod
    def commit(cls):
        db.session.commit()
    
    @classmethod
    def rollback(cls):
        db.session.rollback()