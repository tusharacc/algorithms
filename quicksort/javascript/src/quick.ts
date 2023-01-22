let arr:Array<number> = [3,8,1,98,34,12,90]

quicksort(arr,0,6)
function quicksort(arr:Array<number>, lo:number, hi:number){
    let j:number = partition(arr,lo,hi);
    quicksort(arr,lo,j-1)
    quicksort(arr,j+1,hi)
    console.log(`lo:${lo} --- hi:${hi}`);
    console.log('Array', arr)
}

function swap(arr:Array<number>, idx1:number, idx2:number){
    let temp: number = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
}

function partition(arr:Array<number>, lo:number, hi:number): number{
    let pivot:number = getRandomIntInclusive(lo,hi)
    
    swap(arr,lo,pivot)
    let i:number = lo+1;
    let j:number = hi;
    while (true){
        while (true){
            if (arr[i] >= arr[lo]){
                break
            }
            i += 1
        }
        while (true){
            if (arr[j] <= arr[lo]){
                break
            }
            j -= 1
        }

        if (i >= j){
            break
        }

        swap(arr,i,j)
        
    }
    return lo;
}

function getRandomIntInclusive(min:number, max:number):number{
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
  }
  