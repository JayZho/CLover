module BT {
    import A = BB
    class BloodType 
    {

        var bloodType: string;
        var lowest: int;
        var quantity: int;
        var listOfBloodBags: BloodBags;

        predicate ValidBT()
        reads this, BloodBags
        {
            lowest >= 0 &&
            quantity >= 0 &&
            (bloodType == 'A' || bloodType == 'B' || bloodType == 'O') 
        }

        constructor(bloodtype: string, critical: int)
        ensures ValidBT()
        ensures fresh(listOfBloodBags)
        modifies this, BloodBags
        {
            var temp1 := new BloodBags;
            
            bloodType := bloodtype;
            lowest := critical;
            //listOfBloodBags := array<A> := new A[10];
            quantity := 0;
        }
        A.BloodBags(1, "A", 1, "12/12/12", "12/12/12");
        
    }
}