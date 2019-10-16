(* Nick Thompson *)

(* #1 - quicksort *)
(* Implements Lomuto’s partitioning algorithm. *)
(* If the input list is empty, returns two empty lists. Otherwise calls the function recursively with the pivot and rest of the list *)
(* and assigns those values to smallerNums and largerNums respectively. If the first element of the list is less than the pivot, *)
(* inserts it into the int list smallerNums. Otherwise, inserts it into the int list largerNums. *)
(* val partition = fn : int * int list -> int list * int list *)
fun partition (_, nil) = (nil, nil) |
	partition (pivot, first::rest) =
		let
			val (smallerNums, largerNums) = partition(pivot, rest)
		in
			if first < pivot
				then (first::smallerNums, largerNums)
			else
				(smallerNums, first::largerNums)
		end;
		
(* Implements quicksort using the above implementation of Lomuto’s partitioning algorithm with the pivot initalized *)
(* to the first index of the input list. Relies on the helper function "partition(int, int list)" for partitioning. *)
(* If the input list is empty, returns an empty list. Otherwise, calls partition with the pivot and the rest of the list *)
(* and assigns those values to smallerNums and largerNums respectively. smallerNums is an int list with integers less than the pivot, *)
(* and largerNums is an int list with integers greater than the pivot. The function then recursively calls itself with the int list *)
(* smallerNums concatenated with the pivot concatenated to the recursive call with the int list largerNums. *)
(* val quicksort = fn : int list -> int list *)
fun quicksort nil = nil |
	quicksort (pivot::rest:int list) =
		let
			val (smallerNums, largerNums) = partition(pivot, rest)
		in
			quicksort(smallerNums) @ [pivot] @ quicksort(largerNums)
		end;


(* #2 - member *)
(* Sequentially searches a list and returns a boolean value depending on if the element is in the list. *)
(* If the list is empty, the element cannot be in the list and therefore returns false. *)
(* val member = fn : ''a * ''a list -> bool *)
fun member (_, nil) = false |
	member (element, first::rest) = element = first orelse member(element, rest);
               
               
(* #3 - returns the union of sets (lists) set1 and set2*)
(* If one of the lists is empty, returns the other. Otherwise, uses the above "member(a, a list)" function to determine if the first *)
(* element of the first list is an element of the second list. If it is an element, recursively calls this function with the rest *)
(* of the first list and all of the second list. If it is not an element, inserts the first element of the first list to the *)
(* recursive call with the rest of the first list and all of the second list. *)
(* Assumes that set1 and set2 do not have any duplicate elements in their own list. *)
(* val union = fn : ''a list * ''a list -> ''a list *)
fun union (set1, nil) = set1 |
	union (nil, set2) = set2 |
	union (set1First::set1Rest, set2) = 
		if member(set1First, set2) 
			then union(set1Rest, set2) 
		else 
			set1First::union(set1Rest, set2);
	

(* #4 - returns the intersection of sets (lists) set1 and set2 *)
(* If one of the lists is empty, returns an empty list. Otherwise, uses the above "member(a, a list)" function to determine if the first *)
(* element of the first list is an element of the second list. If it is an element, inserts the first element of the first list *)
(* to the recursive call with the rest of the first list and all of the second list. If it is not an element, *)
(* recursively calls this function with the rest of the first list and all of the second list. *)
(* Assumes that set1 and set2 do not have any duplicate elements in their own list. *)
(* val intersection = fn : ''a list * ''a list -> ''a list *)
fun intersection (_, nil) = nil |
	intersection (nil, _) = nil |
	intersection (set1First::set1Rest, set2) = 
		if member(set1First, set2) 
			then set1First::intersection(set1Rest, set2)
		else 
			intersection(set1Rest, set2);

(* #5 - Returns the list of integers from start (inclusive) to stop (exclusive) by step *)
(* If the starting number is greater than the stopping number and the step size is negative, *)
(* or if the starting number is less than the stopping number and the step size is positive, *)
(* inserts the starting number into the recursive call with the function with the new starting number increased/decreased by the step size. *)
(* If neither of the two conditions are true, returns an empty list. *)
(* val range = fn : int * int * int -> int list *)
fun range(start, stop, step) = 
	if start > stop andalso step < 0
	orelse start < stop andalso step > 0
		then start::range(start+step, stop, step)
	else 
		nil;

(* #6 - Returns a slice of a list between indices start (inclusive), and stop (exclusive). Assumes the first element of list is at index 0*)
(* If the list is empty, returns an empty list. Otherwise, uses a counter to determine if the count of current recursive call is between *)
(* the start index (inclusive) and the stop index (exclusive). If it is between the indices, inserts the first element of the current *)
(* recursive call to the rest of the list and recursively calls the function with the rest of the list, the start index, the stop index, *)
(* and the counter increased by one. Otherwise, if the count of the current recursive call is not between the start index (inclusive) and *)
(* the stop index (exclusive), recursively calls the function with the rest of the list, the start index, the stop index, and the counter *)
(* increased by one. *)
(* val sliceWithCounter = fn : 'a list * int * int * int -> 'a list *)
fun sliceWithCounter(nil, start, stop, count) = nil |
	sliceWithCounter(first::rest, start, stop, count) = 
		if count >= start andalso count < stop
			then first::sliceWithCounter(rest, start, stop, count+1)
		else 
			sliceWithCounter(rest, start, stop, count+1);

(* Calls "sliceWithCounter" with the inputted list, start index, stop index, and 0 (the initial count). *)
(* val slice = fn : 'a list * int * int -> 'a list *)
fun slice(aList, start, stop) = sliceWithCounter(aList, start, stop, 0);