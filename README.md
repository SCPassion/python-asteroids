# Installation guide:

## Step 1: Create a virtual environment at the top level of your project

```bash
uv init your-project-name
cd your-project-name
```

## Step 2: Create a virtual environment:
```bash
uv venv
```

## Step 3: Open a virtual environment

```bash
source .venv/bin/activate
```

## Step 3: import the python package

```bash
uv add -r requirements.txt
or 
uv add pygame==2.6.1
```

# When on a fresh new start:

`source venv/bin/activate`

# Run

```bash
uv run -m pygame
```
