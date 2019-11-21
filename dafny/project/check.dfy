class Store // Dafny 2.3.0
{
 ghost var footprint: set<object>;
 var x: int;

 predicate Valid()
 reads this, footprint
 { this in footprint }

 constructor()
 ensures Valid()
 ensures x==0
 modifies this
 { x := 0; footprint := {this}; }

 method Sets(value: int) modifies this
 requires Valid(); ensures Valid()
 ensures x == value
 { x := value; }
 
 method Gets() returns (value: int)
 requires Valid()
 ensures x == value
 { value := x; }
}

method Verify() {
 var s := new Store();
 var i := s.Gets();
 assert i == 0; // verify init
 s.Sets(-12345);
 i := s.Gets();
 assert i == s.x == -12345;
 // verify the operations
}