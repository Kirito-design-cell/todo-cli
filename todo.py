"""一个简单的命令行待办清单工具"""
import json
import os
import sys

TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"已添加：{text}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("（还没有待办事项）")
        return
    for i, item in enumerate(todos, 1):
        mark = "v" if item["done"] else " "
        print(f"{i}. [{mark}] {item['text']}")


def done(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"完成：{todos[index - 1]['text']}")
    else:
        print("序号无效")


def remove(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"已删除：{removed['text']}")
    else:
        print("序号无效")


def clear_todos():
    todos = load_todos()
    if not todos:
        print("（还没有待办事项）")
        return
    save_todos([])
    print(f"已清空全部 {len(todos)} 条待办")




def stats():
    todos = load_todos()
    total = len(todos)
    done_count = sum(1 for t in todos if t["done"])
    print(f"总计 {total} 条，已完成 {done_count} 条，未完成 {total - done_count} 条")

def main():
    if len(sys.argv) < 2:
        print("用法：python todo.py <add|list|done|remove|clear|stats> [参数]")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "done" and len(sys.argv) > 2:
        done(int(sys.argv[2]))
    elif cmd == "remove" and len(sys.argv) > 2:
        remove(int(sys.argv[2]))
    elif cmd == "stats":
        stats()
    elif cmd == "clear":
        clear_todos()
    else:
        print("用法：python todo.py <add|list|done|remove|clear|stats> [参数]")


if __name__ == "__main__":
    main()