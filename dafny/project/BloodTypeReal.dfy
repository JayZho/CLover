datatype BloodType<B, C> = Leaf(B, B, B, C) | Node(B, B, B, C, BloodType<B, C>)

method Print(t:BloodType<int, string>) // BOTTOM-UP
{
    match t
        case Leaf(n, l, r, k) => print n, ' ', l, ' ', r, ' ', k, ' '; 
        case Node(n,l,r,k, p) => { print n, ' ', l, ' ', r, ' ', k, ' '; Print(p); }
}
method Main(){
    var Leaf1:BloodType<int, string> := Leaf(1, 2, 3, "A");
    var t1:BloodType<int, string> := Node(2, 7, 5, "B", Leaf1);
    Print(t1); print '\n'; 

}