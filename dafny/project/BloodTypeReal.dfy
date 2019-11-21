datatype BloodType<B> = Leaf(B, B, B) | Node(B, B, B, BloodType<B>)

method Print(t:BloodType<int>) // BOTTOM-UP
{
    match t
        case Leaf(n, l, r) => print n, ' ', l, ' ', r, ' '; 
        case Node(n,l,r,k) => { print n, ' ', l, ' ', r, ' '; Print(k); }
}
method Main(){
    var Leaf1:BloodType<int> := Leaf(1, 2, 3);
    var t1:BloodType<int> := Node(2, 7, 5, Leaf1);
    Print(t1); print '\n'; 

}