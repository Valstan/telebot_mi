from pygismeteo import Gismeteo


def gismeteo(city):
    gismet = Gismeteo()
    search_results = gismet.search.by_query(city)
    city_id = search_results[0].id
    current = gismet.current.by_id(city_id)
    return f"В {city} {int(current.temperature.air.c)} " \
           f"(по ощущению {int(current.temperature.comfort.c)}) " \
           f"{current.description.full}"


if __name__ == "__main__":
    pass
