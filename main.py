from classes import APIWrapper, DataBase
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='my_program ',
        description='Command line program that will use the API wrapper and the database class to get a random '
                    'activity and save it in the database. ',
    )

    # Positional
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command new
    new_parser = subparsers.add_parser("new", help="Command to fetch and save a new activity")

    # Optional
    new_parser.add_argument("--type", type=str, help="Filter by activity type")
    new_parser.add_argument("--participants", type=int, help="Specify the number of participants")
    new_parser.add_argument("--price_min", type=float, help="Specify the minimum price range (0.0 - 1.0)")
    new_parser.add_argument("--price_max", type=float, help="Specify the maximum price range (0.0 - 1.0)")
    new_parser.add_argument("--accessibility_min", type=float, help="Specify the minimum accessibility (0.0 - 1.0)")
    new_parser.add_argument("--accessibility_max", type=float, help="Specify the maximum accessibility (0.0 - 1.0)")

    # Command list
    list_parser = subparsers.add_parser("list", help="Return the last activities saved in the database")

    args = parser.parse_args()

    api = APIWrapper()
    db = DataBase()

    if args.command == "new":
        activity_data = api.get_random_act(
            act_type=args.type,
            participants=args.participants,
            minprice=args.price_min,
            maxprice=args.price_max,
            minaccessibility=args.accessibility_min,
            maxaccessibility=args.accessibility_max
        )

        print(activity_data)
        if activity_data:
            db.save_activity(activity_data)

    if args.command == "list":
        lst = db.get_last_5_data()
        for l in lst:
            print(l)


if __name__ == "__main__":
    main()




