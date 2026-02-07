# NOTE: Script for autentication/tokenization/password managemnt

from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "PANDA_PROJECT" # NOTE: You must change key!!!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """
    Hashing password
    
    Params: 
        - password (str):

    Return:
        - Hashed password
    """
    return pwd_context.hash(password)

def verify_password(password, hashed):
    """
    Check hashed password
    
    Params: 
        - password (str):
        - hased (str):

    Return:
        - ...
    """
    return pwd_context.verify(password, hashed)

def create_access_token(data: dict):
    """
    Create specific authentication token from dictionary data

    Params:
        - data (dict)

    Return:
        - Token (str)
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


if __name__ == '__main__':

    pwd = input('Digit your password here: ')
    hashed_pwd = hash_password(pwd)
    valid_hashed = verify_password(pwd, hashed_pwd)
    token = create_access_token({'pippo':10})
    print("This is your hashed password:", hashed_pwd)
    print('This is the verification:', valid_hashed)
    print('This is your token:', token)