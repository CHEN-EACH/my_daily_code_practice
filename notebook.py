import json
from pathlib import Path
import time

notebooks = []
path = Path("notes.json")

def menu():
    """展示记事本功能"""
    title = '=' * 5 + '个人记事本' + '=' * 5
    context = ("1.添加笔记\n"
               "2.查看所有笔记\n"
               "3.删除笔记\n"
               "4.保存笔记到文件\n"
               "5.退出程序")
    print(title)
    print(context)
    print('=' * len(title))

def add_note(list):
    """添加笔记"""
    try:
        content = input("请输入你想添加的笔记:")
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        note = {
            "content": content,
            "time": now_time,
        }
        list.append(note)
        print("笔记添加成功！")
        input("按回车键以继续...")
    except KeyboardInterrupt:
        print("添加笔记失败，请重新添加！")
        input("按回车键以继续...")

def view_note(list):
    """查看所有笔记"""
    if not list:
        print("暂无笔记，请先添加!")
        input("按回车键以继续...")
    else:
        print("=" * 5 + "所有笔记" + "=" * 5)
        for index, note in enumerate(list):#enumerate可以自动生成序号，不过是从0开始
            print(f"{index + 1}. {note['time']} {note['content']}")
        input("按回车键以继续...")

def delete_note(list):
    """删除笔记"""
    if not list:
        print("暂无笔记可以删除")
        input("按回车键以继续...")
    else:
        print("=" * 5 + "所有笔记" + "=" * 5)
        for index, note in enumerate(list):
            print(f"{index + 1}. {note['time']} {note['content']}")
        try:
            i = int(input("输入你想要删除的笔记序号:"))
        except ValueError:
            print("请输入有效数字")
            input("按回车键以继续...")
            return
        try:
            del list[i - 1]
            print("删除成功！")
            input("按回车键以继续...")
        except IndexError:
            print("序号不存在，请输入正确数字")
            input("按回车键以继续...")

def save_note(list):
    """将笔记保存在文件中"""
    with open(path, "w",encoding = "utf-8") as f:
        json.dump(list, f, ensure_ascii = False, indent = 4)

    print("文件保存成功")
    input("按回车键以继续...")

def load_note():
    """打开笔记本"""
    global notebooks
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                notebooks = json.load(f)
                print("已加载历史笔记")
        except json.JSONDecodeError:
            notebooks = []
            print("笔记文件为空或损坏，已重置")

def main():
    while True:
        menu()
        try:
            choice = int(input("请选择你的操作:"))
            if choice == 1:
                add_note(notebooks)
            elif choice == 2:
                view_note(notebooks)
            elif choice == 3:
                delete_note(notebooks)
            elif choice == 4:
                save_note(notebooks)
            elif choice == 5:
                print("谢谢使用")
                break
            else:
                print("请输入正确的数字！！！")
                input("按回车键以继续...")
        except ValueError:
            print("请输入数字")
            input("按回车键以继续...")

load_note()
if __name__ == '__main__':
    main()