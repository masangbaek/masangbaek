def solution(keyinput, board):
    a, b = [0, 0]
    
    x = board[0] // 2
    y = board[1] // 2
    
    for i in keyinput :
        if i == 'up' :
            if b < y :
                b += 1
        elif i == 'down' :
            if b > -y :
                b -= 1
        elif i == 'left' :
            if a > -x :
                a -= 1
        elif i == 'right' :
            if a < x :
                a += 1
    
    return a, b