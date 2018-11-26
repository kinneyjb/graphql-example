#!/usr/bin/env python

from app.models import (
    engine, db_session, Base,
    Organization, Project, Mission, Dataset, Granule, GranuleObject
)

Base.metadata.create_all(bind=engine)

num_organizations = 2
num_projects = 3
num_missions = 4
num_datasets = 5
num_granules = 10
num_granule_objects = 2


for oi in range(num_organizations):
    name = f'org-{oi}'
    org = Organization(name=name)
    db_session.add(org)

    for pi in range(num_projects):
        name = f'project-{oi}-{pi}'
        project = Project(
            name=name,
            organization=org
        )
        db_session.add(project)

        for mi in range(num_missions):
            name = f'mission-{oi}-{pi}-{mi}'
            mission = Mission(
                name=name,
                project=project
            )
            db_session.add(mission)

            for di in range(num_datasets):
                name = f'dataset-{oi}-{pi}-{mi}-{di}'
                dataset = Dataset(
                    name=name,
                    mission=mission
                )
                db_session.add(dataset)

                for gi in range(num_granules):
                    name = f'granule-{oi}-{pi}-{mi}-{di}-{gi}'
                    granule = Granule(
                        name=name,
                        dataset=dataset
                    )
                    db_session.add(granule)

                    for goi in range(num_granule_objects):
                        name = f'granule_object-{oi}-{pi}-{mi}-{di}-{gi}-{goi}'
                        granule_object = GranuleObject(
                            name=name,
                            granule=granule
                        )
                        db_session.add(granule_object)

db_session.commit()
