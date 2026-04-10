# PRACTICAL 20: Copy content of one file to another

def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            content = src.read()
        with open(destination_file, "w") as dest:
            dest.write(content)
        print(f"Content copied successfully from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print("Error: Source file not found!")
    except Exception as e:
        print("An error occurred:", e)


# -------------------------------
# Example usage
source = input("Enter source filename: ")
destination = input("Enter destination filename: ")

copy_file(source, destination)