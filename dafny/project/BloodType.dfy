// The datatype to store the valuable information of ID, expirayDate, arrivalDate of the bloodBag (in that order)
datatype BloodBags<B> = Leaf(B, B, B) | Node(B, B, B, BloodBags<B>)

class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    var Leaf1:BloodBags<int>; 
    var t1:BloodBags<int>;

    predicate ValidBT()
    reads this
    {
        this in footprint &&
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == "A" || bloodType == "B" || bloodType == "O" || bloodType == "AB") 
    }
    
    constructor()
    ensures ValidBT()
    ensures fresh(footprint - old(footprint))
    modifies this, footprint
    {
        bloodType := bloodtype;
        lowest := critical;
        quantity := 0;
    }
    
}