import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import (
    Organization as OrganizationModel,
    Project as ProjectModel,
    Mission as MissionModel,
    Dataset as DatasetModel,
    Granule as GranuleModel,
    GranuleObject as GranuleObjectModel,
)


class Organization(SQLAlchemyObjectType):
    class Meta:
        model = OrganizationModel
        interfaces = (relay.Node, )


class OrganizationConnection(relay.Connection):
    class Meta:
        node = Organization


class Project(SQLAlchemyObjectType):
    class Meta:
        model = ProjectModel
        interfaces = (relay.Node, )


class ProjectConnection(relay.Connection):
    class Meta:
        node = Project


class Mission(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (relay.Node, )


class MissionConnection(relay.Connection):
    class Meta:
        node = Mission


class Dataset(SQLAlchemyObjectType):
    class Meta:
        model = DatasetModel
        interfaces = (relay.Node, )


class DatasetConnection(relay.Connection):
    class Meta:
        node = Dataset


class Granule(SQLAlchemyObjectType):
    class Meta:
        model = GranuleModel
        interfaces = (relay.Node, )


class GranuleConnection(relay.Connection):
    class Meta:
        node = Granule


class GranuleObject(SQLAlchemyObjectType):
    class Meta:
        model = GranuleObjectModel
        interfaces = (relay.Node, )


class GranuleObjectConnection(relay.Connection):
    class Meta:
        node = GranuleObject


class SearchResult(graphene.Union):
    class Meta:
        types = (Dataset,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_organizations = SQLAlchemyConnectionField(OrganizationConnection)
    all_datasets = SQLAlchemyConnectionField(Dataset)
    search = graphene.List(SearchResult, pattern=graphene.String())


    def resolve_search(self, info, **args):
        pattern = args.get("pattern")

        dataset_query = Dataset.get_query(info)
        datasets = dataset_query.filter(
            DatasetModel.name.like(pattern)
        ).all()

        return datasets


schema = graphene.Schema(query=Query, types=[Dataset, Granule, SearchResult])
