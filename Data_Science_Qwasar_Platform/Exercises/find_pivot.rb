def find_pivot(param_1, param_2)
    i = 0
    j = 1
    k = 0
    sum1 = 0
    sum2 = 0

    while j < param_2
        i = 0
        sum1=0
        sum2=0
        while i < j
            k = j+1
            sum1 += param_1[i]
            i += 1
        end
        while k < param_2
            sum2 += param_1[k]
            k += 1
        end
        if sum1 == sum2
            return j
        end
        j += 1
    end
    return -1
end