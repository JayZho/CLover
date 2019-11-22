method BubbleSort(arr: array<int>)
  modifies arr
  requires arr != null
  requires arr.Length >= 1
  ensures forall m, n :: 0  <= m <= n <= arr.Length-1 < arr.Length ==> arr[m] <= arr[n]
  {

    var last := arr.Length - 1;

    while(last > 0)
      invariant  0 <= last <= arr.Length-1
      invariant forall m, n :: 0 <= last <= m <= n <= arr.Length-1 < arr.Length ==> arr[m] <= arr[n]
      invariant forall c, c' :: 0 <= c <= last < c' < arr.Length ==> arr[c] <= arr[c']
      {
        var index := 0;

        while (index < last)
          invariant 0 < last < arr.Length && 0 <= index <= last
          invariant forall m, n :: 0 <= last <= m <= n <= arr.Length-1 < arr.Length ==> arr[m] <= arr[n]
          invariant forall c, c' :: 0 <= c <= last < c' < arr.Length ==> arr[c] <= arr[c']
          invariant forall c :: 0 <= c <= index ==> arr[c] <= arr[index]
          {
            if(arr[index] > arr[index+1])
              {
                var tmp := arr[index];
                arr[index] := arr[index+1];
                arr[index+1] := tmp;

              }
              index := index + 1;
          }
          last := last -1;
      }

 }
