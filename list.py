import json
from pathlib import Path

datas = {
    'tasks' : [],
    'notes' : []
}
path = Path("data.json")

def save_datas():
    """保存数据"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)

def load_datas():
    """加载数据"""
    global datas
    try:
        with open(path, "r", encoding="utf-8") as f:
            datas = json.load(f)
    except FileNotFoundError:
        datas = {
            'tasks': [],
            'notes': []
        }
    except json.JSONDecodeError:
        datas = {
            'tasks': [],
            'notes': []
        }

def menu():
    """系统菜单"""
    print('=' * 5 + '清单事项' + '=' * 5)
    print("1.待办事项管理\n"
          "2.备忘录管理\n"
          "3.退出系统")

def tasks_menu():
    """待办事项子菜单"""
    print('=' * 5 + '待办事项管理' + '=' * 5)
    print("1.查看所有待办\n"
          "2.新增待办\n"
          "3.标记完成\n"
          "4.删除待办\n"
          "5.返回主菜单\n")

def notes_menu():
    """备忘录子菜单"""
    print('=' * 5 + '备忘事项管理' + '=' * 5)
    print("1.查看所有笔记\n"
          "2.新增笔记\n"
          "3.删除笔记\n"
          "4.返回主菜单")

def _view_tasks():
    """查看待办列表"""
    if not datas['tasks']:
        print("暂无待办事项")
    for index, task in enumerate(datas['tasks']):
        if task['completed'] == False:
            status = '❌ 未完成'
        else:
            status = '✅ 已完成'
        print(f"{index + 1}. {task['content']}. 完成情况:{status}")


def _add_task():
    """新增待办"""
    task = input("输入新的待办:")
    tasks = {
        'content': task,
        'completed': False
    }
    datas['tasks'].append(tasks)
    save_datas()
    print("添加成功")
    input("按回车键以继续...")

def marked_tasks():
    """标记任务已经完成"""
    _view_tasks()
    index = int(input("请输入已经完成任务序号:"))
    try:
        task = datas['tasks'][index - 1]['completed'] = True
        save_datas()
        print("标记成功")
        input("按回车键以继续...")
    except IndexError:
        print("序号输入错误")
        input("按回车键以继续...")

def delete_task():
    """删除待办事项"""
    _view_tasks()
    index = int(input("输入要删除的待办序号:"))
    try:
        del datas['tasks'][index - 1]
        save_datas()
        print("删除成功")
        input("按回车键以继续...")
    except IndexError:
        print("序号错误")
        input("按回车键以继续...")

def _view_notes():
    """查看笔记"""
    if not datas['notes']:
        print("暂无备忘记录")
    for index, note in enumerate(datas['notes']):
        print(f"{index + 1}. {note['title']}: {note['content']}")


def _add_note():
    """新增笔记"""
    title = input("请输入笔记标题:")
    content = input("请输入笔记内容:")
    note = {
        'title': title,
        'content': content
    }
    datas['notes'].append(note)
    save_datas()
    print("添加成功")
    input("按回车键以继续...")

def delete_note():
    """删除笔记"""
    _view_notes()
    index = int(input("输入你想删除的笔记的序号:"))
    try:
        del datas['notes'][index - 1]
        save_datas()
        print("删除成功")
        input("按回车键以继续...")
    except IndexError:
        print("序号错误")
        input("按回车键以继续...")

def main():
    while True:
        menu()
        try:
            choice = int(input("请输入操作:"))
            if choice == 1:
                while True:
                    tasks_menu()
                    try:
                        opt_1 = int(input("请选择操作:"))
                        if opt_1 == 1:
                            _view_tasks()
                            input("按回车键以继续...")
                        elif opt_1 == 2:
                            _add_task()
                        elif opt_1 == 3:
                            marked_tasks()
                        elif opt_1 == 4:
                            delete_task()
                        elif opt_1 == 5:
                            print("谢谢使用")
                            break
                        else:
                            print("请输入1-5的数字")
                            input("按回车键以继续...")
                    except ValueError:
                        print("请输入数字")
                        input("按回车键以继续...")
            elif choice == 2:
                while True:
                    notes_menu()
                    try:
                        opt_2 = int(input("请选择操作:"))
                        if opt_2 == 1:
                            _view_notes()
                            input("按回车键以继续...")
                        elif opt_2 == 2:
                            _add_note()
                        elif opt_2 == 3:
                            delete_note()
                        elif opt_2 == 4:
                            print("谢谢使用")
                            break
                        else:
                            print("请输入1-4的数字")
                            input("按回车键以继续...")
                    except ValueError:
                        print("请输入数字")
                        input("按回车键以继续...")
            elif choice == 3:
                print("谢谢使用")
                break
            else:
                print("请输入1-3的数字")
                input("按回车键以继续...")
        except ValueError:
            print("请输入数字")
            input("按回车键以继续...")

load_datas()

if __name__ == '__main__':
    main()