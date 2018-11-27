validPaths = [] 
def findValidPaths(arr,numOfRows,numOfCols): 
    path = [0 for d in range(numOfRows+numOfCols-1)] 
    #print(path)
    findValidPathsUtil(arr,numOfRows,numOfCols,0,0,path,0)
      
def findValidPathsUtil(arr,numOfRows,numOfCols,rowIndex,colIndex,path,indx): 
    print("[%d, %d], index=%d" % (rowIndex,colIndex,indx))
    if(arr[rowIndex][colIndex]==0):
        return
    
    if rowIndex==numOfRows-1: 
        for k in range(colIndex,numOfCols): 
            #print("k=%d" % k)
            path[indx+k-colIndex] = arr[rowIndex][k] 
        #print("-------------") 
        validPaths.append(path) 
        return
    
    if colIndex == numOfCols-1: 
        for k in range(rowIndex,numOfRows): 
            path[indx+k-rowIndex] = arr[k][colIndex] 
        #print(path) 
        validPaths.append(path) 
        return
    path[indx] = arr[rowIndex][colIndex] 
    findValidPathsUtil(arr, numOfRows, numOfCols, rowIndex+1, colIndex, path, indx+1) 
    print("----------------------------------") 
    findValidPathsUtil(arr, numOfRows, numOfCols, rowIndex, colIndex+1, path, indx+1) 
  
lt=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
#lt=[[1, 1], [0, 1]]
findValidPaths(lt,len(lt),len(lt[0])) 
print(len(validPaths))