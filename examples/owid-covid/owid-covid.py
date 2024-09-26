from owid import catalog


def save_data(uri, path):
    rc = catalog.RemoteCatalog()
    data = rc[uri]
    data.to_csv(path)


if __name__ == "__main__":
    URI = "garden/owid/latest/covid/covid"
    PATH = "owid-covid.csv"
    save_data(URI, PATH)
