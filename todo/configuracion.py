from os import getenv
from dotenv import load_dotenv

def cargar_variables():
    load_dotenv()
    print(getenv("FLASK_APP"))

# if __name__ == "__main__":
    # print(getenv("FLASK_APP"))