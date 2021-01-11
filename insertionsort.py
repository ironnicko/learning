def insert(arr: list) -> list: 
    for i in range(1, len(arr)):
        keyframe = arr[i]
        j = i-1
        for _ in range(1, j):
            if keyframe < arr[j]:
                keyframe = arr[j]
        
a=  [i for i in range(120, 0, -1)]
insert(a)
        
    

