import json
from flask import url_for


def all_organizations():
    return """
    {
      allOrganizations {
        edges {
          node {
            id, name
          }
        }
      }
    }
    """


def all_datasets():
    return """
    {
      allDatasets { edges { node { name
        granules { edges { node { name
            granuleObjects { edges { node { name } } }
        } } }
      } } }
    }
    """


def search_dataset():
    return """
    {
      search(pattern: "dataset-1-1-1-1") {
        __typename
        ... on Dataset { name
          granules { edges { node { name
            granuleObjects { edges { node { name } } }
          } } }
        }
      }
    }
    """


def test_query_all_organizations(client):
    url = url_for('graphql')
    params = dict(query=all_organizations())
    result = client.post(url, query_string=params)
    assert result.status_code == 200
    data = json.loads(result.data)

    assert 'data' in data
    data = data['data']

    assert 'allOrganizations' in data
    data = data['allOrganizations']

    assert 'edges' in data
    data = data['edges']

    assert len(data) > 1
    for edge in data:
        node = edge['node']
        assert 'id' in node
        assert 'name' in node


def test_query_all_datasets(client):
    url = url_for('graphql')
    params = dict(query=all_datasets())
    result = client.post(url, query_string=params)
    assert result.status_code == 200
    data = json.loads(result.data)

    assert 'data' in data
    assert 'allDatasets' in data['data']
    assert 'edges' in data['data']['allDatasets']
    edges = data['data']['allDatasets']['edges']

    assert len(edges) > 0
    for edge in edges:
        assert 'node' in edge
        node = edge['node']
        assert 'granules' in node


def test_search_dataset(client):
    url = url_for('graphql')
    params = dict(query=search_dataset())
    result = client.post(url, query_string=params)
    assert result.status_code == 200
    data = json.loads(result.data)

    assert 'data' in data
    assert 'search' in data['data']
    datasets = data['data']['search']
    assert len(datasets) > 0

    for dataset in datasets:
        assert 'name' in dataset
        assert 'granules' in dataset
        assert 'edges' in dataset['granules']
        edges = dataset['granules']['edges']
        assert len(edges) > 0
        for edge in edges:
            assert 'node' in edge
            node = edge['node']
            assert 'name' in node
            assert 'granuleObjects' in node
            assert 'edges' in node['granuleObjects']
            assert len(node['granuleObjects']['edges']) > 1


