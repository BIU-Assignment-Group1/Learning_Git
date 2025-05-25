"""
# 1. Clone a remote repository (get a copy of the project from GitHub or similar)
# Replace <repo-url> with the actual repository URL
git clone <repo-url>

# 2. Change directory into the cloned repository
# Replace <project-folder> with your project's folder name
cd <project-folder>

# 3. (Optional) If starting a new project, initialize it as a Git repository
git init

# 4. Set your Git username and email (only needed once per device)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 5. Pull the latest changes from the remote repository (to make sure it’s up to date)
# Replace <branch-name> with the branch you want to update (usually "main" or "master")
git pull origin <branch-name>

# 6. Create and switch to a new branch for a feature you're working on
# Replace <feature-name> with a short name for your new feature
git checkout -b <feature-name>

# 7. Check the current status of your files (to see what has changed)
git status

# 8. Add files you want to include in your next commit
# Use `.` to add all changed files or replace `.` with a specific file name
git add .

# 9. Commit your changes with a message
# Replace "Your message here" with a short description of your change
git commit -m "Your message here"

# 10. Push your branch and changes to the remote repository
# This uploads your changes to GitHub (or other remote)
git push origin <feature-name>

"""

print("Hello Welcome to Git World")