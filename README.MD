# File Organizer

A simple Python script that automatically sorts files in a folder (like your Downloads) into categorized subfolders — Pictures, Videos, Documents, Music, Zips, and an Other_Folder catch-all for anything unrecognized.

## Feature

- Sorts files by extension into clearly labeled folders
- Skips folders it finds (won't touch subfolders that already exist)
- Automatically creates destination folders if they don't exist
- Won't overwrite files — skips and warns you if a duplicate filename already exists in the destination
- Prints a log of every file it moves

## Getting the Code

**Option 1: Clone with Git**

If you have [Git](https://git-scm.com/) installed, open a terminal and run:

```bash
git clone https://github.com/HazelPhoniePalang/File_Organizer.git
cd file-organizer
```

(Replace the URL with your actual repo URL once it's created.)

**Option 2: Download as ZIP (no Git required)**

1. Go to the repository page on GitHub.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file anywhere on your computer.
5. Open a terminal in that extracted folder.

## 🚀 How to Use

1. Make sure you have the project on your computer using one of the methods above.
2. **Open a terminal** and navigate to the folder containing the script:

```bash
   cd path/to/file_organizer
```

3. **Run the script:**

```bash
   python file_organizer.py
```

4. By default, the script organizes your **Downloads** folder. Sit back and watch your terminal print out every file as it's moved.

## Important Notes

- **This script moves files, it doesn't copy them.** Once moved, files won't be in their original location anymore.
- It's a good idea to **test on a sample folder** with a few dummy files before running it on a real, important folder like Downloads.
- The script only organizes files in the **top level** of the target folder — it does not look inside subfolders.

## License

Free to use and modify for personal or educational projects.
