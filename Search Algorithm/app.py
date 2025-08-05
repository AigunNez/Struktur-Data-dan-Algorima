from flask import Flask, render_template, request
import time
import math

app = Flask(__name__)

def linear_search(arr, x):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == x:
            return i, steps 
        
    return None, steps

def binary_search(arr, x):
    steps = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        steps += 1
        if arr[mid] == x:
            return mid, steps
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None, steps

def jump_search(arr, x):
    steps = 0
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0

    while arr[min(jump, n) - 1] < x:
        steps += 1
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return None, steps

    while arr[prev] < x:
        steps += 1
        prev += 1
        if prev == min(jump, n):
            return None, steps

    if arr[prev] == x:
        return prev, steps

    return None, steps

def interpolation_search(arr, x):   
    steps = 0
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        steps += 1
        if low == high:
            if arr[low] == x:
                return low, steps
            return None, steps

        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

        if arr[pos] == x:
            return pos, steps
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return None, steps

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try :
            array = list(map(int, request.form['array'].split(',')))
            target = int(request.form['target'])
            sorted_array = sorted(array)
            
            results = []
            for name, func, arr in [
                ("Linear Search", linear_search, array),
                ("Binary Search", binary_search, sorted_array),
                ("Jump Search", jump_search, sorted_array),
                ("Interpolation Search", interpolation_search, sorted_array)
            ]:
                start = time.time()
                index, steps = func(arr, target)
                results.append({
                    'name': name,
                    'found': index is not None,
                    'index': index,
                    'steps': steps,
                })
            result = results
        except Exception as e:
            result = f"Error: {str(e)}"
                
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
    