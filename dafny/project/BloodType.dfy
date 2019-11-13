module BT {
    import A = BB
    class BloodType 
    {

        var bloodType: string;
        var lowest: int;
        var quantity: int;
        var listOfBloodBags: array<bloodBags>;

        predicate ValidBT()
        reads this
        {
            lowest >= 0 &&
            quantity >= 0 &&
            (bloodType == 'A' || bloodType == 'B' || bloodType == 'O') 
        }

        constructor(bloodtype: string, critical: int)
        ensures ValidBT()
        modifies this
        {
            bloodType := bloodtype;
            lowest := critical;
            //listOfBloodBags := array<A> := new A[10];
            quantity := 0;
        }
        A.BloodBags(1, "A", 1, "12/12/12", "12/12/12");
        
    }
}