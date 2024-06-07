.model small
.stack 100h

.data
    board   db  '.', '.', '.',     ; Initial board state
            db  '.', '.', '.',
            db  '.', '.', '.'
    
    player  db  'X'                 ; Starting player
    prompt  db  'Enter move (row,col): $'
    winmsg  db  'Player X wins!$'
            db  'Player O wins!$'
            db  'It''s a draw!$'

.code
    mov ax, @data
    mov ds, ax

    mov ah, 09h                     ; Display board
    lea dx, board
    int 21h

    mov cx, 9                       ; Number of moves allowed
    mov bx, 0                       ; Counter for moves

game_loop:
    ; Get player move
    mov ah, 09h
    lea dx, prompt
    int 21h

    mov ah, 01h                     ; Input character
    int 21h
    sub al, '0'                     ; Convert ASCII digit to numeric value
    mov bl, al                      ; Store row

    mov ah, 01h                     ; Input character
    int 21h
    sub al, '0'                     ; Convert ASCII digit to numeric value
    mov bh, al                      ; Store column

    ; Calculate index
    mov dl, 3
    mul dl
    add bl, bh

    ; Check if cell is empty
    mov al, board[bl]
    cmp al, '.'                     ; Check if cell is empty
    jne invalid_move

    ; Place player symbol on the board
    mov al, player
    mov board[bl], al

    ; Display updated board
    mov ah, 09h
    lea dx, board
    int 21h

    ; Check for win or draw
    call check_win
    cmp ax, 1                       ; Player X wins
    je player_x_win
    cmp ax, 2                       ; Player O wins
    je player_o_win
    cmp bx, 9                       ; Draw
    je draw

    ; Switch player
    cmp player, 'X'
    je switch_to_o
    jmp switch_to_x

switch_to_o:
    mov player, 'O'
    jmp game_loop

switch_to_x:
    mov player, 'X'
    jmp game_loop

invalid_move:
    mov ah, 09h
    lea dx, invalid_msg
    int 21h
    jmp game_loop

player_x_win:
    mov ah, 09h
    lea dx, winmsg
    int 21h
    jmp end_game

player_o_win:
    mov ah, 09h
    lea dx, winmsg + 12
    int 21h
    jmp end_game

draw:
    mov ah, 09h
    lea dx, winmsg + 24
    int 21h

end_game:
    mov ah, 4Ch
    int 21h

; Function to check for a win or draw
check_win:
    ; Horizontal lines
    mov cx, 0
    mov dx, 3
    mov ax, board
    call check_line
    cmp ax, 'X'
    je player_x_win
    cmp ax, 'O'
    je player_o_win

    ; Vertical lines
    mov cx, 0
    mov dx, 1
    mov ax, board
    call check_line
    cmp ax, 'X'
    je player_x_win
    cmp ax, 'O'
    je player_o_win

    ; Diagonal lines
    mov cx, 0
    mov dx, 4
    mov ax, board
    call check_line
    cmp ax, 'X'
    je player_x_win
    cmp ax, 'O'
    je player_o_win

    ; Check for draw
    mov ax, 0
    ret

; Function to check a line for a win
check_line:
    mov bx, 0
line_loop:
    cmp bx, 2
    jg line_done

    add ax, cx
    inc bx
    add ax, dx
    inc bx

    add ax, 2
    add ax, dx
    inc bx

    add ax, 4
    add ax, dx
    inc bx

    add ax, 6
    add ax, dx
    inc bx
    jmp line_loop

line_done:
    ret

invalid_msg db 'Invalid move! Try again.$'

endgame

