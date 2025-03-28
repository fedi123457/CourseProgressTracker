# Obsidian-course-index
The Indexer` is a Python script that generates a Markdown index file (`0. INDEX.md`) for video courses.
# The Indexer

## Overview
`The Indexer` is a Python script that generates a Markdown index file (`0. INDEX.md`) for Udemy courses, optimized for use in Obsidian. It scans a course folder, organizes videos and resources from subfolders, and creates a structured index with clickable links to the files. The script is designed to help learners keep track of course materials by providing a centralized index with direct access to videos and resources.

### Features
- Generates a Markdown file named `0. INDEX.md` that appears at the top of the folder when sorted alphabetically.
- Uses the exact folder names as headings (e.g., `## 1. Introduction To The Course`).
- Lists videos and resources in bullet lists without additional numbering, preserving the original file names.
- Sorts files numerically based on the numbers in their names (e.g., "1. Video.mp4", "2. Video.mp4", ..., "10. Video.mp4").
- Creates relative links to files, allowing seamless integration with Obsidian (no security prompts for `file://` links).
- Supports nested folder structures with appropriate heading levels (H2 for first-level subfolders, H3 for deeper subfolders, etc.).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/the-indexer.git
   cd the-indexer
