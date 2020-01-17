from HarleyBot import HarleyBot


def main():
    config = {
        "api_key": "3d7683f13e30172b7f5ebe5448cef62d992975d1f7e6915bb0ef71d9087baadfa3538c76ef8e5a6ba1bed",
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
