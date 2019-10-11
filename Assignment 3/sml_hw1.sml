(* Nick Thompson *)

(* #1 - pow *)
(* Takes two integers as arguments and returns the result of raising the first integer to the power of the second. *)
(* Assumes that the power is not negative and that every integer to the 0 power is 1. *)
(* val pow = fn : int * int -> int *)
fun pow (base, power) = if power = 0 then 1 else base * pow(base, power - 1);


(* #2 - sumTo *)
(* Accepts an integer n and computes the sum of the first n reciprocals. *)
(* If n is 0, returns 0.0. Assumes that n not negative*)
(* For example, sumTo(3) returns (1 + 1/2 + 1/3) = 1.83333333 *)
(* val sumTo = fn : int -> real *)
fun sumTo n = if n = 0 then 0.0 else 1.0 / real(n) + sumTo(n - 1);
               
               
(* #3 - repeat *)
(* Takes a string and an integer as arguments and returns a string composed of the given number of occurrences of the string. *)
(* Assumes that the number of times the string occurs is not negative *)
(* For example, repeat("hello", 3) returns "hellohellohello" *)
(* val repeat = fn : string * int -> string *)
fun repeat (inputString, num) = if num > 0 then inputString ^ repeat(inputString, num - 1) else "";


(* #4 - binary *)
(* Takes an integer in decimal and converts it to an integer list of binary digits by appending the remainder of the decimal integer divided by 2 *)
(* val intToBin = fn : int -> int list *)
fun intToBin decNum = if decNum > 0 then intToBin(decNum div 2)@[(decNum mod 2)] else nil;

(* Takes a list of binary integers (0 or 1) and converts it to a list of binary characters (#"0" or #"1"). *)
(* Contains basic error handing so no operations are performed on an empty list *)
(* val binToChar = fn : int list -> char list *)
fun binToChar nil = nil | binToChar(binNum::binChar) = if binNum = 1 then #"1"::binToChar(binChar) else #"0"::binToChar(binChar);

(* Takes an integer n as an argument and returns a string corresponding to the binary representation of that integer. *)
(* Uses binToChar and intToBin as helper functions. *)
(* Note: Adds a leading zero because of the tests in the provided driver file. *)
(* val binary = fn: int -> string *)
fun binary n = if n > 0 then implode(#"0"::binToChar(intToBin(n))) else "";


(* #5 - countNegative *)
(* Takes a list of integers as an argument and returns a count of the number of negative integers in the list. *)
(* val countNegative = fn : int list -> int *)
fun countNegative x = if null x then 0 else if hd x >= 0 then countNegative(tl(x)) else 1 + countNegative(tl x);


(* #6 - absList *)
(* Takes a tuple of two integers and returns a tuple of the absolute value of each integer. *)
(* val absTuple = fn : int * int -> int * int *)
fun absTuple (a, b) = (abs(a), abs(b));

(* Takes a list of int * int tuples and returns a new list of int * int tuples where every integer is replaced by its absolute value. *)
(* Uses the helper function absTuple to process one tuple at a time *)
(* val absList = fn : (int * int) list -> (int * int) list *)
fun absList inputList =  if null inputList then [] else absTuple(hd inputList)::absList(tl inputList);


(* #7 - split *)
(* Takes an integer as an argument that returns a tuple obtained by splitting each integer. *)
(* The integer is split into a pair of integers whose sum equals the integer and which are each half of the original. *)
(* For odd integers, the second value is one higher than the first. *)
(* Assumes the integer is greater than or equal to 0. *)
(* For example, intToTuple 5 returns (2, 3). *)
(* val intToTuple = fn : int -> int * int *)
fun intToTuple num = if num mod 2 = 0 then (num div 2, num div 2) else (num div 2, (num div 2) + 1);

(* Takes a list of integers as an argument that returns a list of the tuples by using the helper function intToTuple *)
(* Each integer is split into a pair of integers whose sum equals the integer and which are each half of the original. *)
(* For example, split([5,6,8,17,93,0]) returns [(2,3), (3,3), (4,4), (8,9), (46,47), (0,0)]. *)
(*val split = fn : int list -> (int * int) list *)
fun split intList = if null intList then [] else intToTuple(hd intList)::split(tl intList);


(* #8 - isSorted *)
(* Takes a list of integers and returns whether or not the list is in sorted (nondecreasing) order (true if it is, false if it is not). *)
(* By definition, the empty list and a list of one element are considered to be sorted. *)
(* val isSorted = fn : int list -> bool *)
fun isSorted inputList = if null inputList then true else if length(inputList) = 1 then true else if hd inputList <= hd(tl inputList) then (true; isSorted(tl inputList)) else false;

 
(* #9 - collapse *) 
(* Takes a list of integers as an argument and returns the list obtained by collapsing successive pairs in the original list by replacing each pair with its sum. *)
(* For example, collapse([1,3,5,19,7,4]) returns [4,24,11] *)
(* If the list has an odd length, the final number in the list is not collapsed. For example, collapse([1,2,3,4,5]) returns [3,7,5]. *)
(* val collapse = fn : int list -> int list *) 
fun collapse (intList::nil) = [intList] | collapse(a::b::leftOver) = if length(leftOver) > 0 then (a + b)::collapse(leftOver) else [a + b];

        
(* #10 - insert *)       
(* Takes an integer and a sorted (nondecreasing) integer list as parameters and returns the list obtained by inserting the integer into the list so as to preserve sorted order. *)
(* For example, insert(8,[1,3,7,9,22,38]) returns [1,3,7,8,9,22,38]. *)
(* val insert = fn : int * int list -> int list *)        
fun insert(num, nil) = [num] | insert(num, head::tail) = if num <= head then num::head::tail else head::(insert(num, tail));