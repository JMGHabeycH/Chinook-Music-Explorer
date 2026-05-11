from services import search_songs, best_seller_songs, best_seller_albums

def main():
    while True:
        print("\n===== MUSIC APP =====")
        print("1. Search for songs")
        print("2. Best seller songs")
        print("3. Best seller albums")
        print("0. Exit")

        option = input("Choose an option (1, 2, 3, 0): ").strip()

        if option == "1":
            keyword = input("Enter the song name or part of the song name: ").strip()
            df = search_songs(keyword)
            if df.empty:
                print("\nNo songs were found.")
            else:
                print("\nSearch results:")
                print(df.to_string(index=False))
        elif(option == "2"):
            df = best_seller_songs()
            print(df.to_string(index=False))
        elif(option == "3"):
            df = best_seller_albums()
            print(df.to_string(index = False))
        elif(option == "0"):
            print("\nGoodbye")
            break
        else:
            print("\nInvalid option. Try again.")
        
if __name__ == "__main__":
    main()