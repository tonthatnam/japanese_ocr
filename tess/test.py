from run import run

file_path = 'tests/test2.png'
text = run(file_path)
text = "\n".join(text)
with open('results/test_result.txt', 'w') as f:
    f.writelines(text)
