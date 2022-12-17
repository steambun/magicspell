# Magic Spell [![unit-tests](https://github.com/steambun/magicspell/actions/workflows/main.yml/badge.svg)](https://github.com/steambun/magicspell/actions/workflows/main.yml)

Spelling Program to improve Kids Spelling

## Developing Magic Spell

### Environment

1) Setting up virtual environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
2) Setup Pip
    ```sh
    python3 -m pip install --upgrade pip
    ```

3) Install Flask
    ```sh
    pip install flask
    ```

4) Run Flask
    ```sh
    flask run
    ```
### Testing

We use pytest for testing our python code

1. Install the framework
    ```sh
    pip install pytest
    ```

2. Update the requirements file to reflect the latest install
    ```sh
    python3 -m pip freeze > requirements.txt
    ```

3. Running test framework
    ```sh
    pytest
    ```

4. Familiarise yourself with framework with an [online tutorial](https://realpython.com/pytest-python-testing/)


