def main():
    user_input = input()
    emoji = convert(user_input)
    print(emoji, end="")


def convert(text):
    text = text.strip().replace(":)", "🙂").replace(":(", "🙁")
    return text

main()


