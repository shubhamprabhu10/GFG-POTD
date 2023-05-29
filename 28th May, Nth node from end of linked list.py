def getNthFromLast(head,n):
    lst = []
    while head:
        lst.append(head.data)
        head= head.next
    l = len(lst)
    nd = l - n
    if nd < 0:
        return -1
    else:
        return lst[nd]
