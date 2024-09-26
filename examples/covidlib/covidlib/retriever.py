from owid import catalog


def save_data(uri, path):
    rc = catalog.RemoteCatalog()
    data = rc[uri]
    data.to_csv(path)
