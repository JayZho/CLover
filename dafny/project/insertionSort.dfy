
predicate isSorted(a: array<int>, start:int, end:int)
requires a != null 
requires 0<=start<=end<=a.Length
reads a
{ 
    forall x, y:: start<=x<y<end ==> a[x]<=a[y] 
}

method InsertionSort(toSort: array<int>)
requires toSort != null 
requires toSort.Length > 1
ensures isSorted(toSort, 0, toSort.Length);
ensures multiset(toSort[..]) == multiset(old(toSort[..]));
modifies toSort;
{
    var sortedUpTo:=1;
    while (sortedUpTo < toSort.Length)

    invariant 1 <= sortedUpTo <= toSort.Length;
    invariant isSorted(toSort, 0, sortedUpTo);
    invariant multiset(toSort[..]) == multiset(old(toSort[..]));
    {
        var start := sortedUpTo; // the next unordered element
        while (start >= 1 && toSort[start-1] > toSort[start])

        invariant 0 <= start <= sortedUpTo;
        invariant forall i,j:: (0<=i<j<=sortedUpTo && j!=start) ==> toSort[i]<=toSort[j];
        invariant multiset(toSort[..]) == multiset(old(toSort[..]));
        {
            toSort[start-1], toSort[start] := toSort[start], toSort[start-1];
            start:=start-1;
        }
        sortedUpTo:=sortedUpTo+1;
    }
}