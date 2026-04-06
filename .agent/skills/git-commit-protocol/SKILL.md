# Git Commit Protocol

This skill provides a structured methodology for systematizing and writing high-quality Git commits. It ensures that every change is logically grouped, properly categorized, and clearly explained.

## 📋 COMMIT SYSTEMATIZATION STEPS

Follow these steps for every commit or group of changes:

### STEP 1: Logical File Grouping
Identify and group modified files that belong to the same functional change or intent.
- **Files**: List the files to be included in this specific commit.
- **Purpose**: Briefly state why these files are being changed together.

### STEP 2: Intent Mapping (Conventional Commits)
Map the change intent to a standard prefix:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files

### STEP 3: Structured Writing
Draft the commit message using the following structure:
- **Title**: `<type>(<scope>): <short description>`
- **Body**: (Optional) Provide context, rationale, and "Steps" if needed for complex changes.

### STEP 4: Execution & Verification
1. `git add <files>`
2. `git commit -m "<message>"`
3. `git status` (Verify clean state)

---

## 💡 EXAMPLE WORKFLOW

**User**: "I fixed the login bug and updated the README."

**Systematization**:
- **Step 1**: Group files
  - Group A: `src/auth/login.ts` (The fix)
  - Group B: `README.md` (The docs)
- **Step 2**: Intent Mapping
  - Group A -> `fix`
  - Group B -> `docs`
- **Step 3**: Draft
  - Commit 1: `fix(auth): resolve session timeout during login`
  - Commit 2: `docs: update installation instructions in README`
