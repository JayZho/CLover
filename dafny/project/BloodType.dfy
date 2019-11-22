// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
// Which are int(B) while the last variable is the bloodtype string(C) value
datatype BloodBags<B, C> = Leaf(B, B, B, C) 

class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    // The array of BloodBags
    var list : array<BloodBags<int, string>>
    var first: int, last: int; // indexes in list[]
    ghost var shadow: seq<BloodBags<int, string>>;
    
    constructor(bloodtype: string, critical: int, size: int)
    requires critical >= 0 
    requires bloodtype == "A" || bloodtype == "B" || bloodtype == "O" || bloodtype == "AB"
    requires size>0
    ensures shadow == []
    ensures fresh(list)
    ensures ValidSort() && ValidBT()
    ensures list.Length == size
    modifies this
    {
        bloodType := bloodtype;
        lowest := critical;
        quantity := 0;
        var temp : array<BloodBags<int, string>> := new BloodBags[size];
        list := temp;
        first, last, shadow := 0, 0, [];
        footprint := {this};
    }
    // COMPLETE: TOOK ME A BLOODY LONG TIME TO FIGURE THIS OUT LOLS
    // MAIN PROBLEM IS THAT YOU FIRST HAVE TO write
    //  var temp : array<BloodBags<int, string>> := bloodyType.getList(); in the main
    // not just var temp := bloodyType.getList();
    method getList() returns(value: array<BloodBags<int, string>>)
    requires ValidBT()
    ensures value == list
    {
        value := list;
    }
    
    method addBloodBag(data: BloodBags<int, string>) 
    requires ValidBT() && ValidSort()
    requires list != null
    requires list.Length > 0
    ensures shadow == old(shadow) + [data] 
    ensures |shadow| == |old(shadow)| + 1
    ensures if old(last) == old(list.Length) then fresh(list) else list == old(list)
    ensures ValidBT() && ValidSort()
    modifies this, this.list
    {
        
        if (last == list.Length) {
            var b:= new BloodBags[list.Length]; 
            if (first==0) { 
                b:= new BloodBags[2*list.Length]; 
            } 
            forall (i | 0<=i<last-first) { 
                b[i]:= list[first+i]; 
            }
            list, first, last:= b, 0, last-first; 
        }
        list[last], last := data, last+1; 
        shadow := shadow + [data]; 
    }
    // VERFY THE PUSH AND PULL ALGORITHM
    predicate ValidSort()
    reads this, this.list
    {
        list!=null && list.Length!=0 && 0<=first<=last<=list.Length && shadow==list[first..last] 
    }
    // VERFIES THE CONCRETE VALUES OF THE CLASS
    predicate ValidBT()
    reads this, this.list
    {
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == "A" || bloodType == "B" || bloodType == "O" || bloodType == "AB") 
        //list != null
    }
    //NOT COMPLETE; VERFIES BUT VERY STUPID
    method removeBloodBag(bagID: int)
    requires ValidBT() && ValidSort()
    requires list != null
    requires list.Length > 0
    requires shadow != []
    //ensures 
    //ensures |shadow| == |old(shadow)| - 1
    //ensures ValidSort()
    ensures list != null
    modifies this, this.list
    {
        var length := list.Length;
        var newList : array<BloodBags<int, string>> := new BloodBags[length];
        /*
        var Leaf:BloodBags<int, string> := Leaf(0,0,0," ");
        var tick := 0;
        var length := list.Length;
        while (tick != length) 
        invariant 0<= tick <= length
        invariant newList != null && newList.Length > 0;
        {
            //var Leaf:BloodBags<int, string> := Leaf(0,0,0," ");
            newList[tick] := Leaf;
            assert newList[tick] == Leaf;
            tick := tick + 1;
            print tick, ' ', newList[1], ' ',newList.Length, '\n';
        }
        assert tick == length;
        assert newList[tick] == Leaf;
        */
        var counter: int, index: int;
        counter, index := 0, 0;
        while ((counter < last))
        invariant newList != null && newList.Length > 0;
        {   
            var next : BloodBags<int, string> := list[counter];
            match next
            {
                case Leaf(a, b, c, d) => if a != bagID {}//temp1[index]:=next; index := index+1;}
            }
            //newList[index]:=next;
            counter := counter+1;
        }
        list, last := newList, 9;
        
    }
    

}

method Main() {
    var bloodyType := new BloodType("A", 15, 10);
    var Leaf1:BloodBags<int, string> := Leaf(1,1,1,"A");
    var Leaf2:BloodBags<int, string> := Leaf(2,2,2,"B");
    var Leaf3:BloodBags<int, string> := Leaf(3,3,3,"O");
    var temp : array<BloodBags<int, string>> := bloodyType.getList();
    bloodyType.addBloodBag(Leaf1);
    bloodyType.addBloodBag(Leaf2);
    bloodyType.removeBloodBag(1);
    
    temp[2]:=Leaf3;

    print temp.Length, '\n';
    print temp[0], ' ', Leaf1, ' ', temp[1], ' ', Leaf2, temp[2], ' ', Leaf3, '\n';
       
}