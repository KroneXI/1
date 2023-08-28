from conf.config import Config
# from db.db import Database
# from models.user import User

conf = Config()
DATABASE_USER = conf.get_config('DATABASE_USER')
DATABASE_PASSWORD = conf.get_config('DATABASE_PASSWORD')
DATABASE_NAME = conf.get_config('DATABASE_NAME')
DATABASE_URL = conf.get_config('DATABASE_URL').replace('DATABASE_USER', DATABASE_USER).replace('DATABASE_PASSWORD', DATABASE_PASSWORD).replace('DATABASE_NAME', DATABASE_NAME)

print(DATABASE_USER)
print(DATABASE_PASSWORD)
print(DATABASE_NAME)
print(DATABASE_URL)

# if __name__ == "__main__":    
#     db = Database(DATABASE_URL)
    
#     # Создание таблицы
#     db.create_tables()
    
#     def create_user(db):
#         db_user = User(username="user1", email="user1@example.com")
#         db.add(db_user)
#         db.commit()
#         db.refresh(db_user)
#         return db_user
    
#     new_user = db.execute(create_user)
#     print("Created User:", new_user.username, new_user.email)