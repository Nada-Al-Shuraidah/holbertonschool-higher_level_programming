# Everything is Object - Python Deep Dive

This project is part of the Holberton School curriculum and focuses on understanding Python's object model — especially how variables behave when passed, assigned, compared, or mutated.

## 🔍 Objective

The goal of this project is to deeply understand:
- What Python objects are
- The difference between mutable and immutable types
- How identity and equality work (`is` vs `==`)
- How variables behave during assignment and function calls
- Aliasing and its side effects

This is foundational knowledge that affects all Python code, especially when debugging or writing clean, bug-free logic.

## 🧠 Key Concepts

- `type()` vs `id()`
- Mutable vs Immutable built-in types
- Variable assignment and memory reference
- Function argument passing in Python
- List operations and behavior
- String and tuple interning in CPython

## 📁 Project Structure

Each task is solved in a separate file:

- `0-answer.txt` to `28-answer.txt`: Short-answer questions (one-liner per file)
- `19-copy_list.py`: Function that returns a copy of a list
- `README.md`: This file
- `29-blog_post`: A blog post explaining key takeaways, to be shared on LinkedIn/Medium

## ✅ Requirements

- Python 3.8+
- All scripts start with `#!/usr/bin/python3`
- Files are executable
- Text files contain **only one line**, no extra spaces
- Code follows **pycodestyle** (v2.7.\*)

## 📝 Sample Question Example

```python
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> print(b)
[1, 2, 3, 4]  # because lists are mutable and b references the same object
```

## References

- [Python Official Documentation - Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python Official Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Real Python - Variables and Object References](https://realpython.com/pointers-in-python/)

## ✒️ Author
- Nada Al Shuraidah 
- GitHub: [Nada-Al-Shuraidah](https://github.com/Nada-Al-Shuraidah)
