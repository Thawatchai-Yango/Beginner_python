def BubbleSort(a):
    i = 1
    N = len(a)
    for i in range(N):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
            a[j + 1] = key
            i = i + 1


a = [12, 15, 16, 11, 10, 50, 32, 65, 85, 37, 69, 72]
BubbleSort(a)
print(a)

#D:\musWORK\PythonProject\Bubble\venv\Scripts\python.exe D:/musWORK/PythonProject/Bubble/main.py
#[10, 11, 12, 15, 16, 32, 37, 50, 65, 69, 72, 85]