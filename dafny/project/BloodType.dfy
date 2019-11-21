datatype BB = BloodBags 
datatype Tree<T> = Leaf(T) | Node1(T, Tree<T>) | Node2(T, Tree<T>, Tree<T>)
class BloodType 
{
    ghost var footprint: set<object>;
    var bloodType: string;
    var lowest: int;
    var quantity: int;
    var listOfBloodBag: array<BB>:= new BB[4]

    predicate ValidBT()
    reads this, BloodBags
    {
        {this, listOfBloodBags} <= footprint &&
        listOfBloodBags.footprint <= footprint &&
        this !in listOfBloodBags.footprint &&
        listOfBloodBags.ValidBB() &&
        lowest >= 0 &&
        quantity >= 0 &&
        (bloodType == 'A' || bloodType == 'B' || bloodType == 'O') 
    }

    constructor()
    ensures ValidBT()
    ensures fresh(listOfBloodBags)
    modifies this, BloodBags
    {
        var temp1 := new BloodBags();
        listOfBloodBags := temp1;
        bloodType := bloodtype;
        lowest := critical;
        quantity := 0;
    }
}