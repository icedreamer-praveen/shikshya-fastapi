from datetime import datetime, timedelta

from jose import JWTError, jwt

from app.account import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    """
    This function creates an access token by encoding a dictionary with an expiration time using a
    secret key and algorithm.
    
    :param data: A dictionary containing the data to be encoded in the access token
    :type data: dict
    :return: an encoded JSON Web Token (JWT) that contains the data passed as a parameter, along with an
    expiration time. The token is encoded using a secret key and an algorithm specified in the code.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    """
    This function verifies a JWT token by decoding it and checking if it contains a valid email payload.
    
    :param token: The token parameter is a string that represents a JSON Web Token (JWT). It is used to
    authenticate and authorize a user's access to protected resources in a web application
    :type token: str
    :param credentials_exception: `credentials_exception` is an exception that is raised when the
    credentials provided by the user are invalid or unauthorized. It is used in this function to handle
    any errors that occur during the decoding of the JWT token. If an error occurs, the function raises
    the `credentials_exception` to indicate that the user
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception