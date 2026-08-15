# 待办清单（Todo CLI）

一个简单的 Python 命令行待办清单工具，用来练习 Git 和 GitHub 的完整工作流程。

## 功能

- `add "内容"`：添加待办事项
- `list`：查看全部待办
- `done 序号`：标记完成
- `remove 序号`：删除待办
- `clear`：清空所有待办
- `stats`：统计完成情况

## 使用方法

```
python todo.py add "写作业"
python todo.py list
python todo.py done 1
python todo.py clear
```

## 技术栈

- Python 3
- JSON 本地存储