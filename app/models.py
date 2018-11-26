from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
)
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///database.sqlite3',
                       convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    organization = relationship(
        Organization,
        backref=backref(
            'projects',
            uselist=True,
            cascade='delete,all'
        )
    )


class Mission(Base):
    __tablename__ = 'mission'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(
        Project,
        backref=backref(
            'missions',
            uselist=True,
            cascade='delete,all'
        )
    )


class Dataset(Base):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(Integer)
    mission_id = Column(Integer, ForeignKey('mission.id'))
    mission = relationship(
        Mission,
        backref=backref(
            'datasets',
            uselist=True,
            cascade='delete,all'
        )
    )


class Granule(Base):
    __tablename__ = 'granule'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dataset_id = Column(Integer, ForeignKey('dataset.id'))
    dataset = relationship(
        Dataset,
        backref=backref(
            'granules',
            uselist=True,
            cascade='delete,all'
        )
    )


class GranuleObject(Base):
    __tablename__ = 'granule_object'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    granule_id = Column(Integer, ForeignKey('granule.id'))
    granule = relationship(
        Granule,
        backref=backref(
            'granule_objects',
            uselist=True,
            cascade='delete,all'
        )
    )
