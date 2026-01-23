class ETL:
    def extract(self):
        print("Extracting data")

    def transform(self):
        print("Transforming data")

    def load(self):
        print("Loading data")


pipeline = ETL()
pipeline.extract()
pipeline.transform()
pipeline.load()
