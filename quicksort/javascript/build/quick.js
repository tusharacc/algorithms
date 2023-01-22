"use strict";
var arr = [3, 8, 1, 98, 34, 12, 90];
quicksort(arr, 0, 6);
function quicksort(arr, lo, hi) {
    var j = partition(arr, lo, hi);
    quicksort(arr, lo, j - 1);
    quicksort(arr, j + 1, hi);
    console.log("lo:".concat(lo, " --- hi:").concat(hi));
    console.log('Array', arr);
}
function swap(arr, idx1, idx2) {
    var temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
}
function partition(arr, lo, hi) {
    var pivot = getRandomIntInclusive(lo, hi);
    swap(arr, lo, pivot);
    var i = lo + 1;
    var j = hi;
    while (true) {
        while (true) {
            if (arr[i] >= arr[lo]) {
                break;
            }
            i += 1;
            if (i > hi){
                break;
            }
        }
        while (true) {
            if (arr[j] <= arr[lo]) {
                break;
            }
            j -= 1;
            if (j < lo){
                break;
            }
        }
        if (i >= j) {
            break;
        }
        swap(arr, i, j);
    }
    //swap(arr,i,lo)
    return i;
}
function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}
