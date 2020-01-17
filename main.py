from HarleyBot import HarleyBot


def main():
    config = {
        "api_key":
            "c7b9614a600d732d9487dc3d828342d3c14fa67a8daca36ee3b012447fd36be071be11991540e5474ea55",
        "group_id": "61782600",
        "creator": 99806575
    }

    harley = HarleyBot(
        config["api_key"],
        config["group_id"],
        config["creator"]
    )

    harley.load('data.json')
    harley.start()
    harley.save('data.json')


if __name__ == '__main__':
    main()
