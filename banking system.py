import json
from pathlib import Path
import time

path = Path("user.json")
users = []
current_user = None

def menu():
    """主菜单列表"""
    print("欢迎来到银行卡系统\n")
    title = '=' * 5 + '个人银行管理系统' + '=' * 5
    context = ("1.用户注册\n"
               "2.用户登录\n"
               "3.退出系统")
    print(title)
    print(context)
    print("请输入操作:")

def save_users():
    """保存文件"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False)


def load_users():
    global users
    try:
        with open(path, "r", encoding="utf-8") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []
        print("文件出现异常")
    except FileNotFoundError:
        users = []
        print("未找到用户文件，将自动创建")

def register():
    """用户注册"""
    global users
    while True:
        exists = False
        username = input("请输入用户名:")
        for user in users:
            if username in user["username"]:
                exists = True
                break
        if exists:
            print("用户名已存在，请重新输入！")
            continue
        password = input("请输入密码:")
        if not password:
            print("密码不能为空，请重新输入!")
            continue
        user = {
            "username": username,
            "password": password,
            "balance": 0,
            "history": [],
        }
        users.append(user)
        save_users()
        print("注册成功")
        input("按回车键以继续...")
        break

def login():
    """用户登录"""
    global current_user
    while True:
        username = input("请输入用户名")
        password = input("请输入密码")
        for user in users:
            if username == user["username"]:
                if password == user["password"]:
                    print("登录成功")
                    current_user = user
                    print(f"欢迎回来,{current_user['username']}")
                    input("按回车进入个人中心...")
                    user_main()
                    return
                else:
                    print("密码错误")
                    input("按回车键以继续...")
                    return

        print("用户不存在，请重新输入用户名")
        input("按回车键以继续...")

def user_menu():
    """用户登录后菜单"""
    global current_user
    print(f"===== 欢迎 {current_user['username']} 来到个人账户 =====")
    print("1.查询余额\n"
          "2.存款\n"
          "3.取款\n"
          "4.查看交易记录\n"
          "5.退出登录")

def query_balance():
    """查询余额"""
    global current_user
    print(f"{current_user['username']},您当前余额为:{current_user['balance']}")
    input("按回车键以继续...")

def deposit():
    """存款"""
    global current_user
    while True:
        try:
            money = int(input("输入您想存入的金额:"))
            now_time = time.strftime("%Y-%m-%d %H:%M:%S")
            if money <= 0:
                print("存款必须大于零")
                input("按回车键以继续...")
                continue
            else:
                current_user['balance'] += money
                current_user['history'].append(f"{now_time}存入{money}元")
                save_users()
                print("存款成功")
                input("按回车键以继续...")
                break
        except ValueError:
            print("请输入数字")
            input("按回车键以继续...")
            continue

def withdraw():
    """取款"""
    global current_user
    while True:
        try:
            money = int(input("输入您想取出的金额:"))
            now_time = time.strftime("%Y-%m-%d %H:%M:%S")
            if money <= 0:
                print("金额不能小于零")
                input("按回车键以继续...")
                continue
            elif money > current_user['balance']:
                print("余额不足")
                input("按回车键以继续...")
                continue
            else:
                current_user['balance'] -= money
                current_user['history'].append(f"{now_time}取出{money}元")
                save_users()
                print("取款成功")
                input("按回车键以继续...")
                break
        except ValueError:
            print("请输入数字")
            input("按回车键以继续...")
            continue

def transaction_record():
    """查看交易记录"""
    global current_user
    if not current_user['history']:
        print("暂无记录")
        return
    print('=' * 5 + '交易记录' + '=' * 5)
    for index, history in enumerate(current_user['history']):
        print(f"{index + 1}. {history}")
    input("按回车键以继续...")

def main():
    while True:
        menu()
        try:
            choice = int(input())
            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                print("谢谢使用")
                break
            else:
                print("请从1-3中选择!")
                input("按回车键以继续...")
        except ValueError:
            print("请输入数字!")
            input("按回车键以继续...")

def user_main():
    """用户操作"""
    while True:
        user_menu()
        try:
            choice = int(input("请输入操作"))
            if choice == 1:
                query_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                transaction_record()
            elif choice == 5:
                print("已退出登录，谢谢使用")
                break
            else:
                print("请输入1-5的数字")
        except ValueError:
            print("请输入数字")
            input("按回车键以继续...")

load_users()
if __name__ == '__main__':
    main()