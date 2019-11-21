datatype BloodBags<B, C> = Leaf(B, B, B, C) 



method Main() {
    var a : array<BloodBags<int, string>> := new BloodBags[7];
}