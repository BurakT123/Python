def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Boş pozisyonun satır ve sütun indeksini döndür
    return None  # Boş pozisyon bulunamadıysa None döndür
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Tahtayı ekrana yazdıran fonksiyon
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Sudoku tahtasını çözen rekürsif fonksiyon

def solve_board(board):
     # Tahta dolu mu diye kontrol et
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos

     # Boş hücreye sayıları dene
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0
    
    return False

# Belirli bir hücreye sayı yerleştirilip yerleştirilemeyeceğini kontrol eden fonksiyon
def is_valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
# Sudoku tahtasını çöz
solve_board(board)

# Çözülmüş Sudoku tahtasını yazdır
print_board(board)