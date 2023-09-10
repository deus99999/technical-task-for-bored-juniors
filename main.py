from classes import APIWrapper, DataBase
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='my_program ',
        description='What the program does',
        epilog='Text at the bottom of help')

    parser.add_argument("new", help="Command to fetch and save a new activity")
    parser.add_argument("--type", help="Filter by activity type")
    parser.add_argument("--participants", type=int, help="Specify the number of participants")
    parser.add_argument("--price_min", type=float, help="Specify the minimum price range (0.0 - 1.0)")
    parser.add_argument("--price_max", type=float, help="Specify the maximum price range (0.0 - 1.0)")
    parser.add_argument("--accessibility_min", type=float, help="Specify the minimum accessibility (0.0 - 1.0)")
    parser.add_argument("--accessibility_max", type=float, help="Specify the maximum accessibility (0.0 - 1.0)")

    args = parser.parse_args()
    print(args.new, args.type)


if __name__ == "__main__":
    main()

# a = APIWrapper()
# # activity_data = a.get_random_act(act_type="education", participants=1, price=0, accessibility=0.1)
# activity_data = a.get_random_act()
# print(activity_data)
# db = DataBase()
# db.save_activity(activity_data)
# db.get_last_data()

