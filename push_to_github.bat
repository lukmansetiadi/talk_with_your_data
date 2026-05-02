# 1. Initialize the directory as a Git repository
git init

# 2. Add all the files to the staging area
git add .

# 3. Create your first commit
git commit -m "Initial commit with Query Recommendations and Templates"

# 4. Link your local repository to your GitHub remote
# (Replace the URL below with your actual GitHub repository URL if it's different)
git remote add origin https://github.com/lukmansetiadi/talk_with_your_data.git

# 5. Rename the default branch to 'main' (if it isn't already)
git branch -M main

# 6. Push the code to GitHub! 
# (You might need to use --force if the remote repository already has files like the old README)
git push -u origin main --force