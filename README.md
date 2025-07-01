# Initial Setup (One-time per project):
## Install uv: If you haven't already, install uv on your system.
```curl -LsSf https://astral.sh/uv/install.sh | sh```

## Initialize Project: Navigate to your project directory and run uv init. This sets up basic configuration files (pyproject.toml, .python-version, etc.) for uv to manage your project.
```uv init```

## Create Virtual Environment: Create the project's isolated environment. This typically creates a .venv directory.
`uv venv`

## Add Dependencies: Install all your project's dependencies from a requirements.txt file (or add them one by one if you prefer). This also creates a uv.lock file.
`uv add -r requirements.txt`

## Clean Up (Optional but Recommended): Once uv has everything set up, you can remove your old venv directory and requirements.txt if they existed.
```
rm -rf venv
rm requirements.txt
```

# Day-to-Day Development Workflow:
## Activate Virtual Environment: Whenever you open a new terminal session to work on your project, you'll need to activate the uv virtual environment.
`source .venv/bin/activate`

(As mentioned before, many IDEs will do this automatically for you.)
## Run Your Project: Instead of python your_script.py, you'll use uv run.
`uv run main.py`

## If your project has an entry point defined in pyproject.toml, you might just use uv run directly.
Add New Dependencies: If your project needs new packages, use `uv add.`
`uv add new-package-name`

# Fork it
## Clone Your Fork: First, you'd clone your forked repository to your local machine.

```
git clone your-forked-repo-url
cd your-forked-repo-name
```

## Install uv (if you haven't already): Make sure you have uv installed on your system. If not, you'd install it:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

## Create the Virtual Environment: uv needs to create the isolated environment where your packages will live.

`uv venv`

This will create the .venv directory.

## Install Dependencies: Now, uv can install all the dependencies based on the uv.lock file. This ensures you get the exact versions the original author used.

`uv install`

Alternatively, you could use uv sync, which serves a similar purpose, ensuring your environment matches the lock file.

## Activate the Virtual Environment: Just like in your daily workflow, activate the environment to ensure your shell uses the correct Python interpreter and packages.

`source .venv/bin/activate`