import re


# 邮箱验证函数
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print("邮箱格式有效！")
    else:
        print("邮箱格式无效，请重新输入。")


# 字符串大小写转换
def convert_case(text, to_upper=True):
    if to_upper:
        return text.upper()
    else:
        return text.lower()


# 去除前后空格
def remove_spaces(text):
    return text.strip()


# 主函数，展示如何使用
def main():
    print("欢迎使用用户输入处理工具！")
    print("请选择操作:")
    print("1. 邮箱验证")
    print("2. 大小写转换")
    print("3. 去除空格")

    choice = input("请输入选项 (1/2/3): ")

    if choice == '1':
        email = input("请输入邮箱地址: ")
        validate_email(email)
    elif choice == '2':
        text = input("请输入文本: ")
        case_choice = input("请选择转换方式 (1. 转大写, 2. 转小写): ")
        if case_choice == '1':
            print("转换后的文本: ", convert_case(text, True))
        else:
            print("转换后的文本: ", convert_case(text, False))
    elif choice == '3':
        text = input("请输入文本: ")
        print("去除空格后的文本: ", remove_spaces(text))
    else:
        print("无效的选项，请重新输入。")


if __name__ == "__main__":
    main()
