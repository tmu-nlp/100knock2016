import plyvel


def get_japans_artists(searched_area):
    db = plyvel.DB('./db', create_if_missing=True)
    count = 0
    for name, area in db:
        if area == searched_area.encode("utf-8"):
            count += 1
    return count


if __name__ == "__main__":
    print(get_japans_artists("Japan"))
