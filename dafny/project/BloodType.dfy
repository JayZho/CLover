// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
// Which are int while the last variable C is the bloodtype string value
datatype BloodBags<B, C> = Leaf(B, B, B, C) 

class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    var a : array<BloodBags<int, string>>
    //ghost var shadow: seq<Data>;

    predicate ValidBT()
    reads this
    {
        this in footprint &&
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == "A" || bloodType == "B" || bloodType == "O" || bloodType == "AB") &&
        a != null
    }
    
    constructor(bloodtype: string, critical: int)
    requires critical >= 0 
    requires bloodtype == "A" || bloodtype == "B" || bloodtype == "O" || bloodtype == "AB"
    ensures ValidBT()
    modifies this
    {
        bloodType := bloodtype;
        lowest := critical;
        quantity := 0;
        a := new BloodBags[1];
        footprint := {this};
    }


    method addBloodBag(ID: int, expDate: int, arvDate: int, newBloodType: string) 
    requires ValidBT()
    requires newBloodType == "A" || newBloodType == "B" || newBloodType == "O" || newBloodType == "AB"
    ensures ValidBT()
    modifies this
    {
        //var node:BloodBags<int, string> := Node(ID, expDate, arvDate, newBloodType, temp1);
        //temp1 := node;
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