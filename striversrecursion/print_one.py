def counts(count,N):
    if count == 0:
        return
    print(count)
    counts(count-1)
counts(5)