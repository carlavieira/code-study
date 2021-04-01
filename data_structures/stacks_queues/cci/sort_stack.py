def sort_stack(stack):
    aux_stack = []
    while stack:
        #take the last element of the stack
        tmp = stack.pop()
        #while the new element its smaller than the top of the aux stack, its change puts back the biggers nums to the old stack
        while aux_stack and aux_stack[-1] > tmp:
            stack.append(aux_stack.pop())
        # acidiona o menor numero visto até então na posição certa da nova pilha
        aux_stack.append(tmp)

    while aux_stack:
        stack.append(aux_stack.pop())


