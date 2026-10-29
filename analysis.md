In a linked-list stack, elements are added and removed at the head to preserve a constant 
$O(1)$ time efficiency. If these actions were executed at the tail, a full traversal of the list would be necessary, 
degrading performance to $O(n)$. Meanwhile, an array-based queue requires a circular design to 
optimize memory utilization. As items leave from the front, those vacated positions can be recycled. 
By applying the modulo operator to loop the indices back around, the queue avoids unused storage blocks and 
bypasses the costly $O(n)$ operation of shifting all remaining elements forward.


