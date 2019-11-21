datatype BloodBags<B, C> = Leaf(B, B, B, C) 



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