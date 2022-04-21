
#**************************************###############################*************************************
#**************************************###############################*************************************
#**************************************###############################*************************************
#ALGOEXPERT-MEDIUM-Q-Array Of Products-Solution 1:

# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]

#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i!=j:
#                 runningProduct *= array[j]
#         products[i] = runningProduct

#     return products


# print(arrayOfProducts([5,1,4,2]))



#**************************************###############################*************************************
#**************************************###############################*************************************
#**************************************###############################*************************************
#ALGOEXPERT-MEDIUM-Q-Array Of Products-Solution 2:

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1

    for i in range(len(array)):
       leftProducts[i] = leftRunningProduct
       leftRunningProduct *= array[i]
    
    rightRunningProduct = 1

    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i]* rightProducts[i]

    return products


print(arrayOfProducts([5,1,4,2]))