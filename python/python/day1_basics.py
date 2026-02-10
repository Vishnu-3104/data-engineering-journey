# Day 1: Python Basics for Data Engineering

def greet(name):
    return f"Hello, {name}"

def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    print(greet("Data Engineer"))

    nums = [10, 20, 30, 40]
    print("Sum:", sum_numbers(nums))

    text = "Data engineering is about building reliable pipelines"
    print("Word count:", count_words(text))
