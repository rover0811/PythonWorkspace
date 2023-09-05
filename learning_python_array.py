import array

hi=array.array('i', [1, 2, 3, 4, 5])

print(hi, type(hi))

print(hi.buffer_info()) # (140714816, 5) -> (메모리 주소, 길이)를 반환한다.
