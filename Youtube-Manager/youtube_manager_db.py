import sqlite3

conn = sqlite3.connect("youtube_manager_db.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Videos(
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          time TEXT NOT NULL
  )
    """
)


def list_videos():
    cursor.execute("SELECT * FROM Videos")
    for row in cursor.fetchall():
      print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO Videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit()


def update_videos(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM Videos WHERE id=?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Manger app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. delete videos")
        print("5. exit")

        choice = input("Enter the choices: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)

        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id, name, time)

        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_videos(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            continue

    conn.close()


if __name__ == "__main__":
    main()
