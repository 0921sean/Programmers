def solution(phone_book):
    phone_dict = {}
    
    for phone in phone_book:
        phone_dict[phone] = 1
        
    for phone in phone_book:
        tmp = ""
        for digit in phone[:-1]:
            tmp += digit
            if tmp in phone_dict.keys():
                return False
    return True

# 테스트할 케이스들
if __name__ == "__main__":
    phone_book_list = [["119", "97674223", "1195524421"], ["123", "456", "789"], ["12", "123", "1235", "567", "88"]]
    for phone_book in phone_book_list:
        result = solution(phone_book)
        print(result)