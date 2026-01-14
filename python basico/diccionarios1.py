hotel={
    "name":"Stony Hill Resort",
    "stars":5,
    "rooms":[
        {
            "number":101,
            "floor":1,
            "nightly_rate":250
        },
        {
            "number":201,
            "floor":2,
            "nightly_rate":400
        },
        {
            "number":301,
            "floor":3,
            "nightly_rate":600
        }
    ]
}
hotel["name"]
hotel["stars"]
hotel["rooms"][0]["number"]
hotel["rooms"][1]["nightly_rate"]
new_room={
    "number":401,
    "floor":4,
    "nightly_rate":1000
}
hotel["rooms"].append(new_room)
for room in hotel["rooms"]:
    print(
        f"Habitacion {room["number"]} |"
        f"Piso {room["floor"]} |"
        f"${room["nightly_rate"]} por noche."
    )