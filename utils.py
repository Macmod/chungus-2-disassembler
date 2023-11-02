def strip_nops(assembly):
    limit = len(assembly)
    for k in range(len(assembly)-1,0,-1):
        if assembly[k] == '0'*16:
            limit = k
        else:
            break

    return assembly[:limit]

