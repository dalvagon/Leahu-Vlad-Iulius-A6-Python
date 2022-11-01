from utils import process_item


if __name__ == "__main__":
    while True:
        print("Enter a number:")
        try:
            print(process_item(int(input())))
        except ValueError:
            print("Please enter a number!")
