# Git Commit Protocol

This skill provides a structured methodology for systematizing and writing high-quality Git commits. It ensures that every change is logically grouped, properly categorized, and clearly explained.

## 📋 COMMIT SYSTEMATIZATION STEPS

Follow these steps for every commit or group of changes:

### STEP 1: Logical File Grouping

Identify and group modified files that belong to the same functional change or intent.

- **Files**: List the files to be included in this specific commit.
- **Purpose**: Briefly state why these files are being changed together.

### STEP 2: Intent Mapping (Conventional Commits)

Map the change intent to a standard prefix or custom intent:

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
- `init`: Project or module initialization
- `add`: Adding new files or dependencies
- `update`: Updating existing functionality or content
- `create`: Creating a new resource or component
- `delete`: Deleting files or resources
- `remove`: Removing functionality or code blocks
- `clean code`: Refactoring for readability and maintainable standards

### STEP 3: Structured Writing

Draft the commit message using the following structure:

- **Title**: `<type>(<scope>): <short description>`
- **Body**: (Optional) Provide context, rationale, and "Steps" if needed for complex changes.

### STEP 4: Verification & Approval (OPTIONAL)

If the user requests execution (e.g., "commit and push"), the system MUST:

1. **Show Verification**: Display a summary of the grouped files and the drafted commit message(s).
2. **Request Permission**: Ask the user for explicit confirmation (e.g., "Do you approve these commits?").
3. **Execute ONLY on Approval**: Perform the git commands only after the user says "Approve", "Yes", or similar.

**Note**: If approval is not granted, return to Step 1 or Step 3 for refinements.

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
