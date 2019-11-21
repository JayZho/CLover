// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
// Which are int while the last variable C is the bloodtype string value
datatype BloodBags<B, C> = Leaf(B, B, B, C) 

class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    var list : array<BloodBags<int, string>>
    var first: int, last: int; // indexes in list[]
    ghost var shadow: seq<BloodBags<int, string>>;

    predicate ValidSort()
    reads this, this.list
    {
        list!=null && list.Length!=0 && 0<=first<=last<=list.Length && shadow==list[first..last] 
    }

    predicate ValidBT()
    reads this, this.list
    {
        this in footprint &&
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == "A" || bloodType == "B" || bloodType == "O" || bloodType == "AB") &&
        list != null
    }
    
    constructor(bloodtype: string, critical: int, size: int)
    requires critical >= 0 
    requires bloodtype == "A" || bloodtype == "B" || bloodtype == "O" || bloodtype == "AB"
    requires size>0
    ensures shadow == []
    ensures fresh(list)
    ensures ValidSort();
    ensures ValidBT()
    modifies this
    {
        bloodType := bloodtype;
        lowest := critical;
        quantity := 0;
        list := new BloodBags[size];
        first, last, shadow := 0, 0, [];
        footprint := {this};
    }

    method getList() returns(value: array<BloodBags<int, string>>)
    requires ValidBT()
    ensures value == list
    {
        value := list;
    }

    method addBloodBag(data: BloodBags<int, string>) 
    requires ValidBT() && ValidSort()
    requires list != null;
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

}

method Main() {
    /*
    var a : array<BloodBags<int, string>> := new BloodBags[4];
    var Leaf1:BloodBags<int, string> := Leaf(1,1,1,"A");
    var Leaf2:BloodBags<int, string> := Leaf(2,2,2,"B");
    a[0], a[1] := Leaf1, Leaf2;
    print a[0], a[1], '\n';
    var Leaf3:BloodBags<int, string> := a[0];
    print Leaf3, '\n';
    */
    var bloodyType := new BloodType("A", 15, 10);
    var Leaf1:BloodBags<int, string> := Leaf(1,1,1,"A");
    var Leaf2:BloodBags<int, string> := Leaf(2,2,2,"B");
    //bloodyType.addBloodBag(Leaf1);
    var me := bloodyType.getList();
   // assert me[0] == Leaf1;
    print me, '\n';
    
    
}