use "sml_hw1.sml";

fun pass_fail x = if x then "Pass" else "Fail";

fun test(function, input, expected_output) = pass_fail ((function(input) = expected_output));

fun error_print (n, f) = print (Int.toString(n)^"."^f^": Error encountered in test of " ^f^"\n");

print("*********TEST RESULTS******************\n");
print("\n1.Pow: "^test(pow, (2,3), 8)^"\n") handle _ => error_print (1, "pow");
print("\n2.Pow: "^test(pow, (~2,3), ~8)^"\n") handle _ => error_print (2, "pow");
print("\n3.Pow: "^test(pow, (2,0), 1)^"\n") handle _ => error_print (3, "pow");
print("\n4.Binary: "^test(binary, 17, "010001")^"\n") handle _ => error_print(4, "binary");
print("\n5.Binary: "^test(binary, 1023, "01111111111")^"\n") handle _ => error_print(5, "binary");
print("\n6.Binary: "^test(binary, 117, "01110101")^"\n") handle _ => error_print(6, "binary");
print("\n7.Repeat: "^test(repeat, ("hello", 3), "hellohellohello")^"\n") handle _ => error_print(7, "repeat");
print("\n8.CountNegative: "^test(countNegative,[3,17,~9,34,~7,2],2)^"\n") handle _ => error_print(8, "countNegative") ;
print("\n9.CountNegative: "^test(countNegative,[3,17,9,34,7,2],0)^"\n") handle _ => error_print(9, "countNegative");
print("\n10.absList: "^test(absList,[(~38,47), (983,~14), (~17,~92), (0,34)], [(38,47),(983,14), (17,92), (0,34)])^"\n") handle _ => error_print(10, "absList");
print("\n11.split: "^test(split,[5,6,8,17,93,0],[(2,3), (3,3), (4,4), (8,9), (46,47), (0,0)])^"\n") handle _ => error_print(11, "split");
print("\n12.split: "^test(split,[5,1,8,17,93,0],[(2,3), (0,1), (4,4), (8,9), (46,47), (0,0)])^"\n") handle _ => error_print(12, "split");
print("\n13.isSorted: "^test(isSorted, [1,2,3,4,4,5,5], true)^"\n") handle _ => error_print(13, "isSorted");
print("\n14.isSorted: "^test(isSorted, [1,2,3,4,3,5,5], false)^"\n") handle _ => error_print(14, "isSorted");
print("\n15.isSorted: "^test(isSorted, [1], true)^"\n") handle _ => error_print(15, "isSorted");
print("\n16.isSorted: "^test(isSorted, [], true)^"\n") handle _ => error_print(16, "isSorted");
print("\n17.isSorted: "^test(isSorted, [1,1,1,1,1], true)^"\n") handle _ => error_print(17, "isSorted");
print("\n18.Collapse: "^test(collapse,[1,3,5,19,7,4],[4,24,11])^"\n") handle _ => error_print(18, "collapse");
print("\n19.Collapse: "^test(collapse,[1,2,3,4,5],[3,7,5])^"\n") handle _ => error_print(19, "collapse");
print("\n20.Collapse: "^test(collapse,[1,2],[3])^"\n") handle _ => error_print(20, "collapse");
print("\n21.Collapse: "^test(collapse,[1],[1])^"\n") handle _ => error_print(21, "collapse");
print("\n22.Insert: "^test(insert,(8,[1,3,7,9,22,38]), [1,3,7,8,9,22,38])^"\n") handle _ => error_print(22, "insert");
print("\n23.Insert: "^test(insert,(88,[1,3,7,9,22,38]), [1,3,7,9,22,38,88])^"\n") handle _ => error_print(23, "insert");
print("\n24.Insert: "^test(insert,(0,[1,3,7,9,22,38]), [0,1,3,7,9,22,38])^"\n") handle _ => error_print(24, "insert");
print("\n25.Insert: "^test(insert,(22,[1,3,7,9,22,38]), [1,3,7,9,22,22,38])^"\n") handle _ => error_print(25, "insert");

