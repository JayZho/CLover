class BloodBag
{
    ghost var footprint: set<object>;
    var id: int;
    var bloodTypeName: string;
    var donorId: int;
    var expirayDate: int;
    var arrivalDate: int;
    
    predicate ValidBB()
    reads this
    {
        this in footprint &&
        id >= 0 &&
        donorId >= 0 &&
        expirayDate >= 0 &&
        arrivalDate >= 0 &&
        (bloodTypeName == "A" || bloodTypeName == "B" || bloodTypeName == "O" || bloodTypeName == "AB" || bloodTypeName == "")
    }

    constructor()
    ensures ValidBB()
    modifies this
    {
        id := 0;
        bloodTypeName := "";
        donorId := 0;
        expirayDate := 0;
        arrivalDate := 0;
        footprint := {this};
    }
    
    method getType() returns(value: string)
    requires ValidBB() 
    ensures ValidBB()
    ensures value == bloodTypeName
    {
        value := bloodTypeName;
    }

    method setType(BT: string)
    modifies this
    requires ValidBB()
    requires BT == "A" || BT == "B" || BT == "O" || BT == "AB"
    ensures fresh(footprint - old(footprint));
    ensures ValidBB()
    ensures bloodTypeName == BT
    {
        bloodTypeName := BT;
    }
 
    method getDonor() returns(value: int)
    requires ValidBB() 
    ensures ValidBB()
    ensures value == donorId
    {
        value := donorId;
    }

    method setDonor(newDonorId: int) 
    requires ValidBB()
    requires newDonorId >= 0
    ensures ValidBB()
    ensures fresh(footprint - old(footprint))
    ensures donorId == newDonorId
    modifies this
    {
        donorId := newDonorId;
    }

    
    method getArrivalDate() returns(value: int)
    requires ValidBB() 
    ensures ValidBB()
    ensures value == arrivalDate
    {
        value := arrivalDate;
    }

    method setArrivalDate(newArrivalDate: int) 
    requires ValidBB()
    requires newArrivalDate >= 0
    ensures ValidBB()
    ensures arrivalDate == newArrivalDate
    ensures fresh(footprint - old(footprint))
    modifies this
    {
        arrivalDate := newArrivalDate;
    }

    method getExpirayDate() returns (value: int)
    requires ValidBB()
    ensures ValidBB()
    ensures value == expirayDate
    {
        value := expirayDate;
    }

    method setExpirayDate(newExpirayDate: int) 
    requires ValidBB()
    requires newExpirayDate >= 0
    ensures ValidBB()
    ensures expirayDate == newExpirayDate
    ensures fresh(footprint - old(footprint))
    modifies this
    {
        expirayDate := newExpirayDate;
    }

    method isExpiredDate(currentDate: int) returns(expired: bool) 
    requires ValidBB()
    requires currentDate >= 0
    ensures ValidBB()
    ensures expirayDate <= currentDate ==> expired == false
    ensures fresh(footprint - old(footprint))
    modifies this
    {
        if (expirayDate <= currentDate) {
            expired := true;
        }
        expired := false;
    }
}

method Main(){
    var bloodyBag := new BloodBag();
    var bt :=  bloodyBag.getType();
    print bt;
    bloodyBag.setType("A");
    var bt1 :=  bloodyBag.getType();
    print bt1, '\n';
    bloodyBag.setDonor(21);
    var bt2 :=  bloodyBag.getDonor();
    print bt2, '\n';
    bloodyBag.setArrivalDate(5);
    var bt3 :=  bloodyBag.getArrivalDate();
    print bt3, '\n';
    bloodyBag.setExpirayDate(10);
    var bt4 :=  bloodyBag.getExpirayDate();
    print bt4, '\n';
    var bt5 :=  bloodyBag.isExpiredDate(7);
    print bt5, '\n';
}


