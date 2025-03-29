# the_indexer.py
import os
from datetime import datetime
import urllib.parse
import re

def numerical_sort_key(filename):
    # Extract the number from the beginning of the filename (e.g., "1. Dragging..." -> 1)
    match = re.match(r'(\d+)\.', filename)
    if match:
        return int(match.group(1))  # Return the number as an integer for numerical sorting
    return filename  # If no number is found, sort alphabetically

def create_index():
    # Get the current directory name as course title
    course_title = os.path.basename(os.getcwd())
    
    # Initialize markdown content with the course title as Heading 1
    markdown_content = f"# {course_title}\n\n"
    markdown_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Walk through directory
    for root, dirs, files in os.walk('.'):
        # Skip the root directory itself
        if root == '.':
            continue
            
        # Determine the heading level based on the depth of the folder
        depth = root.count(os.sep)
        heading_level = "#" * (depth + 1)  # Root subfolders are ##, deeper subfolders are ###, etc.
        
        # Get the folder name for the heading
        folder_name = os.path.basename(root)
        
        # Add the folder name as a heading
        markdown_content += f"{heading_level} {folder_name}\n\n"
        
        # Process files in this section
        video_files = [f for f in files if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]
        other_files = [f for f in files if not f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]
        
        if video_files:
            markdown_content += "Videos\n"
            # Sort video files numerically based on the number at the start of the filename
            sorted_videos = sorted(video_files, key=numerical_sort_key)
            for video in sorted_videos:
                # Create a relative path for the video
                relative_path = os.path.join(root, video).replace('\\', '/')
                # URL-encode the path for proper linking in Markdown
                encoded_path = urllib.parse.quote(relative_path)
                markdown_content += f"- [{video}]({encoded_path})\n"
            markdown_content += "\n"
        
        if other_files:
            markdown_content += "Resources\n"
            # Sort other files numerically as well
            sorted_resources = sorted(other_files, key=numerical_sort_key)
            for file in sorted_resources:
                # Create a relative path for other resources
                relative_path = os.path.join(root, file).replace('\\', '/')
                encoded_path = urllib.parse.quote(relative_path)
                markdown_content += f"- [{file}]({encoded_path})\n"
            markdown_content += "\n"
    
    # Write to "0. INDEX.md"
    with open('0. INDEX.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Index created successfully as '0. INDEX.md'")

if __name__ == "__main__":
    create_index()
