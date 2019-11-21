// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
datatype BloodBags<B, C> = Leaf(B, B, B, C) | Node(B, B, B, C, BloodBags<B, C>)

class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    var temp1:BloodBags<int, string>; 
    var temp2:BloodBags<int, string>; 

    predicate ValidBT()
    reads this
    {
        this in footprint &&
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == "A" || bloodType == "B" || bloodType == "O" || bloodType == "AB") 
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
        temp1 := Leaf(0, 0, 0, " ");
        footprint := {this};
    }

    method getTemp1() returns(thing :BloodBags<int, string>)
    requires ValidBT()
    ensures ValidBT()
    ensures thing == temp1
    {
        thing := temp1;
    }

    method addBloodBag(ID: int, expDate: int, arvDate: int, newBloodType: string) 
    requires ValidBT()
    requires newBloodType == "A" || newBloodType == "B" || newBloodType == "O" || newBloodType == "AB"
    ensures ValidBT()
    modifies this
    {
        var node:BloodBags<int, string> := Node(ID, expDate, arvDate, newBloodType, temp1);
        temp1 := node;
    }

}

method Main() {
    var bloodyType := new BloodType("A", 15);
    bloodyType.addBloodBag(1, 12, 13, "A");
    var test := bloodyType.getTemp1();
    print test, '\n';
}