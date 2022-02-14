def get_summ(one, two, delimiter='&'):
    summ_str = f'{one}{delimiter}{two}'
    return(summ_str)
print(get_summ('Learn', 'python').upper())