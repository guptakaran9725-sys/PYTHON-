# PRACTICAL 19: Count words in a file

def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("Error: File not found!")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


# -------------------------------
# Example usage
filename = input("Enter the filename: ")
word_count = count_words_in_file(filename)

if word_count is not None:
    print(f"The file '{filename}' contains {word_count} words.")