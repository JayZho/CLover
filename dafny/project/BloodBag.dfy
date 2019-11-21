class BloodBag
{
    ghost var footprint: set<object>;
    var id: int;
    var bloodTypeName: string;
    var donorId: int;
    var expirayDate: int;
    var arrivalDate: int;
    
    predicate ValidBB()
    reads this, footprint
    {
        this in footprint &&
        id >= 0 &&
        donorId >= 0 &&
        expirayDate >= 0 &&
        arrivalDate >= 0 &&
        (bloodTypeName == "A" || bloodTypeName == "B" || bloodTypeName == "O" || bloodTypeName == "AB" || bloodTypeName == "")
    }

    constructor()
    requires ValidBB()
    ensures ValidBB()
    ensures fresh(footprint - old(footprint))
    modifies this, footprint
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
    modifies this, footprint
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
    modifies this, footprint
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
    modifies this, footprint
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
    modifies this, footprint
    {
        expirayDate := newExpirayDate;
    }

    method isExpiredDate(currentDate: int) returns(expired: bool) 
    requires ValidBB()
    requires currentDate >= 0
    ensures ValidBB()
    ensures expirayDate <= currentDate ==> expired == true
    ensures fresh(footprint - old(footprint))
    modifies this, footprint
    {
        if (expirayDate <= currentDate) {
            expired := false;
        }
        expired := true;
    }
}


