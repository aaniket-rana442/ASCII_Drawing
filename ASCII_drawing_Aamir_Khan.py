# ASCII drawing of Aamir Khan

rows = 60
cols = 100
print("\n----------------------------------------------- Aamir Khan -----------------------------------------------\n")
r = 0
while r < rows:
    line = ""
    c = 0
    while c < cols:
        if r == 0:
            if c < 2:
                ch = '*'
            elif c < 6:
                ch = '.'
            elif c < 17:
                ch = ' '
            elif c < 18:
                ch = '.'
            elif c < 19:
                ch = ':'
            elif c < 20:
                ch = '#'
            elif c < 78:
                ch = '@'
            elif c < 79:
                ch = '&'
            elif c < 81:
                ch = '.'
            elif c < 99:
                ch = ' '
            else:
                ch = '.'
        elif r == 1:
            if c < 2:
                ch = '*'
            elif c < 5:
                ch = '.'
            elif c < 15:
                ch = ' '
            elif c < 16:
                ch = '*'
            elif c < 17:
                ch = '&'
            elif c < 18:
                ch = '#'
            elif c < 80:
                ch = '@'
            elif c < 81:
                ch = '#'
            elif c < 82:
                ch = '*'
            elif c < 84:
                ch = '.'
            else:
                ch = ' '
        elif r == 2:
            if c < 1:
                ch = '*'
            elif c < 5:
                ch = '.'
            elif c < 12:
                ch = ' '
            elif c < 13:
                ch = '.'
            elif c < 14:
                ch = '*'
            elif c < 15:
                ch = '8'
            elif c < 16:
                ch = '#'
            elif c < 79:
                ch = '@'
            elif c < 80:
                ch = '#'
            elif c < 81:
                ch = '&'
            elif c < 82:
                ch = '*'
            elif c < 84:
                ch = '.'
            else:
                ch = ' '
        elif r == 3:
            if c < 1:
                ch = '*'
            elif c < 4:
                ch = '.'
            elif c < 10:
                ch = ' '
            elif c < 11:
                ch = '.'
            elif c < 12:
                ch = '&'
            elif c < 13:
                ch = '#'
            elif c < 80:
                ch = '@'
            elif c < 81:
                ch = '#'
            elif c < 82:
                ch = '8'
            elif c < 83:
                ch = '&'
            elif c < 84:
                ch = '*'
            elif c < 86:
                ch = '.'
            else:
                ch = ' '
        elif r == 4:
            if c < 1:
                ch = '*'
            elif c < 4:
                ch = '.'
            elif c < 9:
                ch = ' '
            elif c < 10:
                ch = '.'
            elif c < 11:
                ch = '#'
            elif c < 83:
                ch = '@'
            elif c < 84:
                ch = '#'
            elif c < 85:
                ch = '&'
            elif c < 86:
                ch = '.'
            else:
                ch = ' '
        elif r == 5:
            if c < 4:
                ch = '.'
            elif c < 8:
                ch = ' '
            elif c < 9:
                ch = '.'
            elif c < 10:
                ch = '#'
            elif c < 88:
                ch = '@'
            elif c < 89:
                ch = '#'
            elif c < 90:
                ch = ':'
            else:
                ch = ' '
        elif r == 6:
            if c < 4:
                ch = '.'
            elif c < 7:
                ch = ' '
            elif c < 8:
                ch = '.'
            elif c < 9:
                ch = '8'
            elif c < 27:
                ch = '@'
            elif c < 29:
                ch = '#'
            elif c < 37:
                ch = '8'
            elif c < 38:
                ch = '#'
            elif c < 41:
                ch = '8'
            elif c < 43:
                ch = '#'
            elif c < 45:
                ch = '8'
            elif c < 48:
                ch = '#'
            elif c < 60:
                ch = '@'
            elif c < 64:
                ch = '#'
            elif c < 66:
                ch = '@'
            elif c < 71:
                ch = '#'
            elif c < 74:
                ch = '8'
            elif c < 75:
                ch = '#'
            elif c < 91:
                ch = '@'
            elif c < 92:
                ch = '.'
            else:
                ch = ' '
        elif r == 7:
            if c < 3:
                ch = '.'
            elif c < 7:
                ch = ' '
            elif c < 8:
                ch = '8'
            elif c < 22:
                ch = '@'
            elif c < 23:
                ch = '#'
            elif c < 24:
                ch = '8'
            elif c < 27:
                ch = '&'
            elif c < 34:
                ch = ':'
            elif c < 43:
                ch = '*'
            elif c < 44:
                ch = ':'
            elif c < 45:
                ch = '*'
            elif c < 46:
                ch = ':'
            elif c < 53:
                ch = ':'
            elif c < 57:
                ch = '&'
            elif c < 76:
                ch = ':'
            elif c < 77:
                ch = '&'
            elif c < 78:
                ch = '8'
            elif c < 92:
                ch = '@'
            elif c < 93:
                ch = ':'
            else:
                ch = ' '
        elif r == 8:
            if c < 3:
                ch = '.'
            elif c < 6:
                ch = ' '
            elif c < 7:
                ch = '.'
            elif c < 8:
                ch = '#'
            elif c < 21:
                ch = '@'
            elif c < 22:
                ch = '8'
            elif c < 25:
                ch = ':'
            elif c < 68:
                ch = '*'
            elif c < 71:
                ch = ':'
            elif c < 73:
                ch = '*'
            elif c < 76:
                ch = ':'
            elif c < 77:
                ch = '&'
            elif c < 78:
                ch = '8'
            elif c < 91:
                ch = '@'
            elif c < 92:
                ch = '*'
            else:
                ch = ' '
        elif r == 9:
            if c < 3:
                ch = '.'
            elif c < 6:
                ch = ' '
            elif c < 7:
                ch = '*'
            elif c < 20:
                ch = '@'
            elif c < 21:
                ch = '#'
            elif c < 22:
                ch = '8'
            elif c < 24:
                ch = ':'
            elif c < 36:
                ch = '*'
            elif c < 38:
                ch = '.'
            elif c < 41:
                ch = '*'
            elif c < 48:
                ch = '.'
            elif c < 75:
                ch = '*'
            elif c < 78:
                ch = ':'
            elif c < 79:
                ch = '&'
            elif c < 80:
                ch = '8'
            elif c < 93:
                ch = '@'
            else:
                ch = ' '
        elif r == 10:
            if c < 3:
                ch = '.'
            elif c < 6:
                ch = ' '
            elif c < 7:
                ch = '*'
            elif c < 8:
                ch = '#'
            elif c < 18:
                ch = '@'
            elif c < 19:
                ch = '#'
            elif c < 20:
                ch = '8'
            elif c < 21:
                ch = ':'
            elif c < 27:
                ch = '*'
            elif c < 29:
                ch = '.'
            elif c < 31:
                ch = '*'
            elif c < 49:
                ch = '.'
            elif c < 51:
                ch = '*'
            elif c < 59:
                ch = '.'
            elif c < 72:
                ch = '*'
            elif c < 77:
                ch = ':'
            elif c < 79:
                ch = '&'
            elif c < 80:
                ch = '8'
            elif c < 81:
                ch = '#'
            elif c < 91:
                ch = '@'
            elif c < 92:
                ch = '.'
            else:
                ch = ' '
        elif r == 11:
            if c < 2:
                ch = '.'
            elif c < 6:
                ch = ' '
            elif c < 7:
                ch = '*'
            elif c < 8:
                ch = '#'
            elif c < 18:
                ch = '@'
            elif c < 19:
                ch = '8'
            elif c < 20:
                ch = '&'
            elif c < 21:
                ch = ':'
            elif c < 24:
                ch = '*'
            elif c < 58:
                ch = '.'
            elif c < 70:
                ch = '*'
            elif c < 76:
                ch = ':'
            elif c < 77:
                ch = '&'
            elif c < 79:
                ch = '8'
            elif c < 81:
                ch = '#'
            elif c < 88:
                ch = '@'
            elif c < 90:
                ch = '#'
            elif c < 92:
                ch = '@'
            elif c < 100:
                ch = '.'
            else:
                ch = '.'
        elif r == 12:
            if c < 2:
                ch = '.'
            elif c < 7:
                ch = ' '
            elif c < 8:
                ch = ':'
            elif c < 9:
                ch = '#'
            elif c < 19:
                ch = '@'
            elif c < 20:
                ch = '8'
            elif c < 21:
                ch = ':'
            elif c < 25:
                ch = '*'
            elif c < 58:
                ch = '.'
            elif c < 70:
                ch = '*'
            elif c < 76:
                ch = ':'
            elif c < 78:
                ch = '&'
            elif c < 79:
                ch = '8'
            elif c < 80:
                ch = '#'
            elif c < 91:
                ch = '@'
            elif c < 100:
                ch = '.'
            else:
                ch = '.'
        elif r == 13:
            if c < 2:
                ch = '.'
            elif c < 7:
                ch = ' '
            elif c < 8:
                ch = '*'
            elif c < 9:
                ch = '#'
            elif c < 19:
                ch = '@'
            elif c < 20:
                ch = '&'
            elif c < 21:
                ch = ':'
            elif c < 26:
                ch = '*'
            elif c < 57:
                ch = '.'
            elif c < 69:
                ch = '*'
            elif c < 76:
                ch = ':'
            elif c < 79:
                ch = '&'
            elif c < 80:
                ch = '8'
            elif c < 81:
                ch = '#'
            elif c < 90:
                ch = '@'
            elif c < 100:
                ch = '.'
            else:
                ch = '.'
        elif r == 14:
            if c < 2:
                ch = '.'
            elif c < 8:
                ch = ' '
            elif c < 9:
                ch = '*'
            elif c < 10:
                ch = '#'
            elif c < 16:
                ch = '@'
            elif c < 17:
                ch = '#'
            elif c < 18:
                ch = '8'
            elif c < 19:
                ch = '&'
            elif c < 20:
                ch = ':'
            elif c < 23:
                ch = '*'
            elif c < 61:
                ch = '.'
            elif c < 71:
                ch = '*'
            elif c < 81:
                ch = ':'
            elif c < 82:
                ch = '&'
            elif c < 83:
                ch = '8'
            elif c < 84:
                ch = '#'
            elif c < 89:
                ch = '@'
            elif c < 90:
                ch = ':'
            else:
                ch = ' '
        elif r == 15:
            if c < 2:
                ch = '.'
            elif c < 9:
                ch = ' '
            elif c < 10:
                ch = '*'
            elif c < 11:
                ch = '#'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = '#'
            elif c < 17:
                ch = '8'
            elif c < 18:
                ch = ':'
            elif c < 21:
                ch = '*'
            elif c < 23:
                ch = '.'
            elif c < 24:
                ch = '*'
            elif c < 62:
                ch = '.'
            elif c < 74:
                ch = '*'
            elif c < 80:
                ch = ':'
            elif c < 82:
                ch = '&'
            elif c < 83:
                ch = '8'
            elif c < 87:
                ch = '@'
            elif c < 88:
                ch = '&'
            else:
                ch = ' '
        elif r == 16:
            if c < 2:
                ch = '.'
            elif c < 5:
                ch = ' '
            elif c < 8:
                ch = '.'
            elif c < 10:
                ch = ' '
            elif c < 11:
                ch = '&'
            elif c < 12:
                ch = '#'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = '8'
            elif c < 17:
                ch = '*'
            elif c < 27:
                ch = '.'
            elif c < 29:
                ch = '*'
            elif c < 34:
                ch = '.'
            elif c < 41:
                ch = ' '
            elif c < 52:
                ch = '.'
            elif c < 55:
                ch = ' '
            elif c < 65:
                ch = '.'
            elif c < 67:
                ch = '*'
            elif c < 68:
                ch = ':'
            elif c < 70:
                ch = '&'
            elif c < 71:
                ch = '8'
            elif c < 73:
                ch = '#'
            elif c < 74:
                ch = '8'
            elif c < 76:
                ch = '&'
            elif c < 82:
                ch = ':'
            elif c < 84:
                ch = '&'
            elif c < 85:
                ch = '#'
            elif c < 87:
                ch = '@'
            elif c < 88:
                ch = '&'
            elif c < 89:
                ch = ' '
            elif c < 90:
                ch = '.'
            elif c < 92:
                ch = ':'
            elif c < 94:
                ch = '&'
            elif c < 95:
                ch = ':'
            else:
                ch = ' '
        elif r == 17:
            if c < 2:
                ch = '.'
            elif c < 3:
                ch = ' '
            elif c < 4:
                ch = '.'
            elif c < 10:
                ch = '*'
            elif c < 11:
                ch = ':'
            elif c < 12:
                ch = '#'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = ':'
            elif c < 24:
                ch = '.'
            elif c < 25:
                ch = '*'
            elif c < 26:
                ch = ':'
            elif c < 27:
                ch = '&'
            elif c < 29:
                ch = '8'
            elif c < 32:
                ch = '&'
            elif c < 34:
                ch = ':'
            elif c < 38:
                ch = '*'
            elif c < 44:
                ch = '.'
            elif c < 47:
                ch = ' '
            elif c < 51:
                ch = '.'
            elif c < 54:
                ch = ' '
            elif c < 60:
                ch = '.'
            elif c < 62:
                ch = '*'
            elif c < 63:
                ch = ':'
            elif c < 64:
                ch = '&'
            elif c < 65:
                ch = '8'
            elif c < 67:
                ch = '#'
            elif c < 74:
                ch = '@'
            elif c < 75:
                ch = '#'
            elif c < 76:
                ch = '@'
            elif c < 77:
                ch = '#'
            elif c < 78:
                ch = '&'
            elif c < 84:
                ch = ':'
            elif c < 85:
                ch = '#'
            elif c < 87:
                ch = '@'
            elif c < 88:
                ch = '8'
            elif c < 94:
                ch = '&'
            elif c < 95:
                ch = '8'
            elif c < 96:
                ch = '.'
            else:
                ch = ' '
        elif r == 18:
            if c < 1:
                ch = '.'
            elif c < 3:
                ch = ' '
            elif c < 7:
                ch = '*'
            elif c < 10:
                ch = '.'
            elif c < 11:
                ch = '*'
            elif c < 12:
                ch = ':'
            elif c < 13:
                ch = '#'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = '&'
            elif c < 23:
                ch = '.'
            elif c < 24:
                ch = ':'
            elif c < 28:
                ch = '8'
            elif c < 29:
                ch = '#'
            elif c < 30:
                ch = '8'
            elif c < 31:
                ch = '#'
            elif c < 34:
                ch = '@'
            elif c < 35:
                ch = '#'
            elif c < 36:
                ch = '@'
            elif c < 38:
                ch = '#'
            elif c < 39:
                ch = '8'
            elif c < 40:
                ch = '&'
            elif c < 41:
                ch = ':'
            elif c < 44:
                ch = '*'
            elif c < 53:
                ch = '.'
            elif c < 55:
                ch = '*'
            elif c < 57:
                ch = ':'
            elif c < 59:
                ch = '&'
            elif c < 60:
                ch = '8'
            elif c < 61:
                ch = '#'
            elif c < 62:
                ch = '@'
            elif c < 64:
                ch = '#'
            elif c < 65:
                ch = '8'
            elif c < 68:
                ch = '&'
            elif c < 74:
                ch = ':'
            elif c < 75:
                ch = '&'
            elif c < 76:
                ch = '8'
            elif c < 78:
                ch = '&'
            elif c < 82:
                ch = ':'
            elif c < 83:
                ch = '#'
            elif c < 84:
                ch = '@'
            elif c < 85:
                ch = '#'
            elif c < 86:
                ch = '&'
            elif c < 89:
                ch = ':'
            elif c < 91:
                ch = '&'
            elif c < 93:
                ch = ':'
            else:
                ch = ' '
        elif r == 19:
            if c < 1:
                ch = '.'
            elif c < 3:
                ch = ' '
            elif c < 4:
                ch = '.'
            elif c < 6:
                ch = '*'
            elif c < 12:
                ch = '.'
            elif c < 13:
                ch = '*'
            elif c < 14:
                ch = '8'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = '8'
            elif c < 17:
                ch = '.'
            elif c < 22:
                ch = ' '
            elif c < 23:
                ch = '*'
            elif c < 27:
                ch = '.'
            elif c < 33:
                ch = '*'
            elif c < 36:
                ch = ':'
            elif c < 39:
                ch = '&'
            elif c < 41:
                ch = ':'
            elif c < 42:
                ch = '&'
            elif c < 44:
                ch = ':'
            elif c < 52:
                ch = '.'
            elif c < 53:
                ch = '*'
            elif c < 54:
                ch = ':'
            elif c < 55:
                ch = '&'
            elif c < 57:
                ch = '8'
            elif c < 60:
                ch = '&'
            elif c < 65:
                ch = ':'
            elif c < 68:
                ch = '&'
            elif c < 73:
                ch = '8'
            elif c < 77:
                ch = '&'
            elif c < 82:
                ch = ':'
            elif c < 83:
                ch = '#'
            elif c < 84:
                ch = '@'
            elif c < 86:
                ch = '&'
            elif c < 89:
                ch = ':'
            elif c < 92:
                ch = '&'
            elif c < 93:
                ch = '.'
            else:
                ch = ' '
        elif r == 20:
            if c < 1:
                ch = '.'
            elif c < 3:
                ch = ' '
            elif c < 4:
                ch = '.'
            elif c < 6:
                ch = '*'
            elif c < 12:
                ch = '.'
            elif c < 13:
                ch = '*'
            elif c < 14:
                ch = '8'
            elif c < 15:
                ch = '@'
            elif c < 16:
                ch = '8'
            elif c < 17:
                ch = '.'
            elif c < 22:
                ch = ' '
            elif c < 23:
                ch = '*'
            elif c < 27:
                ch = '.'
            elif c < 33:
                ch = '*'
            elif c < 36:
                ch = ':'
            elif c < 39:
                ch = '&'
            elif c < 41:
                ch = ':'
            elif c < 42:
                ch = '&'
            elif c < 44:
                ch = ':'
            elif c < 52:
                ch = '.'
            elif c < 53:
                ch = '*'
            elif c < 54:
                ch = ':'
            elif c < 55:
                ch = '&'
            elif c < 57:
                ch = '8'
            elif c < 60:
                ch = '&'
            elif c < 65:
                ch = ':'
            elif c < 68:
                ch = '&'
            elif c < 73:
                ch = '8'
            elif c < 77:
                ch = '&'
            elif c < 82:
                ch = ':'
            elif c < 83:
                ch = '#'
            elif c < 84:
                ch = '@'
            elif c < 86:
                ch = '&'
            elif c < 89:
                ch = ':'
            elif c < 92:
                ch = '&'
            elif c < 93:
                ch = '.'
            else:
                ch = ' '
        elif r == 21:
            if c < 1:
                ch = '.'
            elif c < 4:
                ch = ' '
            elif c < 5:
                ch = '.'
            elif c < 7:
                ch = '*'
            elif c < 8:
                ch = '.'
            elif c < 13:
                ch = '*'
            elif c < 14:
                ch = '.'
            elif c < 15:
                ch = '*'
            elif c < 16:
                ch = '8'
            elif c < 17:
                ch = '*'
            elif c < 18:
                ch = ' '
            elif c < 25:
                ch = '.'
            elif c < 26:
                ch = '*'
            elif c < 28:
                ch = ':'
            elif c < 30:
                ch = '&'
            elif c < 31:
                ch = '*'
            elif c < 32:
                ch = ':'
            elif c < 36:
                ch = '&'
            elif c < 38:
                ch = ':'
            elif c < 44:
                ch = '&'
            elif c < 45:
                ch = ':'
            elif c < 46:
                ch = '*'
            elif c < 47:
                ch = '.'
            elif c < 51:
                ch = ' '
            elif c < 52:
                ch = '.'
            elif c < 54:
                ch = '*'
            elif c < 59:
                ch = '&'
            elif c < 61:
                ch = ':'
            elif c < 66:
                ch = '*'
            elif c < 68:
                ch = ':'
            elif c < 69:
                ch = '&'
            elif c < 70:
                ch = ':'
            elif c < 72:
                ch = '&'
            elif c < 73:
                ch = '8'
            elif c < 76:
                ch = '&'
            elif c < 82:
                ch = ':'
            elif c < 84:
                ch = '&'
            elif c < 86:
                ch = '#'
            elif c < 89:
                ch = '&'
            elif c < 92:
                ch = ':'
            elif c < 93:
                ch = '.'
            else:
                ch = ' '
        elif r == 22:
            if c < 1:
                ch = '.'
            elif c < 6:
                ch = ' '
            elif c < 9:
                ch = '.'
            elif c < 10:
                ch = '*'
            elif c < 11:
                ch = ':'
            elif c < 12:
                ch = '*'
            elif c < 15:
                ch = '.'
            elif c < 16:
                ch = '*'
            elif c < 17:
                ch = ':'
            elif c < 19:
                ch = ' '
            elif c < 30:
                ch = '.'
            elif c < 32:
                ch = '*'
            elif c < 33:
                ch = '.'
            elif c < 34:
                ch = '*'
            elif c < 36:
                ch = '.'
            elif c < 41:
                ch = '*'
            elif c < 42:
                ch = ':'
            elif c < 47:
                ch = '.'
            elif c < 49:
                ch = ' '
            elif c < 51:
                ch = '.'
            elif c < 52:
                ch = '*'
            elif c < 53:
                ch = ':'
            elif c < 56:
                ch = '&'
            elif c < 59:
                ch = ':'
            elif c < 69:
                ch = '*'
            elif c < 77:
                ch = ':'
            elif c < 79:
                ch = '*'
            elif c < 82:
                ch = ':'
            elif c < 85:
                ch = '&'
            elif c < 86:
                ch = '#'
            elif c < 87:
                ch = '8'
            elif c < 88:
                ch = '&'
            elif c < 90:
                ch = '8'
            elif c < 91:
                ch = '&'
            elif c < 92:
                ch = ':'
            elif c < 93:
                ch = '.'
            else:
                ch = ' '
        elif r == 23:
            if c < 1:
                ch = '.'
            elif c < 8:
                ch = ' '
            elif c < 9:
                ch = '.'
            elif c < 10:
                ch = '*'
            elif c < 12:
                ch = ':'
            elif c < 14:
                ch = '*'
            elif c < 16:
                ch = '.'
            elif c < 17:
                ch = '&'
            elif c < 18:
                ch = '.'
            elif c < 35:
                ch = ' '
            elif c < 36:
                ch = '*'
            elif c < 42:
                ch = '.'
            elif c < 43:
                ch = ' '
            elif c < 46:
                ch = '.'
            elif c < 47:
                ch = '*'
            elif c < 50:
                ch = ':'
            elif c < 53:
                ch = '*'
            elif c < 57:
                ch = '.'
            elif c < 73:
                ch = '*'
            elif c < 75:
                ch = ':'
            elif c < 78:
                ch = '&'
            elif c < 81:
                ch = '8'
            elif c < 84:
                ch = '&'
            elif c < 85:
                ch = '*'
            else:
                ch = ' '
        elif r == 24:
            if c < 1:
                ch = '.'
            elif c < 8:
                ch = ' '
            elif c < 9:
                ch = '.'
            elif c < 10:
                ch = '*'
            elif c < 13:
                ch = '.'
            elif c < 14:
                ch = '*'
            elif c < 15:
                ch = '&'
            elif c < 16:
                ch = ':'
            elif c < 17:
                ch = '*'
            elif c < 18:
                ch = '.'
            elif c < 47:
                ch = '.'
            elif c < 49:
                ch = ' '
            elif c < 52:
                ch = '.'
            elif c < 53:
                ch = '*'
            elif c < 57:
                ch = ':'
            elif c < 62:
                ch = '*'
            elif c < 67:
                ch = '.'
            elif c < 69:
                ch = '*'
            elif c < 71:
                ch = '.'
            elif c < 79:
                ch = '*'
            elif c < 81:
                ch = ':'
            elif c < 83:
                ch = '&'
            elif c < 86:
                ch = '8'
            elif c < 87:
                ch = '&'
            elif c < 90:
                ch = ':'
            else:
                ch = ' '
        elif r == 25:
            if c < 10:
                ch = ' '
            elif c < 15:
                ch = '.'
            elif c < 18:
                ch = '*'
            elif c < 20:
                ch = ' '
            elif c < 47:
                ch = '.'
            elif c < 48:
                ch = ' '
            elif c < 52:
                ch = '.'
            elif c < 54:
                ch = '*'
            elif c < 58:
                ch = ':'
            elif c < 60:
                ch = '*'
            elif c < 71:
                ch = '.'
            elif c < 78:
                ch = '*'
            elif c < 81:
                ch = ':'
            elif c < 83:
                ch = '&'
            elif c < 85:
                ch = '8'
            elif c < 89:
                ch = '&'
            elif c < 90:
                ch = '.'
            else:
                ch = ' '
        elif r == 26:
            if c < 11:
                ch = ' '
            elif c < 17:
                ch = '.'
            elif c < 18:
                ch = '*'
            elif c < 19:
                ch = '.'
            elif c < 20:
                ch = ' '
            elif c < 52:
                ch = '.'
            elif c < 54:
                ch = '*'
            elif c < 62:
                ch = ':'
            elif c < 63:
                ch = '*'
            elif c < 72:
                ch = '.'
            elif c < 77:
                ch = '*'
            elif c < 80:
                ch = ':'
            elif c < 83:
                ch = '&'
            elif c < 85:
                ch = '8'
            elif c < 87:
                ch = '&'
            elif c < 88:
                ch = ':'
            elif c < 89:
                ch = '.'
            else:
                ch = ' '
        elif r == 27:
            if c < 13:
                ch = ' '
            elif c < 17:
                ch = '.'
            elif c < 18:
                ch = '*'
            elif c < 19:
                ch = '.'
            elif c < 21:
                ch = ' '
            elif c < 27:
                ch = '.'
            elif c < 31:
                ch = ' '
            elif c < 37:
                ch = '.'
            elif c < 41:
                ch = '*'
            elif c < 44:
                ch = '.'
            elif c < 51:
                ch = ' '
            elif c < 53:
                ch = '.'
            elif c < 54:
                ch = '*'
            elif c < 56:
                ch = ':'
            elif c < 60:
                ch = '*'
            elif c < 61:
                ch = ':'
            elif c < 62:
                ch = '&'
            elif c < 63:
                ch = ':'
            elif c < 65:
                ch = '*'
            elif c < 71:
                ch = '.'
            elif c < 72:
                ch = '*'
            elif c < 74:
                ch = '.'
            elif c < 77:
                ch = '*'
            elif c < 80:
                ch = ':'
            elif c < 82:
                ch = '&'
            elif c < 83:
                ch = '#'
            elif c < 84:
                ch = ':'
            elif c < 85:
                ch = '*'
            elif c < 86:
                ch = '.'
            else:
                ch = ' '
        elif r == 28:
            if c < 18:
                ch = ' '
            elif c < 19:
                ch = '.'
            elif c < 21:
                ch = ' '
            elif c < 34:
                ch = '.'
            elif c < 39:
                ch = '*'
            elif c < 42:
                ch = '.'
            elif c < 44:
                ch = ' '
            elif c < 45:
                ch = '.'
            elif c < 52:
                ch = ' '
            elif c < 54:
                ch = '.'
            elif c < 55:
                ch = '*'
            elif c < 57:
                ch = ':'
            elif c < 60:
                ch = '*'
            elif c < 61:
                ch = '&'
            elif c < 62:
                ch = ':'
            elif c < 64:
                ch = '*'
            elif c < 71:
                ch = '.'
            elif c < 77:
                ch = '*'
            elif c < 80:
                ch = ':'
            elif c < 82:
                ch = '&'
            elif c < 83:
                ch = '#'
            elif c < 84:
                ch = '.'
            else:
                ch = ' '
        elif r == 29:
            if c < 18:
                ch = ' '
            elif c < 34:
                ch = '.'
            elif c < 38:
                ch = '*'
            elif c < 40:
                ch = '.'
            elif c < 44:
                ch = '*'
            elif c < 46:
                ch = ':'
            elif c < 47:
                ch = '*'
            elif c < 48:
                ch = '.'
            elif c < 51:
                ch = ' '
            elif c < 52:
                ch = '*'
            elif c < 53:
                ch = ':'
            elif c == 53:
                ch = '8'
            elif c == 54:
                ch = '8'
            elif c == 55:
                ch = '#'
            elif c == 56:
                ch = '8'
            elif c == 57:
                ch = '8'
            elif c == 58:
                ch = '8'
            elif c == 59:
                ch = '&'
            elif c == 60:
                ch = '&'
            elif c == 61:
                ch = '&'
            elif c < 63:
                ch = ':'
            elif c < 68:
                ch = '.'
            elif c < 75:
                ch = '*'
            elif c < 78:
                ch = ':'
            elif c == 78:
                ch = '&'
            elif c == 79:
                ch = '&'
            elif c == 80:
                ch = '8'
            elif c == 81:
                ch = '#'
            else:
                ch = ' '
        elif r == 30:
            if c < 19:
                ch = ' '
            elif c < 21:
                ch = '.'
            elif c < 25:
                ch = '*'
            elif c < 35:
                ch = '.'
            elif c < 37:
                ch = '*'
            elif c < 39:
                ch = ':'
            elif c < 44:
                ch = '*'
            elif c < 52:
                ch = ':'
            elif c == 52:
                ch = '&'
            elif c == 53:
                ch = '8'
            elif c == 54:
                ch = '#'
            elif c == 55:
                ch = '8'
            elif c == 56:
                ch = '#'
            elif c == 57:
                ch = '8'
            elif c == 58:
                ch = '&'
            elif c == 59:
                ch = '&'
            elif c == 60:
                ch = '&'
            elif c == 61:
                ch = '8'
            elif c == 62:
                ch = '8'
            elif c == 63:
                ch = '8'
            elif c == 64:
                ch = '&'
            elif c == 65:
                ch = ':'
            elif c < 74:
                ch = '*'
            elif c < 78:
                ch = ':'
            elif c == 78:
                ch = '&'
            elif c == 79:
                ch = '&'
            elif c == 80:
                ch = '8'
            elif c == 81:
                ch = '#'
            elif c == 82:
                ch = '.'
            else:
                ch = ' '
        elif r == 31:
            if c < 19:
                ch = ' '
            elif c < 22:
                ch = '.'
            elif c < 26:
                ch = '*'
            elif c < 31:
                ch = '.'
            elif c < 33:
                ch = '*'
            elif c < 36:
                ch = ':'
            elif c < 38:
                ch = '&'
            elif c == 38:
                ch = '8'
            elif c == 39:
                ch = ':'
            elif c < 43:
                ch = '*'
            elif c == 43:
                ch = '.'
            elif c < 47:
                ch = '*'
            elif c == 47:
                ch = ':'
            elif c < 51:
                ch = '&'
            elif c == 51:
                ch = ':'
            elif c == 52:
                ch = '*'
            elif c == 53:
                ch = ':'
            elif c == 54:
                ch = '&'
            elif c == 55:
                ch = ':'
            elif c < 60:
                ch = ':'
            elif c == 60:
                ch = '&'
            elif c == 61:
                ch = '8'
            elif c == 62:
                ch = '8'
            elif c == 63:
                ch = '8'
            elif c == 64:
                ch = '&'
            elif c < 71:
                ch = ':'
            elif c < 73:
                ch = '*'
            elif c < 75:
                ch = ':'
            elif c == 75 or c == 76:
                ch = '&'
            elif c == 77 or c == 78:
                ch = '8'
            elif c == 79:
                ch = '#'
            else:
                ch = ' '
        elif r == 32:
            if c < 20:
                ch = ' '
            elif c == 20:
                ch = '.'
            elif c < 30:
                ch = '*'
            elif c < 33:
                ch = ':'
            elif c < 35:
                ch = '&'
            elif c == 35:
                ch = '8'
            elif c == 36:
                ch = '8'
            elif c == 37:
                ch = '#'
            elif c == 38:
                ch = '&'
            elif c < 43:
                ch = ':'
            elif c < 47:
                ch = '*'
            elif c < 50:
                ch = '.'
            elif c < 54:
                ch = '*'
            elif c < 57:
                ch = ':'
            elif c == 57:
                ch = '&'
            elif 58 <= c <= 62:
                ch = '8'
            elif c == 63:
                ch = '&'
            elif 64 <= c <= 65:
                ch = ':'
            elif 66 <= c <= 67:
                ch = '&'
            elif 68 <= c <= 71:
                ch = ':'
            elif 72 <= c <= 74:
                ch = '&'
            elif c == 75:
                ch = '8'
            elif c == 76:
                ch = '#'
            elif c == 77:
                ch = '&'
            else:
                ch = ' '
        elif r == 33:
            if c < 21:
                ch = ' '
            elif c < 34:
                ch = '*'
            elif c == 34:
                ch = ':'
            elif c == 35:
                ch = '&'
            elif c in [36, 37]:
                ch = '8'
            elif c == 38:
                ch = '&'
            elif c == 39:
                ch = ':'
            elif 40 <= c <= 42:
                ch = '.'
            elif c == 43:
                ch = '*'
            elif 44 <= c <= 54:
                ch = '.'
            elif 55 <= c <= 58:
                ch = '*'
            elif 59 <= c <= 61:
                ch = ':'
            elif 62 <= c <= 63:
                ch = '&'
            elif 64 <= c <= 66:
                ch = ':'
            elif c == 67:
                ch = '&'
            elif 68 <= c <= 70:
                ch = ':'
            elif 71 <= c <= 74:
                ch = '&'
            elif c == 75:
                ch = '8'
            elif c == 76:
                ch = '#'
            elif c == 77:
                ch = '&'
            else:
                ch = ' '
        elif r == 34:
            if c < 21:
                ch = ' '
            elif c == 21:
                ch = '.'
            elif 22 <= c <= 27:
                ch = '*'
            elif c == 28:
                ch = ':'
            elif 29 <= c <= 32:
                ch = '*'
            elif c == 33:
                ch = ':'
            elif c == 34:
                ch = '&'
            elif 35 <= c <= 36:
                ch = ':'
            elif 37 <= c <= 39:
                ch = '*'
            elif 40 <= c <= 41:
                ch = '.'
            elif c == 42:
                ch = '*'
            elif 43 <= c <= 46:
                ch = '.'
            elif 47 <= c <= 55:
                ch = '*'
            elif 56 <= c <= 63:
                ch = ':'
            elif 64 <= c <= 65:
                ch = '*'
            elif c == 66:
                ch = ':'
            elif 67 <= c <= 68:
                ch = '&'
            elif 69 <= c <= 71:
                ch = ':'
            elif c == 72:
                ch = '&'
            elif 73 <= c <= 75:
                ch = '8'
            elif c == 76:
                ch = '&'
            else:
                ch = ' '
        elif r == 35:
            if c < 22:
                ch = ' '
            elif c == 22:
                ch = '.'
            elif 23 <= c <= 26:
                ch = ':'
            elif 27 <= c <= 29:
                ch = '*'
            elif 30 <= c <= 36:
                ch = ':'
            elif 37 <= c <= 42:
                ch = '*'
            elif c == 43:
                ch = '.'
            elif 44 <= c <= 47:
                ch = '*'
            elif c == 48:
                ch = ':'
            elif c == 49:
                ch = '*'
            elif 50 <= c <= 60:
                ch = ':'
            elif c == 61:
                ch = '&'
            elif c == 62:
                ch = ':'
            elif c == 63:
                ch = '*'
            elif 64 <= c <= 67:
                ch = ':'
            elif 68 <= c <= 70:
                ch = '&'
            elif c == 71:
                ch = '8'
            elif c == 72:
                ch = '&'
            elif c == 73:
                ch = '8'
            elif c == 74:
                ch = '#'
            elif c == 75:
                ch = '8'
            elif c == 76:
                ch = '*'
            else:
                ch = ' '
        elif r == 36:
            if c < 23:
                ch = ' '
            elif c == 23:
                ch = '.'
            elif c == 24:
                ch = '*'
            elif c == 25:
                ch = ':'
            elif c == 26:
                ch = '&'
            elif 27 <= c <= 36:
                ch = ':'
            elif 37 <= c <= 40:
                ch = '*'
            elif 41 <= c <= 47:
                ch = '.'
            elif 48 <= c <= 56:
                ch = '*'
            elif 57 <= c <= 58:
                ch = ':'
            elif 59 <= c <= 60:
                ch = '*'
            elif 61 <= c <= 66:
                ch = '&'
            elif 67 <= c <= 73:
                ch = '8'
            elif 74 <= c <= 75:
                ch = '#'
            elif c == 76:
                ch = '*'
            else:
                ch = ' '
        elif r == 37:
            if c < 24:
                ch = ' '
            elif 24 <= c <= 25:
                ch = '.'
            elif c == 26:
                ch = ':'
            elif 27 <= c <= 28:
                ch = '&'
            elif 29 <= c <= 30:
                ch = ':'
            elif 31 <= c <= 35:
                ch = '&'
            elif 36 <= c <= 39:
                ch = ':'
            elif 40 <= c <= 42:
                ch = '*'
            elif c == 43:
                ch = '.'
            elif c == 44:
                ch = '*'
            elif 45 <= c <= 52:
                ch = '.'
            elif 53 <= c <= 55:
                ch = '*'
            elif c == 56:
                ch = ':'
            elif 57 <= c <= 58:
                ch = '&'
            elif 59 <= c <= 61:
                ch = ':'
            elif c == 62:
                ch = '&'
            elif 63 <= c <= 68:
                ch = '8'
            elif 69 <= c <= 72:
                ch = '#'
            elif 73 <= c <= 74:
                ch = '8'
            elif c == 75:
                ch = '.'
            else:
                ch = ' '
        elif r == 38:
            if c < 20:
                ch = ' '
            elif c == 20:
                ch = '.'
            elif 21 <= c <= 22:
                ch = ' '
            elif 23 <= c <= 26:
                ch = '.'
            elif c == 27:
                ch = ':'
            elif c == 28:
                ch = '*'
            elif 29 <= c <= 36:
                ch = '&'
            elif 37 <= c <= 39:
                ch = ':'
            elif 40 <= c <= 47:
                ch = '*'
            elif c == 48:
                ch = '.'
            elif 49 <= c <= 55:
                ch = '*'
            elif 56 <= c <= 59:
                ch = ':'
            elif 60 <= c <= 64:
                ch = '&'
            elif 65 <= c <= 66:
                ch = '8'
            elif 67 <= c <= 73:
                ch = '#'
            elif c == 74:
                ch = '8'
            elif 75 <= c <= 77:
                ch = '&'
            elif c == 78:
                ch = '8'
            elif c == 79:
                ch = ':'
            else:
                ch = ' '
        elif r == 39:
            if c < 17:
                ch = ' '
            elif c == 17:
                ch = '.'
            elif 18 <= c <= 19:
                ch = '*'
            elif c == 20:
                ch = '.'
            elif 21 <= c <= 22:
                ch = ' '
            elif 23 <= c <= 27:
                ch = '.'
            elif c == 28:
                ch = ':'
            elif c == 29:
                ch = '*'
            elif 30 <= c <= 37:
                ch = '&'
            elif 38 <= c <= 45:
                ch = ':'
            elif 46 <= c <= 47:
                ch = '*'
            elif 48 <= c <= 51:
                ch = ':'
            elif c == 52:
                ch = '*'
            elif 53 <= c <= 55:
                ch = ':'
            elif 56 <= c <= 58:
                ch = '&'
            elif 59 <= c <= 60:
                ch = '8'
            elif 61 <= c <= 63:
                ch = '#'
            elif 64 <= c <= 66:
                ch = '@'
            elif c == 67:
                ch = '#'
            elif c == 68:
                ch = '8'
            elif 69 <= c <= 76:
                ch = '&'
            elif c == 77:
                ch = ':'
            elif c == 78:
                ch = '*'
            else:
                ch = ' '
        elif r == 40:
            if c < 15:
                ch = ' '
            elif c == 15:
                ch = '.'
            elif 16 <= c <= 19:
                ch = '*'
            elif 20 <= c <= 22:
                ch = '.'
            elif c == 23:
                ch = ' '
            elif 24 <= c <= 30:
                ch = '.'
            elif 31 <= c <= 32:
                ch = '*'
            elif c == 33:
                ch = ':'
            elif 34 <= c <= 36:
                ch = '&'
            elif 37 <= c <= 39:
                ch = '8'
            elif 40 <= c <= 41:
                ch = '&'
            elif 42 <= c <= 49:
                ch = ':'
            elif c == 50:
                ch = '&'
            elif c == 51:
                ch = ':'
            elif 52 <= c <= 59:
                ch = '&'
            elif 60 <= c <= 63:
                ch = '8'
            elif 64 <= c <= 66:
                ch = '#'
            elif 67 <= c <= 68:
                ch = '@'
            elif 69 <= c <= 70:
                ch = '#'
            elif 71 <= c <= 73:
                ch = '&'
            elif 74 <= c <= 75:
                ch = ':'
            elif 76 <= c <= 81:
                ch = '&'
            elif 82 <= c <= 83:
                ch = '8'
            elif c == 84:
                ch = '&'
            elif 85 <= c <= 86:
                ch = ':'
            elif c == 87:
                ch = '*'
            else:
                ch = ' '
        elif r == 41:
            if c < 4:
                ch = ' '
            elif c == 4:
                ch = '.'
            elif 5 <= c <= 7:
                ch = '*'
            elif 8 <= c <= 10:
                ch = ':'
            elif 11 <= c <= 15:
                ch = '*'
            elif 16 <= c <= 42:
                ch = '.'
            elif 43 <= c <= 44:
                ch = '*'
            elif c == 45:
                ch = ':'
            elif 46 <= c <= 48:
                ch = '&'
            elif 49 <= c <= 50:
                ch = '8'
            elif 51 <= c <= 52:
                ch = '&'
            elif 53 <= c <= 56:
                ch = '8'
            elif c == 57:
                ch = '&'
            elif 58 <= c <= 66:
                ch = '8'
            elif 67 <= c <= 74:
                ch = '#'
            elif c == 75:
                ch = '8'
            elif 76 <= c <= 77:
                ch = '&'
            elif 78 <= c <= 81:
                ch = ':'
            elif c == 82:
                ch = '&'
            elif 83 <= c <= 84:
                ch = ':'
            elif 85 == c:
                ch = '&'
            elif 86 <= c <= 95:
                ch = '&'
            elif c == 96:
                ch = ':'
            elif c == 97:
                ch = '*'
            elif 98 <= c <= 99:
                ch = ':'
            else:
                ch = ' '
        elif r == 42:
            if 0 <= c <= 2:
                ch = '.'
            elif c == 3:
                ch = '*'
            elif 4 <= c <= 6:
                ch = '.'
            elif c == 7:
                ch = ':'
            elif 8 <= c <= 11:
                ch = '*'
            elif 12 <= c <= 27:
                ch = '.'
            elif c == 28:
                ch = '*'
            elif 29 <= c <= 31:
                ch = ':'
            elif 32 <= c <= 35:
                ch = '&'
            elif c == 36:
                ch = '8'
            elif c == 37:
                ch = '&'
            elif 38 <= c <= 41:
                ch = '&'
            elif c == 42:
                ch = '8'
            elif c == 43:
                ch = '&'
            elif 44 <= c <= 45:
                ch = '&'
            elif 46 <= c <= 54:
                ch = '8'
            elif c == 55:
                ch = '&'
            elif 56 <= c <= 57:
                ch = ':'
            elif 58 <= c <= 59:
                ch = '*'
            elif 60 <= c <= 71:
                ch = ':'
            elif 72 <= c <= 80:
                ch = '&'
            elif 81 <= c <= 84:
                ch = ':'
            elif c == 85:
                ch = '&'
            elif 86 <= c <= 87:
                ch = ':'
            elif 88 <= c <= 89:
                ch = '*'
            elif 90 <= c <= 91:
                ch = '.'
            else:
                ch = ' '
        elif r == 43:
            if 0 <= c <= 1:
                ch = '.'
            elif 2 <= c <= 3:
                ch = '*'
            elif 4 <= c <= 6:
                ch = '.'
            elif 7 <= c <= 8:
                ch = '*'
            elif c == 9:
                ch = ':'
            elif c == 10:
                ch = '*'
            elif 11 <= c <= 39:
                ch = '.'
            elif c == 40:
                ch = '*'
            elif c == 41:
                ch = '.'
            elif 42 <= c <= 52:
                ch = '*'
            elif 53 <= c <= 61:
                ch = ':'
            elif 62 <= c <= 69:
                ch = '*'
            elif 70 <= c <= 77:
                ch = ':'
            elif 78 <= c <= 83:
                ch = '&'
            elif 84 <= c <= 87:
                ch = ':'
            elif c == 88:
                ch = '&'
            elif 89 <= c <= 97:
                ch = ':'
            elif c == 98:
                ch = '*'
            else:
                ch = ' '
        elif r == 44:
            if c == 0:
                ch = '*'
            elif 1 <= c <= 2:
                ch = '.'
            elif 3 <= c <= 5:
                ch = '*'
            elif c == 6:
                ch = '.'
            elif 7 <= c <= 9:
                ch = '*'
            elif 10 <= c <= 11:
                ch = ':'
            elif 12 <= c <= 13:
                ch = '*'
            elif 14 <= c <= 45:
                ch = '.'
            elif 46 <= c <= 51:
                ch = '*'
            elif c == 52:
                ch = ':'
            elif c == 53:
                ch = '*'
            elif c == 54:
                ch = ':'
            elif c == 55:
                ch = '*'
            elif 56 <= c <= 59:
                ch = ':'
            elif 57 <= c <= 59:
                ch = '*'
            elif 60 <= c <= 69:
                ch = ':'
            elif 70 <= c <= 74:
                ch = '&'
            elif 75 <= c <= 82:
                ch = ':'
            elif c == 83:
                ch = '&'
            elif c == 84:
                ch = ':'
            elif c == 85:
                ch = '&'
            elif 86 <= c <= 87:
                ch = ':'
            else:
                ch = ' '
        elif r == 45:
            if 0 <= c <= 1:
                ch = '*'
            elif 2 <= c <= 3:
                ch = '.'
            elif 4 <= c <= 8:
                ch = '*'
            elif 9 <= c <= 10:
                ch = '.'
            elif c == 11:
                ch = '*'
            elif c == 12:
                ch = ':'
            elif c == 13:
                ch = '&'
            elif c == 14:
                ch = ':'
            elif c == 15:
                ch = '*'
            elif 16 <= c <= 20:
                ch = '.'
            elif c == 21:
                ch = '*'
            elif 22 <= c <= 46:
                ch = '.'
            elif 47 <= c <= 55:
                ch = '*'
            elif 56 <= c <= 58:
                ch = '.'
            elif 59 <= c <= 62:
                ch = '*'
            elif 63 <= c <= 74:
                ch = ':'
            elif c == 75:
                ch = '&'
            elif 76 <= c <= 77:
                ch = '8'
            elif 78 <= c <= 80:
                ch = ':'
            elif c == 81:
                ch = '*'
            elif 82 <= c <= 89:
                ch = ':'
            elif 90 <= c <= 91:
                ch = '&'
            else:
                ch = ' '
        elif r == 46:
            if c == 0:
                ch = '*'
            elif 1 <= c <= 5:
                ch = '.'
            elif 6 <= c <= 13:
                ch = '*'
            elif c == 14:
                ch = ':'
            elif c == 15:
                ch = '&'
            elif c == 16:
                ch = ':'
            elif 17 <= c <= 21:
                ch = '*'
            elif 22 <= c <= 46:
                ch = '.'
            elif 47 <= c <= 53:
                ch = '*'
            elif 54 <= c <= 57:
                ch = '.'
            elif 58 <= c <= 60:
                ch = '*'
            elif 61 <= c <= 66:
                ch = ':'
            elif 67 <= c <= 70:
                ch = '*'
            elif 71 <= c <= 72:
                ch = ':'
            elif 73 <= c <= 75:
                ch = '&'
            elif 76 <= c <= 77:
                ch = ':'
            elif 78 <= c <= 79:
                ch = '*'
            elif 80 <= c <= 87:
                ch = ':'
            elif 88 <= c <= 89:
                ch = '&'
            elif 90 <= c <= 91:
                ch = ':'
            elif c == 92:
                ch = '&'
            elif c == 93:
                ch = ':'
            else:
                ch = ' '
        elif r == 47:
            if 0 <= c <= 1:
                ch = '.'
            elif c == 2:
                ch = '*'
            elif 3 <= c <= 5:
                ch = '.'
            elif c == 6:
                ch = '*'
            elif 7 <= c <= 8:
                ch = ':'
            elif 9 <= c <= 12:
                ch = '*'
            elif 13 <= c <= 14:
                ch = '.'
            elif c == 15:
                ch = '*'
            elif c == 16:
                ch = ':'
            elif 17 <= c <= 19:
                ch = '&'
            elif c == 20:
                ch = ':'
            elif c == 21:
                ch = '*'
            elif 22 <= c <= 47:
                ch = '.'
            elif 48 <= c <= 50:
                ch = '*'
            elif 51 <= c <= 55:
                ch = ':'
            elif 56 <= c <= 61:
                ch = '*'
            elif 62 <= c <= 64:
                ch = ':'
            elif c == 65:
                ch = '*'
            elif c == 66:
                ch = ':'
            elif c == 67:
                ch = '*'
            elif 68 <= c <= 86:
                ch = ':'
            elif c == 87:
                ch = '&'
            elif c == 88:
                ch = ':'
            else:
                ch = ' '
        elif r == 48:
            if 0 <= c <= 13:
                ch = '*'
            elif c == 14:
                ch = '.'
            elif c == 15:
                ch = '*'
            elif c == 16:
                ch = '.'
            elif 17 <= c <= 18:
                ch = '*'
            elif c == 19:
                ch = ':'
            elif c == 20:
                ch = '&'
            elif c == 21:
                ch = ':'
            elif c == 22:
                ch = '*'
            elif c == 23:
                ch = ':'
            elif 24 <= c <= 54:
                ch = '.'
            elif 55 <= c <= 56:
                ch = '*'
            elif 57 <= c <= 61:
                ch = ':'
            elif 62 <= c <= 73:
                ch = '*'
            elif 74 <= c <= 93:
                ch = ':'
            else:
                ch = ' '
        elif r == 49:
            if 0 <= c <= 5:
                ch = '*'
            elif 6 <= c <= 7:
                ch = '.'
            elif 8 <= c <= 14:
                ch = '*'
            elif 15 <= c <= 16:
                ch = '.'
            elif c == 17:
                ch = '*'
            elif 18 <= c <= 19:
                ch = '.'
            elif 20 <= c <= 21:
                ch = '*'
            elif 22 <= c <= 25:
                ch = ':'
            elif 26 <= c <= 27:
                ch = '*'
            elif 28 <= c <= 59:
                ch = '.'
            elif 60 <= c <= 61:
                ch = '*'
            elif 62 <= c <= 64:
                ch = ':'
            elif 65 <= c <= 72:
                ch = '*'
            elif 73 <= c <= 76:
                ch = ':'
            elif c == 77:
                ch = '*'
            elif 78 <= c <= 83:
                ch = ':'
            elif 84 <= c <= 85:
                ch = '*'
            elif 86 <= c <= 99:
                ch = ':'
        elif r == 50:
            if 0 <= c <= 17:
                ch = '*'
            elif 18 <= c <= 21:
                ch = '.'
            elif 22 <= c <= 25:
                ch = '*'
            elif 26 <= c <= 29:
                ch = ':'
            elif 30 <= c <= 31:
                ch = '*'
            elif 32 <= c <= 59:
                ch = '.'
            elif 60 <= c <= 74:
                ch = '*'
            elif 75 <= c <= 78:
                ch = ':'
            elif 79 <= c <= 81:
                ch = '*'
            elif c == 82:
                ch = ':'
            elif c == 83:
                ch = '*'
            elif 84 <= c <= 87:
                ch = '*'
            elif 88 <= c <= 99:
                ch = ':'
        elif r == 51:
            if 0 <= c <= 23:
                ch = '*'
            elif c == 24:
                ch = '.'
            elif 25 <= c <= 30:
                ch = '*'
            elif c == 31:
                ch = ':'
            elif 32 <= c <= 35:
                ch = '*'
            elif 36 <= c <= 57:
                ch = '.'
            elif 58 <= c <= 65:
                ch = '*'
            elif c == 66:
                ch = ':'
            elif c == 67:
                ch = '*'
            elif 68 <= c <= 70:
                ch = ':'
            elif c == 71:
                ch = '*'
            elif c == 72:
                ch = ':'
            elif 73 <= c <= 74:
                ch = '*'
            elif c == 75:
                ch = ':'
            elif 76 <= c <= 80:
                ch = '*'
            elif 81 <= c <= 99:
                ch = ':'
        elif r == 52:
            if c == 0:
                ch = '.'
            elif 1 <= c <= 22:
                ch = '*'
            elif c == 23:
                ch = '.'
            elif 24 <= c <= 25:
                ch = '*'
            elif c == 26:
                ch = '.'
            elif 27 <= c <= 28:
                ch = '*'
            elif 29 <= c <= 30:
                ch = '.'
            elif 31 <= c <= 41:
                ch = '*'
            elif 42 <= c <= 56:
                ch = '.'
            elif 57 <= c <= 68:
                ch = '*'
            elif c == 69:
                ch = ':'
            elif c == 70:
                ch = '*'
            elif c == 71:
                ch = ':'
            elif c == 72:
                ch = '*'
            elif 73 <= c <= 74:
                ch = ':'
            elif 76 <= c <= 79:
                ch = '*'
            elif 80 <= c <= 81:
                ch = ':'
            elif 82 <= c <= 85:
                ch = '*'
            elif c == 86:
                ch = ':'
            elif 87 <= c <= 90:
                ch = '*'
            elif 91 <= c <= 99:
                ch = ':'
        elif r == 53:
            if 0 <= c <= 29:
                ch = '*'
            elif c == 30:
                ch = '.'
            elif 31 <= c <= 52:
                ch = '*'
            elif 53 <= c <= 55:
                ch = ':'
            elif 56 <= c <= 66:
                ch = '*'
            elif 67 <= c <= 69:
                ch = ':'
            elif c == 70:
                ch = '*'
            elif c == 71:
                ch = ':'
            elif 72 <= c <= 75:
                ch = '*'
            elif c == 76:
                ch = ':'
            elif 77 <= c <= 78:
                ch = '*'
            elif 79 <= c <= 80:
                ch = ':'
            elif 81 <= c <= 82:
                ch = '*'
            elif 83 <= c <= 85:
                ch = ':'
            elif c == 86:
                ch = '*'
            elif 87 <= c <= 99:
                ch = ':'
        elif r == 54:
            if 0 <= c <= 23:
                ch = '*'
            elif c == 24:
                ch = '.'
            elif 25 <= c <= 31:
                ch = '*'
            elif c == 32:
                ch = '.'
            elif 33 <= c <= 36:
                ch = '*'
            elif 37 <= c <= 38:
                ch = ':'
            elif 39 <= c <= 42:
                ch = '*'
            elif c == 43:
                ch = ':'
            elif 44 <= c <= 63:
                ch = '*'
            elif c == 64:
                ch = ':'
            elif 65 <= c <= 67:
                ch = '*'
            elif 68 <= c <= 79:
                ch = ':'
            elif 80 <= c <= 81:
                ch = '*'
            elif 82 <= c <= 84:
                ch = ':'
            elif c == 85:
                ch = '&'
            elif 86 <= c <= 87:
                ch = ':'
            elif c == 88:
                ch = '*'
            elif 89 <= c <= 99:
                ch = ':'
        elif r == 55:
            if 0 <= c <= 1:
                ch = '*'
            elif c == 2:
                ch = ':'
            elif c == 3:
                ch = '*'
            elif c == 4:
                ch = '.'
            elif c == 5:
                ch = ':'
            elif 6 <= c <= 12:
                ch = '*'
            elif c == 13:
                ch = '.'
            elif 14 <= c <= 20:
                ch = '*'
            elif 21 <= c <= 22:
                ch = '.'
            elif 23 <= c <= 55:
                ch = '*'
            elif c == 56:
                ch = ':'
            elif 57 <= c <= 58:
                ch = '*'
            elif c == 59:
                ch = ':'
            elif c == 60:
                ch = '*'
            elif c == 61:
                ch = ':'
            elif 62 <= c <= 65:
                ch = '*'
            elif 66 <= c <= 68:
                ch = ':'
            elif 69 <= c <= 78:
                ch = '*'
            elif c == 79:
                ch = ':'
            elif c == 80:
                ch = '*'
            elif 81 <= c <= 98:
                ch = ':'
            elif c == 99:
                ch = '*'
        elif r == 56:
            if c == 0:
                ch = ':'
            elif 1 <= c <= 31:
                ch = '*'
            elif c == 32:
                ch = '.'
            elif 33 <= c <= 36:
                ch = '*'
            elif c == 37:
                ch = ':'
            elif 38 <= c <= 47:
                ch = '*'
            elif c == 48:
                ch = ':'
            elif 49 <= c <= 65:
                ch = '*'
            elif c == 66:
                ch = ':'
            elif 67 <= c <= 75:
                ch = '*'
            elif 76 <= c <= 78:
                ch = ':'
            elif 79 <= c <= 82:
                ch = '*'
            elif c == 83:
                ch = ':'
            elif 84 <= c <= 85:
                ch = '*'
            elif 86 <= c <= 88:
                ch = ':'
            elif 89 <= c <= 99:
                ch = '*'
        elif r == 57:
            if 0 <= c <= 28:
                ch = '*'
            elif c == 29:
                ch = ':'
            elif 30 <= c <= 34:
                ch = '*'
            elif c == 35:
                ch = ':'
            elif 36 <= c <= 42:
                ch = '*'
            elif c == 43:
                ch = ':'
            elif 44 <= c <= 56:
                ch = '*'
            elif c == 57:
                ch = '.'
            elif 58 <= c <= 73:
                ch = '*'
            elif 74 <= c <= 75:
                ch = ':'
            elif 76 <= c <= 77:
                ch = '*'
            elif c == 78:
                ch = ':'
            elif c == 79:
                ch = '*'
            elif 80 <= c <= 87:
                ch = ':'
            elif c == 88:
                ch = '*'
            elif c == 89:
                ch = ':'
            elif 90 <= c <= 98:
                ch = '*'
            elif c == 99:
                ch = ':'
        elif r == 58:
            if 0 <= c <= 3:
                ch = '*'
            elif 4 <= c <= 6:
                ch = ':'
            elif 7 <= c <= 16:
                ch = '*'
            elif c == 17:
                ch = ':'
            elif 18 <= c <= 20:
                ch = '*'
            elif 21 <= c <= 23:
                ch = ':'
            elif 24 <= c <= 54:
                ch = '*'
            elif 55 <= c <= 56:
                ch = ':'
            elif 57 <= c <= 62:
                ch = '*'
            elif c == 63:
                ch = ':'
            elif c == 64:
                ch = '*'
            elif c == 65:
                ch = ':'
            elif c == 66:
                ch = '*'
            elif c == 67:
                ch = ':'
            elif c == 68:
                ch = '*'
            elif c == 69:
                ch = ':'
            elif c == 70:
                ch = '*'
            elif 71 <= c <= 72:
                ch = ':'
            elif 73 <= c <= 76:
                ch = '*'
            elif c == 77:
                ch = ':'
            elif 78 <= c <= 82:
                ch = '*'
            elif 83 <= c <= 86:
                ch = ':'
            elif 87 <= c <= 89:
                ch = '*'
            elif 90 <= c <= 96:
                ch = ':'
            elif 97 <= c <= 99:
                ch = '*'
        elif r == 59:
            if 0 <= c <= 1:
                ch = '*'
            elif c == 2:
                ch = ':'
            elif 3 <= c <= 5:
                ch = '*'
            elif 6 <= c <= 8:
                ch = ':'
            elif 9 <= c <= 39:
                ch = '*'
            elif 40 <= c <= 42:
                ch = ':'
            elif c == 43:
                ch = '*'
            elif 44 <= c <= 46:
                ch = ':'
            elif 47 <= c <= 56:
                ch = '*'
            elif c == 57:
                ch = ':'
            elif c == 58:
                ch = '*'
            elif c == 59:
                ch = ':'
            elif 60 <= c <= 65:
                ch = '*'
            elif c == 66:
                ch = ':'
            elif c == 67:
                ch = '*'
            elif c == 68:
                ch = ':'
            elif 69 <= c <= 75:
                ch = '*'
            elif 76 <= c <= 82:
                ch = ':'
            elif c == 83:
                ch = '*'
            elif 84 <= c <= 96:
                ch = ':'
            elif c == 97:
                ch = '*'
            elif 98 <= c <= 99:
                ch = ':'
        else:
            ch = " "
        line = line + ch
        c = c + 1
    print(line)
    r = r + 1
print()