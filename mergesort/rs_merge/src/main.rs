use std::process;

fn main() {
    let mut a:[i32;8] = [8,4,9,2,6,5,3,7];
    let array = &mut a[0..8];
    println!("{:?}",array);
    divide(array,0,8);
    println!("{:?}",array);
}

fn divide(array: &mut [i32],low:usize, high:usize) {

    println!("Function Divide:Array low :{}, High :{}",low,high);
    if (array[low..high].len() == 1){
        return;
    } 
    let length:usize = array[low..high].len();
    let mid: usize = low + length /2;
    let left_arr = divide(array,low,mid);
    //println!("The low:{}, high: {}, mid: {}", low,high,mid);
    let right_arr = divide(array,mid,high);
    merge_sort(array,low, mid, high);
}

fn merge_sort(array: &mut [i32], low:usize, mid:usize, high:usize){

    println!("Low :{}, mid :{}, high :{}",low, mid,high);
    let mut right_arr: Vec<i32>;
    let mut left_arr: Vec<i32>;
    right_arr = array[low..mid].to_vec();
    left_arr = array[mid..high].to_vec();
    
    println!("{:?} - left array",left_arr);
    println!("{:?} - right array",right_arr);
    let length:usize = right_arr.len();
    let mut left_len: usize = 0;
    let mut right_len: usize = 0;
    let mut index:usize = low;
    loop {
        println!("Left Len: {}, Right Len: {}, length: {}",left_len,right_len, length);
        if left_len < length && right_len < length{
            if left_arr[left_len] < right_arr[right_len]{
                array[index] = left_arr[left_len];
                index += 1;
                left_len += 1;
            } else {
                array[index] = right_arr[right_len];
                index += 1;
                right_len += 1;
            }
        } else if left_len < length{
            array[index] = left_arr[left_len];
            index += 1;
            left_len += 1;
        } else if right_len < length {
            array[index] = right_arr[right_len];
            index += 1;
            right_len  += 1;
        } else if (left_len >= length && right_len >= length){
            break;
        }
    }
    
}
