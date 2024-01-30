import secrets
import string

async def generate_password(length):
    # Определяем символы, из которых будет состоять пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль заданной длины
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Генерируем 9-значный сложный ключ пароля
    password = generate_password(15)
    await message.answer((f"Ключь успешно создан: {password} "))
    