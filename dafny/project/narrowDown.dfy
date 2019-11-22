
predicate inDifference(original: multiset<int>, curr: multiset<int>, key: int)
{
  key in original-curr
}


method narrowDown(bags: array<int>, start: int, end: int) returns (selected: seq<int>)

requires start <= end
ensures forall x:: 0<=x<|selected| ==> start<=selected[x]<=end
//ensures forall x:: inDifference(multiset(bags[..]), multiset(selected[..]), x) ==> !(start<=x<=end)
{
    var i := 0;
    selected := [];
    while i < bags.Length
    invariant 0<=i<=bags.Length
    invariant forall x:: 0<=x<|selected| ==> start<=selected[x]<=end
    //invariant forall x:: inDifference(multiset(bags[..i]), multiset(selected[..]), x) ==> !(start<=x<=end)
    {
        if start<=bags[i]<=end{
            selected := selected + [bags[i]];
        }
        i := i + 1;
    }
}
  
  
  
  
  
 
