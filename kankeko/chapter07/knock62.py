import plyvel


def get_japan(sarea):
    db = plyvel.DB('./db', create_if_missing=True)
    count = 0
    for name,area in db:
        if area == sarea.encode("utf-8"):
            count += 1
    return count

if __name__ == "__main__":
    print(get_japan("Japan"))
