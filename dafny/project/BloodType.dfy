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
    reads this, list
    {
        list!=null && list.Length!=0 && 0<=first<=last<=list.Length && shadow==list[first..last] 
    }

    predicate ValidBT()
    reads this, list
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


    method addBloodBag(ID: int, expDate: int, arvDate: int, newBloodType: string) 
    requires ValidBT()
    requires newBloodType == "A" || newBloodType == "B" || newBloodType == "O" || newBloodType == "AB"
    ensures ValidBT()
    modifies this
    {
        var node:BloodBags<int, string> := Leaf(ID, expDate, arvDate, newBloodType);
        
    }

}

method Main() {
    var a : array<BloodBags<int, string>> := new BloodBags[4];
    var Leaf1:BloodBags<int, string> := Leaf(1,1,1,"A");
    var Leaf2:BloodBags<int, string> := Leaf(2,2,2,"B");
    a[0], a[1] := Leaf1, Leaf2;
    print a[0], a[1], '\n';
    var Leaf3:BloodBags<int, string> := a[0];
    print Leaf3, '\n';
    //var bloodyType := new BloodType("A", 15);
    
    
}