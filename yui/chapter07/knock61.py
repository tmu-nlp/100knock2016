# -*- coding: utf-8 -*-

import plyvel


def get_artists_area(name):
    db = plyvel.DB('./db', create_if_missing=True)
    return db.get(name.encode("utf-8"))
    db.close()


if __name__ == "__main__":
    print(get_artists_area("Mew").decode("utf-8"))
