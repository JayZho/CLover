module BB {
    class BloodBag
    {
        ghost var footprint: set<object>;
        var id: int;
        var bloodType: string;
        var donorId: int;
        var expirayDate: string;
        var arrivalDate: string;
        
        predicate ValidBB()
        reads this, footprint
        {
            this in footprint &&
            id >= 0 &&
            donorId >= 0 &&
            (bloodType == "A" || bloodType == "B" || bloodType == "O")
        }

        constructor(newId: int, newBloodType: string, newDonorId: int, newExpirayDate: string, newArrivalDate: string) 
        requires newId >= 0
        requires newDonorId >= 0
        requires newBloodType == "A" || newBloodType == "B" || newBloodType == "O"
        ensures fresh(footprint - old(footprint))
        ensures ValidBB()
        modifies this, footprint
        {
            id := newId;
            bloodType := newBloodType;
            donorId := newDonorId;
            expirayDate := newExpirayDate;
            arrivalDate := newArrivalDate;
        }
    }
}