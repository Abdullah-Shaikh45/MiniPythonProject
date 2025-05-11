import json

# Load video data from file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save video data to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

# Display the list of videos
def list_video(videos):
    print("\n" + "*" * 40)
    print(f"Total videos: {len(videos)}")
    print("*" * 40)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
        print("*" * 40)

# Add a new video
def add_video(videos):
    name = input("Enter the name: ").strip()
    time = input("Enter the time: ").strip()
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

# Update an existing video
def update_video(videos):
    list_video(videos)
    try:
        index = int(input("Enter video number to update: ").strip())
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ").strip()
            time = input("Enter the new video time: ").strip()
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid index value!")
    except ValueError:
        print("Please enter a valid number.")

# Delete a video
def delete_video(videos):
    list_video(videos)
    try:
        index = int(input("Enter the video number to be deleted: ").strip())
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
        else:
            print("Invalid video index selected.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the app
def main():
    videos = load_data()
    while True:
        print("\n" + "=" * 40)
        print("Welcome to YouTube Manager!")
        print("=" * 40)
        print("\nOption List:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the application")

        try:
            choice = int(input("\nChoose your option: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                list_video(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice! Please choose a number from the options list.")

if __name__ == "__main__":
    main()
