def check_password_strength(password):
    score = 0

    checks = [
        (lambda pwd: len(pwd) > 12, 2),
        (lambda pwd: any(char.isdigit() for char in pwd), 2),
        (lambda pwd: any(char.isalpha() for char in pwd), 2),
        (lambda pwd: any(char.isupper() for char in pwd), 1),
        (lambda pwd: any(char.islower() for char in pwd), 1),
        (lambda pwd: any(not char.isalnum() for char in pwd), 2)
    ]

    for check, points in checks:
        if check(password):
            score += points

    return score


def main():
    password = input("Введите пароль: ")
    score = check_password_strength(password)
    print(f"Рейтинг пароля: {score}")


if __name__ == '__main__':
    main()

