import os
import tempfile
import unittest
import todo


class TodoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.tmp.close()
        todo.TODO_FILE = self.tmp.name

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.unlink(self.tmp.name)

    def test_add_and_list(self):
        todo.add("买牛奶")
        todo.add("写作业")
        todos = todo.load_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0]["text"], "买牛奶")

    def test_done(self):
        todo.add("学 git")
        todo.done(1)
        todos = todo.load_todos()
        self.assertTrue(todos[0]["done"])

    def test_remove(self):
        todo.add("清理")
        todo.remove(1)
        self.assertEqual(todo.load_todos(), [])

    def test_clear(self):
        todo.add("a")
        todo.add("b")
        todo.clear_todos()
        self.assertEqual(todo.load_todos(), [])

    def test_stats(self):
        todo.add("a")
        todo.add("b")
        todo.done(1)
        todo.stats()


if __name__ == "__main__":
    unittest.main()