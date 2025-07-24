<!-- # makes a top-level heading (H1) -->
# git_Course_Test

<!-- --- creates a horizontal line -->
---

<!-- ## makes a section heading (H2) -->
## Git Configuration (Local Setup)

<!-- ### makes a third-level heading (H3) -->
### 1. Set your username
```bash
git config --global user.name "Your_User_Name"
```

### 2. Set your email
```bash
git config --global user.email "your_email@gmail.com"
```

---

## Create and Manage a Local Repository

### 1. Initialize your repository
```bash
git init
```

### 2. Add files to staging area
```bash
git add your_file_name.ext
# You can add any file type, e.g., .txt, .jpg, .xls, .py, .cpp, .mp4, etc.
```

### 3. Check repository status
```bash
git status
```
<!-- - Green: Added to staging (ready to be committed) -->
<!-- - Red: Not yet added to staging -->

### 4. Add all files to staging
```bash
git add --all
```

### 5. Commit your changes
```bash
git commit -m "Describe your change to the file"
```

### 6. View commit history
```bash
git log
```

---

## What is GitHub?

GitHub is a Git-based platform for hosting repositories, managing collaborative projects, and version control.

---

## Connect Local Repository to GitHub

### 1. Sign up or log in to [GitHub](https://github.com/)

### 2. On GitHub:  
- Create a new repository (**do not** initialize with README, .gitignore, or license if your local repo already has files).

### 3. In local terminal:  
#### Add README.md (optional, recommended)
```bash
git add README.md
git commit -m "Add README.md"
```

#### Create main branch
```bash
git branch -M main
```

#### Add remote repository (replace with your GitHub info)
```bash
git remote add origin https://github.com/Your_User/Your_Repository.git
```

#### Verify remote URL
```bash
git remote -v
```

### 4. Generate a Personal Access Token (for authentication)
- Go to your GitHub profile  
  - Profile > Settings  
  - Developer Settings (left sidebar)  
  - Personal access tokens > Tokens (classic)  
  - Generate new token

### 5. Push local repository to GitHub
```bash
git push -u origin main
```
<!-- Use your GitHub username/email and your generated token as password if prompted. -->

### 6. Pull changes from GitHub (if needed)
```bash
git pull origin main
```

---

## Markdown Quick Reference

<!-- Inline comments below will not appear in the rendered README, but help you remember! -->

<!-- #      → H1 (main title)
##     → H2 (section)
###    → H3 (subsection)
---    → horizontal line
`text` → inline code
```    → code block (multi-line)
-      → bulleted list
1.     → numbered list
[text](url) → link
![alt](image_url) → image
>      → blockquote
<!-- comment --> → hidden comment
\      → escape special character
-->

---

## Tips

- Use descriptive commit messages.
- Pull changes before pushing if collaborating with others to avoid conflicts.
- Protect your token—do not share it.

---

## License

[Add your license information here, if desired.]