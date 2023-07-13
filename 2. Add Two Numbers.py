class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Помічник вузол для початку зв'язаного списку
        current = dummy  # Вказівник на поточний вузол
        carry = 0  # Змінна переносу для додавання

        while l1 or l2 or carry:
            # Отримуємо значення з двох списків
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Обчислюємо суму цифр та перенос
            total = val1 + val2 + carry
            carry = total // 10  # Перенос - ціла частина від ділення на 10
            digit = total % 10  # Одинична цифра - остача від ділення на 10

            # Створюємо новий вузол та пересуваємо вказівник поточного вузла
            current.next = ListNode(digit)
            current = current.next

            # Переміщуємо вказівник наступного вузла в кожному зі списків
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Повертаємо початок зв'язаного списку