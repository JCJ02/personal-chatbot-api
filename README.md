# Meet Kimmy - My Digital Sidekick!

## Kimmy is a smart, friendly, and helpful AI chatbot designed to be my portfolio's ultimate tour guide. She's here to answer all your questions about me (JC) — from my work experience, technical skills, and portfolio projects to my goals, passions, and accolades.

# How to Setup My Personal ChatBot?

Learn more about the following technologies:
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Get Started (Skip Step 1-3 if Python already installed in your Desktop/Laptop):
### Step 1: You have to download the latest version of Python!
- [Download the Latest Version of Python](https://www.python.org/downloads/)

### Step 2: Install it!

### Step 3: On Windows:
- Open the Start Menu and search for Environment Variables.
- Click on <strong>Edit the system environment variables</strong>.
- In the System Properties window, click on the <strong>Environment variables</strong> button.
- Under <strong>System Variables</strong>, find the `Path` variable and click <strong>Edit</strong>.
- Add the following path (replace `PhthonXX` with your Python version, e.g., `Python313`):

```console
C:\Users\<YourUsername>\AppData\Roaming\Python\PythonXX\Scripts\
```

- Click <strong>OK</strong> to save the changes.

### Step 4: Cloning Repository
Use `git clone` to clone this repository:

```console
$ git clone https://github.com/JCJ02/invoice-api.git
```

or

Click `Clone or download` and `Download ZIP` to get this repo.

### Step 5: Virtual Environments (Recommended):

It is highly recommended to create a virtual environment for your project. This isolates the project dependencies and prevents conflicts with other Python projects.

1.  Create a virtual environment:

    ```console
    python -m venv venv
    ```

2.  Activate the virtual environment:

    * **On Windows:**

        ```console
        . venv/Scripts/activate
        ```

    * **On macOS and Linux:**

        ```console
        source venv/bin/activate
        ```

    * **Important:** Make sure your terminal prompt shows `(venv)` before proceeding.

### Step 6: Reinstall requirements.txt

    ```console
    pip freeze > requirements.txt
    ```
    
    or

    ```console
    pip 
    ```


### Step 7: TO RUN THE SERVER

    ```console
    python -m api.main
    ```

### TO RUN OTHER UTILITIES:

#### generateRandomText.py

    ```console
    python api/utilities/generateRandomText.py
    ```
