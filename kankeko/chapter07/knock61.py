import plyvel


def get_area(name):
    db = plyvel.DB('./db', create_if_missing=True)
    return db.get(name.encode("utf-8"))

if __name__ == "__main__":
    print(get_area("Amazon").decode("utf-8"))
