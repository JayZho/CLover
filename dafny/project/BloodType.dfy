// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
datatype BloodBags<B, C> = Leaf(B, B, B, C) | Node(B, B, B, BloodBags<B, C>)

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

    method addBloodBag(ID: int, expDate: int, arvDate: int) returns(test: bool)
    requires ValidBT()
    ensures ValidBT()
    modifies this
    {
        var node:BloodBags<int> := Node(ID, expDate, arvDate, temp1);
        temp1 := node;
    }

}

method Main() {
    var bloodyType := new BloodType();

}