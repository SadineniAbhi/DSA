def insert_at_bottom(stack,ins_ele):
    if len(stack) == 0:
        stack.append(ins_ele)
    elif stack[-1] < ins_ele:
        stack.append(ins_ele)
    else:
        ele = stack.pop()
        insert_at_bottom(stack,ins_ele)
        stack.append(ele)


def pop_all_stack(stack):
    if len(stack) == 0:
        return
    ele = stack.pop()
    pop_all_stack(stack)
    insert_at_bottom(stack,ele)


stack = [5,1,3,2,4]
pop_all_stack(stack)
print(stack)