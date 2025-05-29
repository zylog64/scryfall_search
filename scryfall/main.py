import argparse
from scrython import cards

parser = argparse.ArgumentParser(
    description="Search Scryfall for cards and print to stdout for cardmarket whislists"
)
parser.add_argument("--set", help="add set filter")
parser.add_argument("--rarity", help="add rarity filter")
parser.add_argument("--color", help="add color filter")
args = parser.parse_args()


def main():
    result = cards.Search(q=build_query())
    print(f"Found {result.total_cards()} cards\n")
    write_to_stdout(result.data())

def build_query():
    query = ""
    if args.set:
        query += f"e:{args.set} "
    if args.rarity:
        query += f"r:{args.rarity} "
    if args.color:
        query += f"c:{args.color} "

    return query.strip()

def write_to_stdout(cards):
    for i, card in enumerate(cards):
        if i != 0 and i % 50 == 0:
            print("\n\n")
        print(f"1 {card['name']} ({card['set_name']})")


if __name__ == "__main__":
    main()
