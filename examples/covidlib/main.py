from covidlib.retriever import save_data


if __name__ == "__main__":
    URI = "garden/owid/latest/covid/covid"
    PATH = "owid-covid.csv"
    save_data(URI, PATH)
