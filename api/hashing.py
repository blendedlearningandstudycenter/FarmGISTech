from passlib.context import CryptContext

pwd_cxt =CryptContext(schemes=["pbkdf2_sha256", "des_crypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)