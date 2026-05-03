from RB_trees import RedBlackTree
import os
def load_dictionary(tree, filename):
    if not os.path.exists(filename):
        print(f"Creating new dictionary file: {filename}")
        open(filename, 'w').close()
        return

    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            if word:
                tree.insert(word)
    print(f"Dictionary loaded. Total words: {tree.size}")


def dictionary_app():
    tree = RedBlackTree()
    filename = "dictionary.txt"
    load_dictionary(tree, filename)

    while True:
        print("\n--- English Dictionary Menu ---")
        print("1. Insert Word")
        print("2. Look-up a Word")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            word = input("Enter word to insert: ").strip()
            if tree.insert(word):

                with open(filename, 'a') as f:
                    f.write(word + "\n")
                print(f"SUCCESS: '{word}' added.")
            else:
                print(f"ERROR: Word '{word}' already in the dictionary!")


            print(f"Tree Size: {tree.size}")
            print(f"Tree Height: {tree.get_height(tree.root)}")
            print(f"Black Height: {tree.get_black_height(tree.root)}")

        elif choice == '2':
            word = input("Enter word to search: ").strip()
            result = tree.search(word)
            if result != tree.NIL:
                print("YES")
            else:
                print("NO")

        elif choice == '3':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    dictionary_app()