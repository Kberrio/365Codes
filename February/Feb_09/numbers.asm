section .data
    msg1 db 'Enter first number: ', 0
    msg2 db 'Enter second number: ', 0
    result_msg db 'The result is: ', 0

section .bss
    num1 resb 5
    num2 resb 5
    result resb 10

section .text
    global _start

_start:
    ; Print message asking for the first number
    mov eax, 4          ; System call for sys_write
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, msg1       ; Address of the message to print
    mov edx, 19         ; Number of bytes to write
    int 0x80            ; Call kernel

    ; Read first number from user
    mov eax, 3          ; System call for sys_read
    mov ebx, 0          ; File descriptor 0 is stdin
    mov ecx, num1       ; Buffer to store the input
    mov edx, 5          ; Maximum number of bytes to read
    int 0x80            ; Call kernel

    ; Convert ASCII input to integer
    mov eax, 0          ; Clear eax register
    mov ecx, num1       ; Address of the input buffer
    call ascii_to_int   ; Call the function to convert ASCII to integer
    mov [num1], eax     ; Store the integer in num1

    ; Print message asking for the second number
    mov eax, 4          ; System call for sys_write
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, msg2       ; Address of the message to print
    mov edx, 20         ; Number of bytes to write
    int 0x80            ; Call kernel

    ; Read second number from user
    mov eax, 3          ; System call for sys_read
    mov ebx, 0          ; File descriptor 0 is stdin
    mov ecx, num2       ; Buffer to store the input
    mov edx, 5          ; Maximum number of bytes to read
    int 0x80            ; Call kernel

    ; Convert ASCII input to integer
    mov eax, 0          ; Clear eax register
    mov ecx, num2       ; Address of the input buffer
    call ascii_to_int   ; Call the function to convert ASCII to integer
    mov [num2], eax     ; Store the integer in num2

    ; Add the two numbers
    mov eax, [num1]     ; Load first number into eax
    add eax, [num2]     ; Add second number to eax
    mov [result], eax   ; Store result in result variable

    ; Print the result
    mov eax, 4          ; System call for sys_write
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, result_msg ; Address of the result message
    mov edx, 15         ; Number of bytes to write
    int 0x80            ; Call kernel

    mov eax, 4          ; System call for sys_write
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, result     ; Address of the result variable
    call print_int      ; Call the function to print integer
    mov edx, 10         ; Number of bytes to write
    int 0x80            ; Call kernel

    ; Exit program
    mov eax, 1          ; System call for sys_exit
    xor ebx, ebx        ; Exit with return code 0
    int 0x80            ; Call kernel

; Function to convert ASCII input to integer
ascii_to_int:
    xor ebx, ebx        ; Clear ebx register
.next_digit:
    movzx edx, byte [ecx]  ; Load next byte from input buffer
    test dl, dl         ; Check for null terminator
    jz .done            ; If null terminator found, exit loop
    imul eax, ebx, 10   ; Multiply previous result by 10
    sub edx, '0'        ; Convert ASCII to integer
    add ebx, eax        ; Add to running total
    inc ecx             ; Move to next character
    jmp .next_digit     ; Repeat loop
.done:
    ret

; Function to print integer
print_int:
    ; Store original registers
    push eax
    push ebx
    push ecx
    push edx

    ; Initialize variables
    mov ebx, 10         ; Base 10 for integer conversion
    mov ecx, 0          ; Counter for number of digits

    ; Find number of digits
.find_digits:
    inc ecx             ; Increment digit counter
    mov edx, 0          ; Clear edx register
    div ebx             ; Divide number by 10
    test eax, eax       ; Check if quotient is zero
    jnz .find_digits    ; If not, repeat loop

    ; Print digits in reverse order
.print_digits:
    dec ecx             ; Decrement digit counter
    mov eax, edx        ; Move remainder into eax
    add eax, '0'        ; Convert to ASCII
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, eax        ; Move ASCII digit to ecx
    mov edx, 1          ; Number of bytes to write
    int 0x80            ; Call kernel
    test ecx, ecx       ; Check if digit counter is zero
    jnz .print_digits   ; If not, repeat loop

    ; Restore original registers
    pop edx
    pop ecx
    pop ebx
    pop eax
    ret
